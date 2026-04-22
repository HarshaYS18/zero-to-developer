numbers = list(map(int, input("Enter numbers:").split()))
k = int(input("Enter the max size for the subarray:"))

left = 0
window_sum = 0
max_sum = float('-inf')

for right in range(len(numbers)):
    window_sum = window_sum+numbers[right]
    if right - left + 1 == k:
        max_sum = max(max_sum, window_sum)
        window_sum -= numbers[left]
        left += 1
print("Maximum for the subarray of given lenghth:",max_sum)
print("The subarray is:",numbers[left-1:right+1])