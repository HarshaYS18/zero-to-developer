def rev(text):
    rev =""
    for ch in text  :
        rev = ch+rev
    return rev

text = input("Enter text: ")
result = rev(text)
print (result)