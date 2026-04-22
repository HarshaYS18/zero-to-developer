numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

seen = {}

for i in range(len(numbers)):
    num = numbers[i]
    complement = target  - num
    if complement in seen:
        print([seen[complement],i])
        break
    else:
        seen[num]=i