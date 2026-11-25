import csv

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
rows = []

for item in soup.select(".quote"):
    rows.append({
        "quote": item.select_one(".text").get_text(strip=True),
        "author": item.select_one(".author").get_text(strip=True),
    })

with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=["quote", "author"])
    writer.writeheader()
    writer.writerows(rows)

print(f"抓取完成，共 {len(rows)} 条")
