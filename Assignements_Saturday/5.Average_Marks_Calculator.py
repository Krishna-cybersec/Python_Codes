'''5.Average_Marks_Calculator.py
------------------------------------------------
Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
-------------------------------------------------
'''

marks1,marks2,marks3= map(int,input("Enter marks of all 3 subjects :" ).split(","))

avg = (marks1+marks2+marks3/3)

print("Average:",avg)