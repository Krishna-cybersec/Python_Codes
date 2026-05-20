'''8_compound_interest.py

Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0

---
'''

principal = int(input("Principal ="))
rate = eval(input("Rate in % ="))
time = eval(input("Time in years = "))



amount = principal*(1+rate/100)**time

print(amount)