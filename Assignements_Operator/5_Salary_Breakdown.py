'''5_Salary_Breakdown.py
---

Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5

---
'''

month=int(input("Monthly salary = "))
days=int(input("Working days="))
hour=int(input("Working hours per day ="))

salary_p_d=month/days
salary_p_h=salary_p_d/hour

print("Salary per day =",salary_p_d)
print("Salary per hour = ",salary_p_h	)