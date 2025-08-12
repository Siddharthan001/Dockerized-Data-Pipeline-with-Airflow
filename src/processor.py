import json
import os
import re
from utils import upload_to_s3
import yaml

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.yaml")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s.,!?]', '', text)  # Remove unwanted chars
    return text.strip()

if __name__ == "__main__":
    raw_file = os.path.join(OUTPUT_DIR, "raw_data.json")
    processed_file = os.path.join(OUTPUT_DIR, "processed_data.json")

    with open(raw_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    processed_data = {site: clean_text(content) for site, content in data.items()}

    with open(processed_file, "w", encoding="utf-8") as f:
        json.dump(processed_data, f, indent=2)

    print(f"Processed data saved to {processed_file}")

    if config["aws"]["upload"]:
        upload_to_s3(processed_file, config["aws"]["bucket_name"], "processed_data.json")
