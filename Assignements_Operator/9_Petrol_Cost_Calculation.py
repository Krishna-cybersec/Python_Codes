'''9_Petrol_Cost_Calculation.py
---

Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0

---
'''

distance = int(input("Distance in km = "))
mileage = int(input("mileage in km/litre = "))
petrol  = int(input("petrol price per litre = "))

petrol_used =  distance/mileage
cost =  (distance/mileage)*petrol

print("Petrol Used = ",petrol_used,"litres")
print("₹",cost)

