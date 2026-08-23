import csv
rows = list(csv.DictReader(open("quotes.csv", encoding="utf-8-sig")))
print(f"{'#':>2}  {'author':<22} tags")
print("-" * 52)
for i, r in enumerate(rows[:8], 1):
    print(f"{i:>2}  {r['author']:<22} {r['tags'][:24]}")
