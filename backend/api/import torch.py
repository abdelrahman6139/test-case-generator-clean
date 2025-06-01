import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Set your model path
MODEL_PATH = "./final_model"

try:
    # Load Tokenizer and Model
    tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
    model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
    model.eval()

    # Test Classification
    sentence = "This is a test sentence for classification."
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True, padding=True, max_length=128)
    
    with torch.no_grad():
        output = model(**inputs)
    
    prediction = torch.argmax(output.logits, dim=1).item()
    print("Model Loaded Successfully ✅")
    print("Prediction Output:", prediction)

except Exception as e:
    print("Error Loading Model ❌")
    print(e)
