Question_9.py

Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number

```python
num = int(input())

sum_factors = 0

for i in range(1, num):
    if num % i == 0:
        sum_factors += i

if sum_factors > num:
    print("Abundant Number")
else:
    print("Not an Abundant Number")
```