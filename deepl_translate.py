import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("DEEPL_API_KEY")
if not API_KEY:
    raise ValueError("Missing API key from .env file")

# free keys end in :fx
URL = (
    "https://api-free.deepl.com/v2/translate"
    if API_KEY.endswith(":fx")
    else "https://api.deepl.com/v2/translate"
)


def translate_sentences(sentences, target_lang="EN-US"):
    response = requests.post(
        URL,
        headers={"Authorization": f"DeepL-Auth-Key {API_KEY}"},
        json={"text": sentences, "target_lang": target_lang},
    )

    response.raise_for_status()
    return [t["text"] for t in response.json()["translations"]]


example_sentences = ["Γειά σου, τί κάνεις;", "Καλημέρα και καλή καρδιά"]
results = translate_sentences(example_sentences)
print(results)
