from flask import Flask, request, jsonify
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model
MODEL_PATH = "./final_model"  # Ensure the path is correct
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

@app.route('/classify', methods=['POST'])
def classify():
    try:
        print("Classify API Hit")  # Debug log
        data = request.get_json()
        print("Received Data:", data)  # Debug log

        if not data or 'sentences' not in data:
            return jsonify({"error": "No sentences provided"}), 400

        sentences = data['sentences']
        results = [classify_sentence(sentence) for sentence in sentences]
        return jsonify({"results": results})

    except Exception as e:
        print(f"Error in classify route: {e}")  # Debug log
        return jsonify({"error": str(e)}), 500

def classify_sentence(sentence):
    """Classifies a given sentence as 'Requirement' or 'Not Requirement'."""
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        output = model(**inputs)
    prediction = torch.argmax(output.logits, dim=1).item()
    return "Requirement" if prediction == 1 else "Not Requirement"

if __name__ == '__main__':
    print("Starting Flask server...")  # Debug log
    app.run(host='0.0.0.0', port=5000, debug=True)
