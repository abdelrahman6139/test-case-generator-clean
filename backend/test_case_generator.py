from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
import subprocess
import json
import regex as re
import time

load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:3000"])

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

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

        prompt = (
            "You are an AI that generates structured test cases in JSON format.\n"
            f"Generate from 5 to 10 test cases in JSON format for the following requirement:\n\n"
            f"{requirement}\n\n"
            "The test case should include:\n"
            "- id\n"
            "- test_case_id\n"
            "- topic\n"
            "- test_scenario\n"
            "- test_steps (as a list)\n"
            "- expected_intended_result\n"
            "- pass_fail_criteria\n"
            "- selenium_script (Python Selenium Script using webdriver.Chrome and unittest).\n"
            "Return valid JSON ONLY"
        )

        response = model.generate_content(prompt)
        test_cases = response.text.strip().removeprefix("```json").removesuffix("```").strip()

        parsed = safe_parse_json_objects(test_cases)
        saved_files = []

        for i, tc in enumerate(parsed):
            filename = f"test_case_{len(os.listdir(TEST_CASE_DIR)) + 1}_{i+1}.py"
            path = os.path.join(TEST_CASE_DIR, filename)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(tc.get("selenium_script", ""))
            tc["script_filename"] = filename
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

    time.sleep(0.3)  # 🔐 تأخير بسيط يضمن كتابة الملف قبل التنفيذ

    result = subprocess.run(['pytest', filename, '--alluredir=api/results'], capture_output=True, text=True)

    log_filename = f"api/results/last_log_{index}.txt" if index is not None else "api/results/last_log.txt"
    with open(log_filename, "w", encoding="utf-8") as log_file:
        log_file.write(result.stdout + "\n" + result.stderr)

    if result.returncode == 0:
        return jsonify({
            "message": "✅ Script passed",
            "result": "passed",
            "stdout": result.stdout
        }), 200
    else:
        return jsonify({
            "message": "⚠️ Script ran with issues",
            "result": "failed",
            "stdout": result.stdout,
            "stderr": result.stderr
        }), 200

@app.route('/test_result_log', methods=['GET'])
def test_result_log():
    try:
        index = request.args.get("index")
        log_path = f"api/results/last_log_{index}.txt" if index else "api/results/last_log.txt"

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
        subprocess.run(['allure', 'serve', 'api/results'], shell=True)
        return "Report opened", 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True, use_reloader=False)  # ✅ الحل النهائي
