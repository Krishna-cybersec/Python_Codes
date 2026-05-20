#8_Simple_Interest.py
'''========================================
Assignment 8: Simple Interest Calculator
========================================

A bank wants to help customers calculate the simple interest on their savings.

Write a Python program that:
- Accepts principal amount, rate of interest, and time (in years) as input.
- Calculates the simple interest using the formula:
  SI = (P × R × T) / 100
- Displays the simple interest.

Example:
Principal = 1000
Rate = 5
Time = 2
Simple Interest = 100.0
'''

amount,roi,time= map(eval,input("Enter the Principal,rate,time:").split())

si = (amount*roi*time)/100

print(f"Principal = {amount} Rate ={roi}  Time={time} Simple Interest = {si}")
