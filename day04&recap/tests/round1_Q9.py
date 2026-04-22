list1 = list(map(int, input("Enter numbers for first list:").split()))
list2 = list(map(int, input("Enter numbers for second list:").split()))
result = []
for num in list1:
    if num in list2 and num not in result:
        result.append(num)
print(result)