def rev(text):
    rev = ""
    for ch in text:
        rev = ch+rev
    return rev
text = input("Enter Text:").lower().strip()
result = rev(text)

print(result)