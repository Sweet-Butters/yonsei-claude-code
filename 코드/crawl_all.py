import csv
from scrapling.fetchers import Fetcher

BASE = "https://quotes.toscrape.com"
url, rows = BASE + "/", []

for page_no in range(1, 4):
    page = Fetcher.get(url)
    for q in page.css(".quote"):
        rows.append({
            "text":   q.css(".text")[0].text,
            "author": q.css(".author")[0].text,
            "tags":   ",".join(t.text for t in q.css(".tag")),
        })
    print(f"{page_no}페이지 완료 - 누적 {len(rows)}행")
    nxt = page.css("li.next a")
    if not nxt:
        break
    url = BASE + nxt[0].attrib["href"]

with open("quotes_all.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
    w.writeheader(); w.writerows(rows)

print(f"총 {len(rows)}행 -> quotes_all.csv")
