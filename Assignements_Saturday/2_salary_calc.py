'''2_salary_calc.py
----------------------------------------
Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000
----------------------------------------------
'''

wage=int(input("Enter the daily wage ="))
days=int(input("Enter the number of days worked ="))

salary=wage*days
print("Salary = {}".format(salary))
