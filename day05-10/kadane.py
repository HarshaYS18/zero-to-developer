numbers = list(map(int, input("Enter numbers:").split()))

current_max = numbers[0]
max_sum = numbers[0]

for num in range(1, len(numbers)):
    element = numbers[num]
    
    current_max = max(element, current_max+element)
    max_sum = max(current_max, max_sum)
print(max_sum)