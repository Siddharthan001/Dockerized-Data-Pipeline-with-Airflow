import requests
from bs4 import BeautifulSoup
import yaml
import json
import os
from utils import upload_to_s3

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.yaml")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def crawl_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return None

if __name__ == "__main__":
    all_data = {}
    for site in config["websites"]:
        print(f"Crawling: {site}")
        content = crawl_website(site)
        if content:
            all_data[site] = content

    output_file = os.path.join(OUTPUT_DIR, "raw_data.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2)

    print(f"Data saved to {output_file}")

    if config["aws"]["upload"]:
        upload_to_s3(output_file, config["aws"]["bucket_name"], "raw_data.json")
