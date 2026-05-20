Question 3.py

Perfect Number Reward System

A gaming company rewards users if entered number is a Perfect Number.

(Perfect Number = sum of proper factors equals number)

Write a program using for-else loop to:

- Find sum of proper factors
- If sum equals number print Reward Unlocked
- Else print Try Again

Input:
6

Output:
Reward Unlocked

```python
num = int(input())

sum_factors = 0

for i in range(1, num):
    if num % i == 0:
        sum_factors += i

if sum_factors == num:
    print("Reward Unlocked")
else:
    print("Try Again")
```