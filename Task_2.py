a = open(r"text.txt", "r", encoding="utf-8")

for i, line in enumerate(a, 1):
    print(f"В {i} строке {len(line.split())} слов")

a.close()
