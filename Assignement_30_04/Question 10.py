Question 10.py

Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:
        
        First 100 units      → ₹5 per unit
        
        Next 100 units      → ₹7 per unit
        
        Above 200 units     → ₹10 per unit
        
    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge
        - If units < 50 → give ₹100 subsidy
    - Print bill for each house
- After processing all houses:
    - Print total bill collected
    - Print highest bill

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700

```python
n = int(input())

total = 0
highest = 0

for i in range(1, n + 1):
    units = int(input())

    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    if bill > 2000:
        bill += bill * 0.10

    if units < 50:
        bill -= 100

    print(f"House {i} Bill = {int(bill)}")

    total += bill

    if bill > highest:
        highest = bill

print("Total Collection =", int(total))
print("Highest Bill =", int(highest))
```

https://pythononline.net/