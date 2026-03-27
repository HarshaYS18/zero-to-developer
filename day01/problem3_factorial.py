# Take input from the user
num = int(input("Enter a positive integer to calculate factorial: "))

# Initialize factorial
factorial = 1

# Loop to calculate factorial
for i in range(1, num + 1):
    factorial *= i

# Print the final factorial
print("The factorial of", num, "is", factorial)