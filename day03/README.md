# Day 3 – Functions & Advanced List Logic 🔢

**Author:** Sree Harsha Reddy  

Welcome to Day 3 of my Python development journey!  
This day focused on mastering functions, advanced list operations, and solving K-th element problems using structured logic.

---

## 📁 Repository Contents

This folder contains 10 structured problems:

1. problem1_sum_function.py  
2. problem2_reverse_a_string.py  
3. problem3_factorial.py  
4. problem4_max_number.py  
5. problem5_second_smallest.py  
6. problem6_second_largest.py   
7. problem7_third_ls(dup allowed).py  
8. problem8_thirdLS(distinct).py  
9. problem9_kthsmall&kthlarge(dup allowed).py  
10. problem10_kthsmall&large(distinct).py  

---

## 📚 Topics Covered

### 🔹 1. Functions (Core Focus)
- Created reusable functions
- Practiced:
  - sum of list
  - reverse string
  - factorial
  - max number
- Learned input handling inside functions

---

### 🔹 2. Second Smallest & Largest
- Implemented using loops (no sorting)
- Used single-pass logic
- Introduced shifting concept

---

### 🔹 3. Third Smallest & Largest (Duplicates Allowed)
- Extended logic to 3 variables
- Allowed equal values
- Used relaxed comparisons (`<=`)

---

### 🔹 4. Third Smallest & Largest (Distinct)
- Ignored duplicates
- Used strict comparisons (`<`)
- Ensured unique ranking

---

### 🔹 5. Edge Case Handling
- Cases handled:
  - less than required elements
  - all values same
- Used:
  - `float('inf')`
  - `-float('inf')`

---

### 🔹 6. K-th Smallest & Largest (With Duplicates)
- Used sorting approach
- Index logic:
  - smallest → `k-1`
  - largest → `len(a) - k`
- Handled input validation

---

### 🔹 7. K-th Smallest & Largest (Distinct)
- Removed duplicates manually using loops
- Created new list for unique values
- Applied same K-th logic

---

## 🧠 Key Concepts Learned

- Function creation and usage
- Single-pass list processing
- Multi-variable tracking (min/max)
- Duplicate vs distinct handling
- Sorting and indexing logic
- Clean program structure
- Input validation

---

## ⚠️ Common Mistakes Fixed

- Misusing `.sort()`:
  ```python
  a = a.sort() ❌