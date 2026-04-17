def sum_list(numbers):
    total = 0
    for num in numbers:
        total = num+total
    return total
numbers = list(map(int, input("Enter numbers: ").split()))

result = sum_list(numbers)
print(result)