'''10_Time_Conversion.py
---

Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4

---
'''

Seconds = int(input("Total event duration in seconds:"))
hour=Seconds//3600
Min= (Seconds%3600)//60
Sec= (Seconds%3600)%60


print("Hours   = ",hour)
print("Minutes = ",Min)
print("Second  = ",Sec)

