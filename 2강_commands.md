# 2강 — GitHub에서 가져와 직접 크롤링

## URL

```
https://github.com/D4Vinci/Scrapling
```
```
https://pypi.org/project/scrapling/
```
```
https://quotes.toscrape.com/
```

## git clone

```
git clone https://github.com/D4Vinci/Scrapling.git
```

가져온 것 확인.

```
ls
```
```
git log --oneline -5
```

## 설치

가상환경을 먼저 만듭니다.

```
python -m venv .venv
```

Windows에서 활성화:

```
.venv\Scripts\activate
```

macOS · Linux에서 활성화:

```
source .venv/bin/activate
```

설치. **`[fetchers]`를 빼면 `Fetcher`를 쓸 수 없습니다.**

```
pip install "scrapling[fetchers]"
```

> `pip install scrapling` 만 하면 파싱 기능만 깔립니다.
> 웹페이지를 가져오는 `Fetcher`는 `curl_cffi` 등이 필요해서 `[fetchers]`가 있어야 합니다.
> (scrapling 0.4.14 기준 · 2026-08-20 실행 확인)

## 첫 크롤링

> 아래 코드는 [`코드/crawl.py`](코드/crawl.py)에 그대로 들어 있습니다. 파일을 받아 쓰셔도 됩니다.

```python
from scrapling.fetchers import Fetcher

page = Fetcher.get("https://quotes.toscrape.com/")
print(page.status)

for q in page.css(".quote"):
    print(q.css(".text")[0].text, "|", q.css(".author")[0].text)
```

## CSV로 저장

```python
import csv
from scrapling.fetchers import Fetcher

rows = []
page = Fetcher.get("https://quotes.toscrape.com/")
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
```

## 막혔을 때 Claude Code에 넣을 지시

```
github의 scrapling을 쓰고 싶어. README와 공식 문서를 읽고,
지금 내 환경에서 무엇이 되고 무엇이 안 되는지 표로 정리해줘.
```


## 여러 페이지 크롤링 (검증 완료 · 30행)

> [`코드/crawl_all.py`](코드/crawl_all.py)

```python
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
```

> 2026-08-20 실행 확인 — 3페이지 30행.
