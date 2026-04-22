###ELIMINATE DUPLICATES####

numbers = list(map(int, input("Enter the numbers:").split()))

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)
print("Unique elements:", unique)