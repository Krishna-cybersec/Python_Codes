Question_6.py

Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29

```python
num = int(input())

n = num + 1

while True:
    if n < 2:
        n += 1
        continue

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        print("Next Prime Cabin =", n)
        break

    n += 1
```
