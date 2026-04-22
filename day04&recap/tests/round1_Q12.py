list1 = list(map(int, input("Enter numbers of list1:").split()))
list2 = list(map(int, input("Enter numbers of list2:").split()))

freq1 = {}
freq2 = {}

for num in list1:
        if num in freq1:
            freq1[num] = freq1[num]+1
        else:
            freq1[num] = 1
for num in list2:
        if num in freq2:
            freq2[num] = freq2[num]+1
        else:
            freq2[num] = 1
if freq1.items() == freq2.items():
    print("Anagram")
else:
     print("Not an anagram")