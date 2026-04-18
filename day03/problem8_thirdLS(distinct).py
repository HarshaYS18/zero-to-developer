a = list(map(int, input("Input numbers:").split()))

fSmall = a[0]
sSmall = float('inf')
tSmall = float('inf')

for num in a[1:]:
    if fSmall>num:
        tSmall = sSmall
        sSmall = fSmall
        fSmall = num
    elif fSmall<num<sSmall:
        tSmall = sSmall
        sSmall = num
    elif sSmall<num<tSmall:
        tSmall = num
if tSmall == float('inf'):
    print("No third smallest exists")
else:
    print("Third Smallest number is:",tSmall)


fLarge = a[0]
sLarge = -float('inf')
tLarge = -float('inf')

for num in a[1:]:
    if fLarge < num:
        tLarge = sLarge
        sLarge = fLarge
        fLarge = num
    elif fLarge > num > sLarge:
        tLarge = sLarge
        sLarge = num
    elif sLarge > num > tLarge:
        tLarge = num
if tLarge == -float('inf'):
    print("Third Largest number doesn't exist in the input provided: \n", "Please try again")
else:
    print("Third Largest Number is:", tLarge)