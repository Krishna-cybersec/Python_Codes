'''9_Fuel_cost.py
Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
'''

distance = int(input("Distance = "))
mileage = int(input("mileage = "))
petrol = int(input("petrol price = "))


cost = (distance //mileage)*petrol

print("Cost = ",cost)