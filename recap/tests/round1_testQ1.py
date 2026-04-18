###PALINDROME####


a = int(input("Enter number: "))


original = a
rev = 0

while a > 0:
    digit = a % 10
    rev = rev * 10 + digit
    a = a // 10

if rev == original:
    if original % 2 == 0:
        print("Even Palindrome")
    else:
        print("Odd Palindrome")
else:
    print("Not Palindrome")