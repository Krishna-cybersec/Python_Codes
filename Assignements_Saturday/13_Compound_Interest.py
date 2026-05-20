'''13_Compound_Interest.py
Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0
'''
#ci = (p((100+r)/100)**n) -p

prin = int(input("Principal = "))
rate = int(input("Rate = "))
time = int(input("Time = "))

ci = (prin*(1+rate/100)**time)-prin
print(round(ci,2))