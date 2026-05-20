'''11_Time_duration.py
Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
'''

hour=int(input("Hour = "))
minutes=int(input("Minutes = "))
seconds=int(input("seconds = "))

print("Total Seconds",hour*3600+minutes*60+seconds)