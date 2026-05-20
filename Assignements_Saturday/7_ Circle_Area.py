'''7_circle_area.py
----------------------------------------------------------------
Assignment 7: Circle Area Calculator

Write a Python program that:

Accepts radius.
Calculates area of circle.

Input:
Radius = 7

Output:
Area = 153.86
------------------------------------------------------------------------
'''

radius=eval(input("Enter radius of a circle:"))

area = round(3.14*(radius**2),2)

print(area)