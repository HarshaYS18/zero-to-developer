def freq(numbers):
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] = freq[num]+1
        else:
            freq[num] = 1
    for key in freq:
        print(key, "->", freq[key])
    return freq

number = list(map(int, input("Enter numbers:").split()))

print(freq(number))