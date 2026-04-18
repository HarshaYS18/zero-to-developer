a = list(map(int, input("Enter numbers:").split()))

a.sort()

k = int(input("Enter the minimum you want to find:"))

l = int(input("Enter the maximum you want to find:"))

if k > 0 and k <= len(a):
    req_min = a[k-1]
    print (k,"th", "smallest is:", req_min)
else:
    print("There is no such minimum: \n", "Try Again:-(")

if l > 0 and l <= len(a):
    req_max = a[len(a)-l]
    print (l,"th", "largest is:", req_max)
else:
    print("There is no such maximum: \n", "Try Again:-(")