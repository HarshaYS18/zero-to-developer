text = input("Enter a string: ").lower().strip()
count = 0
for ch in text:
    if ch in "aeiou":
        count = count + 1
print(count)