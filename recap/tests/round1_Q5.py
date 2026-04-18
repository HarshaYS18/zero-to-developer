def maxi(numbers):
    maxi = 0
    for num in numbers:
        if maxi < num:
            maxi = num
    return maxi

number = list(map(int, input("Enter numbers:").split()))

result = maxi(number)

print(result)