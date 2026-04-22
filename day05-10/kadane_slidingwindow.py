text = input("Enter text:")

left = 0
seen = set()
max_length = 0
best_start = 0
best_end = 0

for right in range(len(text)):
    ch = text[right]
    while ch in seen:
        seen.remove(text[left])
        left += 1
    seen.add(ch)
    if right - left + 1 > max_length:
        max_length = right - left + 1
        best_start = left
        best_end = right
print("Longest lenghth:", max_length)
print("Longest substring:", text[best_start:best_end+1])