Question_8.py

Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number

```python
n = int(input("Enter number: "))

cube = n * n * n
temp = n

flag = True

while temp > 0:
    if temp % 10 != cube % 10:
        flag = False
        break
    temp //= 10
    cube //= 10

if flag:
    print("Trimorphic Number")
else:
    print("Not Trimorphic Number")
```