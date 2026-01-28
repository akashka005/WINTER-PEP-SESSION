# 🧠 WITER PEP – Day 1 (Python Practice)

This repository contains Python practice programs written during the WITER PEP Session – Day 1.
The focus is on strengthening basic programming concepts, functions, recursion, string manipulation, and file handling.

## 📌 Topics Covered

- Fibonacci Series (Iteration & Recursion)
- String Manipulation
- Split & Join Methods
- File Handling
- Case Conversion

## 🧮 1. Fibonacci Series

### 🔹 Problem Statement

- Take a number as input
- Print the first 5 numbers of the Fibonacci series
- Implement using:
  - Iteration
  - Recursion

### 🔹 Iterative Approach

```python
def fib_s(n):
    if n <= 0:
        return
    else:
        a, b = 0, 1
        count = 0
        while count < 5:
            print(a, end=' ')
            a, b = b, a + b
            count += 1

num = int(input("Enter a number: "))
fib_s(num)
```

**Concepts Used:**
- Functions
- While loop
- Conditional statements

### 🔹 Recursive Approach

```python
def fib_sr(n, a=0, b=1, c=0):
    if c == n:
        return
    print(a, end=' ')
    fib_sr(n, b, a + b, c + 1)

num = int(input("Enter a number: "))
if num > 0:
    fib_sr(num)
else:
    print("Enter a positive number")
```

**Concepts Used:**
- Recursion
- Function parameters
- Base condition

## 🔁 2. Replace Spaces with Hyphens (-)

### 🔹 Problem Statement

- Replace all spaces in a string with `-`
- Ensure:
  - No multiple `-` appear
  - Newlines are handled correctly
  - Works with multi-line text files

### 🔹 Using split(" ") and join()

```python
def replace(a):
    b = a.split(" ")
    c = "-".join(b)
    return c

string = input("Enter a string: ")
print(replace(string))
```

> ⚠️ **Note:** This may create multiple hyphens if there are extra spaces.

### ✅ Improved Version (Recommended)

```python
def replace2(a):
    parts = a.split()
    return "-".join(parts)

filename = "test_input.txt"

with open(filename, 'r') as file:
    content = file.read()

result = replace2(content)
print("Processed text:")
print(result)
```

**Why this works better:**
- `split()` handles:
  - Multiple spaces
  - Tabs
  - Newlines
- Produces clean output

### 📝 Sample Input File (test_input.txt)

```
hello user 0000.
this is line 1.
this is line 2.
  this is line 3.
```

## 🔠 3. Swap Case of a String

### 🔹 Problem Statement

- Take a string as input
- Convert:
  - Uppercase → Lowercase
  - Lowercase → Uppercase

### 🔹 Manual Implementation

```python
def swap(n):
    result = ""
    for char in n:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result

inp = input("Enter a string: ")
print(swap(inp))
```

**Concepts Used:**
- String traversal
- Character methods (`isupper()`, `islower()`)

### 🔹 Built-in Method (Simpler)

```python
a = input("Enter the input: ")
print(a.swapcase())
```

✅ **Preferred** for clean and efficient code.

## 🛠️ Requirements

- Python 3.x
- Any code editor (VS Code recommended)

## 🎯 Learning Outcomes

- Understand recursion vs iteration
- Learn effective string handling
- Handle files with multi-line content
- Write clean and optimized Python code

## 📅 Session Info

| Attribute | Value |
|-----------|-------|
| Program   | WITER PEP |
| Day       | 1 |
| Language  | Python |