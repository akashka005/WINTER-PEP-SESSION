from collections import Counter
s = input().strip()
frq = Counter(s)
for ch, count in frq.items():
    print(ch, count, end = " \n")


#or 

s = input().strip()
freq = set()

for ch in s:
    if ch not in freq:
        count = 0
        for c in s:
            if c == ch:
                count += 1
print(ch, count, c)