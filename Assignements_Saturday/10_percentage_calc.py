'''10_percentage_calc.py
Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
'''

total = int(input("Enter total marks : "))
obtain = int(input("Enter total marks obtained :"))

perc = (obtain*100)//total

print("Percentage = ", perc,"%")

