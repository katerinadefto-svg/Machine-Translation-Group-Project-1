import os
import uuid
import requests
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("AZURE_TRANSLATOR_KEY")
REGION = os.getenv("AZURE_TRANSLATOR_REGION")
if not KEY or not REGION:
    raise ValueError("Missing KEY or REGION in .env file")

URL = "https://api.cognitive.microsofttranslator.com/translate"


def translate_sentences(sentences, target_lang="en"):
    headers = {
        "Ocp-Apim-Subscription-Key": KEY,
        "Ocp-Apim-Subscription-Region": REGION,
        "Content-Type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4()),
    }
    params = {"api-version": "3.0", "to": [target_lang]}
    body = [{"text": s} for s in sentences]

    response = requests.post(URL, params=params, headers=headers, json=body)
    response.raise_for_status()

    return [item["translations"][0]["text"] for item in response.json()]


example_sentences = ["Γειά σου, τί κάνεις;", "Καλημέρα και καλή καρδιά"]
results = translate_sentences(example_sentences)
print(results)
