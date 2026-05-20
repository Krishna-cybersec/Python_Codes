'''4_Travel_Distance_Calculation.py

Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km

---
'''


speed = int(input("Speed in km/hr:"))
hr,min = map(int,input("Time =").split(" "))

time = ((hr*60)+30)/60

distance = speed*time

print("Total Time =",time,"hours")

print("distance = ",distance,"km") 

