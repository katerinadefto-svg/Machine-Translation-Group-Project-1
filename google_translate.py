import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_TRANSLATE_API_KEY")
if not API_KEY:
    raise ValueError("Missing API key in .env file")

URL = "https://translation.googleapis.com/language/translate/v2"


def translate_sentences(sentences, target_lang="en"):
    response = requests.post(
        URL,
        params={"key": API_KEY},
        json={"q": sentences, "target": target_lang, "format": "text"},
    )
    response.raise_for_status()
    translations = response.json()["data"]["translations"]
    return [t["translatedText"] for t in translations]


example_sentences = ["Γειά σου, τί κάνεις;", "Καλημέρα και καλή καρδιά"]
results = translate_sentences(example_sentences)
print(results)
