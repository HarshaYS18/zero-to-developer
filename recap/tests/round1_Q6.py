def second_max(numbers):
    first_max = -float('inf')
    second_max = -float("inf")

    for num in numbers:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num!=first_max and num > second_max:
            second_max = num
    if second_max == -float('inf'):
        return "No Second_max"
    return second_max

number = list(map(int, input("Enter numbers:").split()))

print(second_max(number))