Question_7.py
Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime

```python
num = int(input())

sum_alt = 0
pos = 1

while num > 0:
    digit = num % 10
    if pos % 2 == 1:
        sum_alt += digit
    num //= 10
    pos += 1

print("Alternate Sum =", sum_alt)

if sum_alt < 2:
    print("Not Prime")
else:
    for i in range(2, int(sum_alt**0.5) + 1):
        if sum_alt % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
```