'''
3_Split_Bill.py
========================================
Assignment 3: Split the Bill
========================================

You and your friends went out to eat. The bill was quite high and you want to split it evenly.

Write a Python program that:
- Accepts the total bill amount.
- Accepts the number of friends.
- Displays how much each person should pay.

Example:
Total bill = 1250
Friends = 5
Each should pay = 250.0

'''

bill=float(input("Enter the total bill amount:"))
friends=int(input("Enter number of friends"))
print("\n")
print("Total bill = ",bill)
print("Friends=",friends)
print("Each should pay =",round(bill/friends))
