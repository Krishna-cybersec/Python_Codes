Question_5.py

Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number

```python
num = int(input())

prev = num % 10
num //= 10

while num > 0:
    curr = num % 10
    if curr >= prev:
        print("Unstable Number")
        break
    prev = curr
    num //= 10
else:
    print("Stable Number")
```
