from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import subprocess
import json
import regex as re
import time
from dotenv import load_dotenv
import google.generativeai as genai
import shutil
import platform




load_dotenv()
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(os.getenv("MONGO_URI"))
db = client["mydatabase"]  # نفس اسم الداتابيز اللي في URI
history_collection = db["test_history"]  # اسم الكولكشن الجديد لحفظ التستات


app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:3000"])

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

# File system setup
TEST_CASE_DIR = "api/test_cases"
REPORT_DIR = "api/results"
os.makedirs(TEST_CASE_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

def safe_parse_json_objects(json_str):
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        json_objects = re.findall(r'\{(?:[^{}]|(?R))*\}', json_str)
        parsed_objects = []
        for obj in json_objects:
            try:
                parsed_objects.append(json.loads(obj))
            except Exception as e:
                print("⛔ Failed to parse one object:", e)
        return parsed_objects

@app.route('/generate_test_case', methods=['POST'])
def generate_test_case():
    try:
        data = request.get_json()
        requirement = data.get("requirement")
        if not requirement:
            return jsonify({"error": "No requirement provided"}), 400

        prompt = f"""
You are a professional QA engineer who writes **accurate Python Selenium test scripts** using `webdriver.Chrome` and `unittest`.

🎯 Your goal is to generate between **5 and 10 unique test cases** for the requirement below.

Each test case must be returned in **pure JSON array format**.

### Required Format:
Each test case must include the following fields:
- id (integer)
- test_case_id (string)
- topic (string)
- test_scenario (string)
- expected_intended_result (string)
- pass_fail_criteria (string)
- test_steps (array of strings)
- selenium_script (string) → a valid Python Selenium test script using unittest

---

### ⚠️ Critical Requirements:
- ✅ Each `selenium_script` must use `import unittest` and run with `pytest`
- ✅ Every script **must contain at least one `assert`** statement that determines whether the test passes or fails
- ✅ Do **NOT** rely only on `print()` statements
- ✅ All test cases must be returned in **one JSON array**, no markdown, no explanations
- ❌ DO NOT wrap in ```json or ```python
- ❌ DO NOT include summaries or extra text

---

### ✅ FEW-SHOT EXAMPLES (For Reference)

[
  {{
    "id": 1,
    "test_case_id": "TC_Login_001",
    "topic": "Login Functionality",
    "test_scenario": "User logs in with valid credentials",
    "expected_intended_result": "User is redirected to secure area",
    "pass_fail_criteria": "Page contains the text 'You logged into a secure area!'",
    "test_steps": [
      "Go to login page",
      "Enter valid username and password",
      "Click login button"
    ],
    "selenium_script": "import unittest\\nfrom selenium import webdriver\\nfrom selenium.webdriver.common.by import By\\n\\nclass LoginTest(unittest.TestCase):\\n    def setUp(self):\\n        self.driver = webdriver.Chrome()\\n\\n    def test_valid_login(self):\\n        driver = self.driver\\n        driver.get('https://the-internet.herokuapp.com/login')\\n        driver.find_element(By.ID, 'username').send_keys('tomsmith')\\n        driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')\\n        driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()\\n        message = driver.find_element(By.ID, 'flash').text\\n        self.assertIn('You logged into a secure area!', message)\\n\\n    def tearDown(self):\\n        self.driver.quit()\\n\\nif __name__ == '__main__':\\n    unittest.main()"
  }},
  {{
    "id": 2,
    "test_case_id": "TC_Login_002",
    "topic": "Login Functionality",
    "test_scenario": "User logs in with invalid password",
    "expected_intended_result": "User sees an error message",
    "pass_fail_criteria": "Error message contains 'Your password is invalid!'",
    "test_steps": [
      "Go to login page",
      "Enter valid username and invalid password",
      "Click login button"
    ],
    "selenium_script": "import unittest\\nfrom selenium import webdriver\\nfrom selenium.webdriver.common.by import By\\n\\nclass InvalidLoginTest(unittest.TestCase):\\n    def setUp(self):\\n        self.driver = webdriver.Chrome()\\n\\n    def test_invalid_password(self):\\n        driver = self.driver\\n        driver.get('https://the-internet.herokuapp.com/login')\\n        driver.find_element(By.ID, 'username').send_keys('tomsmith')\\n        driver.find_element(By.ID, 'password').send_keys('WrongPassword123')\\n        driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()\\n        error = driver.find_element(By.ID, 'flash').text\\n        self.assertIn('Your password is invalid!', error)\\n\\n    def tearDown(self):\\n        self.driver.quit()\\n\\nif __name__ == '__main__':\\n    unittest.main()"
  }}
]

---

Now generate between 5 and 10 test cases for this requirement:

\"{requirement}\"
"""

        response = model.generate_content(prompt)
        test_cases = response.text.strip().removeprefix("```json").removesuffix("```").strip()

        parsed = safe_parse_json_objects(test_cases)
        saved_files = []

        for i, tc in enumerate(parsed):
            script = tc.get("selenium_script", "")
            if "assert" not in script:
                continue

            filename = f"test_case_{len(os.listdir(TEST_CASE_DIR)) + 1}_{i+1}.py"
            path = os.path.join(TEST_CASE_DIR, filename)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(script)

            # ✅ Save to MongoDB
            test_doc = {
                "requirement": requirement,
                "script_filename": filename,
                "selenium_script": script,
                "status": "not_run",
                "userId": data.get("user_id"),
                "created_at": time.time()
            }

            inserted = history_collection.insert_one(test_doc)
            tc["_id"] = str(inserted.inserted_id)

            saved_files.append(filename)



             

        return jsonify({
            "message": "Test cases generated and saved",
            "saved_files": saved_files,
            "test_cases": parsed
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route('/run_custom_script', methods=['POST'])
def run_custom_script():
    data = request.get_json()
    script = data.get('script')
    index = data.get('index')

    if not script:
        return jsonify({"error": "No script provided"}), 400

    filename = "api/test_cases/custom_test.py"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(script)

    time.sleep(0.5)

    result = subprocess.run([
        'pytest', filename, '--tb=short', '--disable-warnings', f'--alluredir={REPORT_DIR}'
    ], capture_output=True, text=True)

    log_filename = f"{REPORT_DIR}/last_log_{index}.txt" if index else f"{REPORT_DIR}/last_log.txt"
    with open(log_filename, "w", encoding="utf-8") as log_file:
        log_file.write(result.stdout + "\n" + result.stderr)

    stdout_lower = result.stdout.lower()
    stderr_lower = result.stderr.lower()

    failed = "failed" in stdout_lower or "error" in stdout_lower or "exception" in stderr_lower
    passed = "1 passed" in stdout_lower and not failed

    # ✅ Update test history in MongoDB
    if index:
        try:
            _id = ObjectId(index)
            history_collection.update_one(
                {"_id": _id},
                {
                    "$set": {
                        "status": "passed" if passed else "failed",
                        "stdout": result.stdout,
                        "stderr": result.stderr,
                        "executed_at": time.time()
                    }
                }
            )
        except Exception as e:
            print("⛔ Failed to update MongoDB history:", e)

    return jsonify({
        "message": "✅ Script passed" if passed else "❌ Script failed",
        "result": "passed" if passed else "failed",
        "stdout": result.stdout,
        "stderr": result.stderr
    }), 200


@app.route('/test_result_log', methods=['GET'])
def test_result_log():
    try:
        index = request.args.get("index")
        log_path = f"{REPORT_DIR}/last_log_{index}.txt" if index else f"{REPORT_DIR}/last_log.txt"

        if not os.path.exists(log_path):
            return jsonify({"message": "No result log found"}), 404

        with open(log_path, 'r', encoding='utf-8') as file:
            content = file.read()

        return jsonify({"log": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/show_report', methods=['GET'])
def show_report():
    try:
        # ✅ Adjust path to match your system's Allure installation
        allure_path = r"C:\allure-2.34.0\bin\allure.bat"
        command = [allure_path, 'serve', 'api/results']

        if platform.system() == "Windows":
            # 🚀 Start in new console window without freezing Flask
            subprocess.Popen(command, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            subprocess.Popen(command)

        return "✅ Allure report is opening in a new browser tab...", 200
    
    except Exception as e:
        return jsonify({"error": f"Allure failed: {str(e)}"}), 500

@app.route("/get_history", methods=["GET"])
def get_history():
    user_id = request.args.get("userId")
    try:
        # بدل ObjectId(user_id) بـ user_id لأنك بتخزنها كنص
        records = list(history_collection.find({"userId": user_id}))
        for r in records:
            r["_id"] = str(r["_id"])
            r["userId"] = str(r["userId"])
        return jsonify(records), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/delete_history", methods=["DELETE"])
def delete_history():
    history_id = request.args.get("id")
    if not history_id:
        return jsonify({"error": "Missing ID"}), 400
    try:
        result = history_collection.delete_one({"_id": ObjectId(history_id)})
        return jsonify({"message": "Deleted", "deleted": result.deleted_count}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500    
    
    

if __name__ == '__main__':
    # Clean Allure results once on server startup
    if os.path.exists(REPORT_DIR):
        shutil.rmtree(REPORT_DIR)
    os.makedirs(REPORT_DIR, exist_ok=True)
    print("🧹 Allure results cleared on startup.")

    app.run(port=5001, debug=True, use_reloader=False)

