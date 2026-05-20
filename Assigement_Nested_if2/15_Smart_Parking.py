'''15_Smart_Parking.py

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220
'''


vehicle = input("Enter vehicle type = ").lower()

parked = int(input("Enter hours parked = "))

if parked > 5:

  price = 100

else:
  price = 0

if vehicle == "bike":

  price+=10*parked
  print("Total Parking Fee: ₹",price)

elif vehicle == "car":

  price+=20*parked
  print("Total Parking Fee: ₹",price)
  

elif vehicle =="bus":
  price +=50*parked
  print("Total Parking Fee: ₹",price)
