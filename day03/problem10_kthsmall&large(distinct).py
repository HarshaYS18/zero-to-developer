a = list(map(int, input("Enter numbers:").split()))

a.sort()

b = []

for num in a:
    if num not in b:
        b.append(num)

k = int(input("Enter the minimum you want to find:"))

l = int(input("Enter the maximum you want to find:"))

if k > 0 and k <= len(b):
    req_min = b[k-1]
    print (k,"th", "smallest is:", req_min)
else:
    print("There is no such minimum: \n", "Try Again:-(")

if l > 0 and l <= len(b):
    req_max = b[len(b)-l]
    print (l,"th", "largest is:", req_max)
else:
    print("There is no such maximum: \n", "Try Again:-(")