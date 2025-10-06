import requests

API_KEY = "8bd26cbd59msha2ac41ef2cffed5p131458jsnae18841f06fc"
API_HOST = "namedentityrecognition.p.rapidapi.com"
API_URL = f"https://{API_HOST}/ner"

def ner(text):
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST,
        "Content-Type": "application/json"
    }
    payload = {"text": text}
    response = requests.post(API_URL, json=payload, headers=headers)
    data = response.json()

    # ✅ Normalize the format
    formatted = {"entities": []}
    for ent in data.get("entities", []):
        formatted["entities"].append({
            "name": ent.get("text"),
            "category": label_to_category(ent.get("label")),
            "confidence_score": ent.get("confidence_score", None)
        })
    return formatted

def label_to_category(label):
    """Map NER labels to readable categories"""
    mapping = {
        "ORG": "organization",
        "PERSON": "person",
        "GPE": "place",
        "LOC": "place",
        "DATE": "date",
        "TIME": "time",
        "EVENT": "event"
    }
    return mapping.get(label, label.lower() if label else "unknown")

if __name__ == "__main__":
    result = ner("Apple is opening a new office in New York.")
    print(result)
