'''
1_Restaurant_Bill_Split.py
Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75

---
'''

amount = int(input("Total bill amount:"))

gst = int(input("GST % = "))

Service= int(input("Service charge % = "))

friends= int(input("Number of friends ="))

total = ((amount*gst)/100 + (amount*Service)/100 + amount)

eachpay=total/friends

print("Final Bill = ",total)
print("Each Person Pays =" ,friends)
