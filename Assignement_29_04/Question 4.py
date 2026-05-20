Question 4.py

Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code

```python
num = int(input())

temp = num

while temp > 0:
    digit = temp % 10
    count = 0
    check = num

    while check > 0:
        if check % 10 == digit:
            count += 1
        check //= 10

    if count > 1:
        print("Invalid Code")
        break

    temp //= 10
else:
    print("Valid Unique Code")
```