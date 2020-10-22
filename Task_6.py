ans = {}
with open('text.txt', encoding="utf-8") as text:
    for line in text:
        name, stats = line.split(':')
        name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        ans[name] = name_sum
print(ans)
