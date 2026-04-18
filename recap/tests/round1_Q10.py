list1 = list(map(int, input("Enter numbers for first list:").split()))
list2 = list(map(int, input("Enter numbers for second list:").split()))

result = list1.copy()

for num in list2:
    if num not in result:
        result.append(num)
print(result)