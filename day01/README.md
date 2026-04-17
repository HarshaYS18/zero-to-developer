# Day 1 – Python Fundamentals 🐍

**Author:** Sree Harsha Reddy

Welcome to Day 1 of my Python practice journey! This repository focuses on the core building blocks of Python: lists, dictionaries, loops, and conditionals.

---

## 📁 Repository Contents

This folder contains three distinct practice problems:
1. [Problem 1: Largest Number Tracker](#problem-1--largest-number-tracker)
2. [Problem 2: File Type Classifier](#problem-2--file-type-classifier)
3. [Problem 3: Factorial Calculator](#problem-3--factorial-calculator)

---

## Problem 1 – Largest Number Tracker

**File Name:** `problem1_largest_number.py`

### 🎯 Goal
Find the largest number in a list by comparing each element.

### 💡 Approach
1. Start with the first number as `current_max`.
2. Compare each number with `current_max` in a loop.
3. Update `current_max` if a number is greater.
4. At the end, `current_max` holds the largest number.

### 💻 Code
```python
nums = [4, 1, 6, 3, 9, 2]
current_max = nums[0]

for i in range(len(nums) - 1):
    if nums[i+1] > current_max:
        current_max = nums[i+1]

print("The largest number is", current_max)

🚀 Example Output
The largest number is 9

---

## Problem 2 – File Type Classifier

**File Name:** `problem2_file_type.py`

### 🎯 Goal
Take multiple filenames from the user and classify them as Images, Text, or Unknown based on their file extensions.

### 💡 Approach
1. Split user input into a list of filenames.
2. Loop through each filename and check its extension.
3. Use a dictionary to map extensions to file types.
4. Print the type of each file, or `Unknown` if not listed.

### 💻 Code
```python
filename = input(
    "Input multiple file names in this format:\nEg: xyz.zip,abc.img,demi.god\nInput: "
).strip().lower()

file_list = filename.split(",")

file_type = {
    "Images": [".jpg", ".gif", ".png"],
    "Text": [".txt", ".pdf", ".doc"]
}

for ext in file_list:
    found = False
    for fn, ft in file_type.items():
        if ext.endswith(tuple(ft)):
            print(ext, "->", fn)
            found = True
            break
    if not found:
        print(ext, "-> Unknown ⚠️")

🚀 Example Input / Output
Input: cat.pdf, ant.jpg, pig.txt, mouse.rar

Output:
cat.pdf -> Text
ant.jpg -> Images
pig.txt -> Text
mouse.rar -> Unknown ⚠️

---

***
## Problem 3 – Factorial Calculator

**File Name:** `problem3_factorial.py`

### 🎯 Goal
Calculate the factorial of a positive integer entered by the user.

### 💡 Approach
1. Initialize `factorial` as `1`.
2. Loop from `1` to the number entered by the user.
3. Multiply `factorial` by each number in the loop.
4. Print the final factorial.

### 💻 Code
```python
num = int(input("Enter a positive integer to calculate factorial: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print("The factorial of", num, "is", factorial)

🚀 Example Input / Output
Input: 5

Output:
The factorial of 5 is 120

---
---
*Fundamentals set. Ready for the next challenge.*⚡