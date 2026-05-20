'''1_speed_calc.py
Assignment 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
----------------------------------------
'''
dist=eval(input("Enter the distance:"))
time=eval(input("Enter the time taken:"))

speed=dist/time
print(f"Speed = f{speed} km/h")