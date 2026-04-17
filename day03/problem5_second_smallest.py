a = list(map(int, input("Enter numbers: ").split()))

aSmall = a[0]
bSmall = float('inf')

for num in a:
    if aSmall>num:
        bSmall = aSmall
        aSmall = num
    elif aSmall<num<bSmall:
        bSmall = num
print(bSmall)