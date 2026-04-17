a = list(map(int, input("Enter numbers:").split()))

aLarge = a[0]
bLarge = float('inf')

for num in a:
    if aLarge < num:
        bLarge = aLarge
        aLarge = num
    elif aLarge>num>bLarge:
        bLarge = num
print("First Highest:",aLarge)
print("Second Highest:",bLarge)