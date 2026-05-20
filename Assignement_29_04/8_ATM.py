8_ATM.py

A bank ATM dispenses ₹100 notes.

Write a program to:

- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Input:
700

Output:
Notes = 7

```python
amount = int(input())

count = 0

while amount >= 100:
    amount -= 100
    count += 1

print("Notes =", count)
```