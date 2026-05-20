'''6_Data_Storage_Conversion.py
---

Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0

---
'''
data=int(input("Data = "))

mb = data*1024
kb = mb *1024

print("In MB = ",mb)
print("In KB =",kb)