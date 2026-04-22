number = list(map(int, input("Enter numbers:").split()))

seen =[]

for num in number:
    if num in seen:
        print(num)
        break
    else:
        seen.append(num)