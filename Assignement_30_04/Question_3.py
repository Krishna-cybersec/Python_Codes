Question_3.py
Fibonacci Population Growth Tracker

A wildlife research team is studying the growth of a rare species.

They observe that the population follows a Fibonacci pattern:

- Month 1 → 0 animals
- Month 2 → 1 animal
- Every next month → sum of previous two months

The researchers want to analyze the growth pattern.

Write a program to:

- Read number of months n
- Generate Fibonacci series up to n months using loop
- Print population for each month
- Find total population observed
- Count how many months population exceeded 5

Input:
8

Output:
Population Growth:
0 1 1 2 3 5 8 13

Total Population = 33
Months with Population > 5 = 2

```python
n = int(input())

a, b = 0, 1
total = 0
count = 0

print("Population Growth:")

for i in range(n):
    print(a, end=" ")
    total += a
    if a > 5:
        count += 1
    a, b = b, a + b

print("\nTotal Population =", total)
print("Months with Population > 5 =", count)
```
