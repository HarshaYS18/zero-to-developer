# Day 1 – Problem 1: Largest Number Tracker
# List of numbers
nums = [4, 1, 6, 3, 9, 2]

# Start with the first number as current max
current_max = nums[0]

# Loop through numbers and compare with current_max
for i in range(len(nums) - 1):
    if nums[i+1] > current_max:          # Compare next number with current max
        print(nums[i+1], "is greater than", current_max)
        current_max = nums[i+1]          # Update current max if bigger
    else:
        print(current_max, "is greater than", nums[i+1])

# Print the final largest number
print("The largest number is", current_max)