'''15_Average_Speed.py
Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h
'''

dist1=int(input("Enter Distance 1 = "))
time1=int(input("Enter time 1 = "))
speed1=dist1//time1

dist2= int(input("Enter Distance2 = "))
time2=int(input("Enter time 2 ="))
speed2=dist2//time2

print("Average Speed = ",(speed1+speed2)//2)

