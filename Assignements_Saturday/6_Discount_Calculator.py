'''6_Discount_Calculator.py
Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
'''

amount=eval(input("Enter the amount:"))
Discount=(amount//100)*10
total=amount-Discount

print("Discount =",Discount)
print("Final = ",total)

