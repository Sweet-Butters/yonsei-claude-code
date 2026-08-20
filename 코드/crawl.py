import csv
from scrapling.fetchers import Fetcher

page = Fetcher.get("https://quotes.toscrape.com/")
print("status:", page.status)

rows = []
for q in page.css(".quote"):
    rows.append({
        "text":   q.css(".text")[0].text,
        "author": q.css(".author")[0].text,
        "tags":   ",".join(t.text for t in q.css(".tag")),
    })

with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
    w.writeheader()
    w.writerows(rows)

print(f"{len(rows)}개 저장 -> quotes.csv")
