def num(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)
    return result


number = list(map(int, input("Enter numbers:").split()))

print(num(number))