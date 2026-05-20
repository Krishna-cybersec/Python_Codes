'''
6_Smart_Coin.py
========================================
Assignment 6: Smart Coin Machine
========================================

You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).

Write a Python program that:
- Accepts the total amount.
- Calculates how many ₹10 coins and ₹5 coins will be dispensed.
- Displays the result.

Example:
Amount = ₹35
Output = ₹10 x 3, ₹5 x 1
'''

amount=int(input("Enter the amount:"))

output= amount//10 
output2 =(amount %10 )//5

print("Output = ₹10 x {}, ₹5 x {}".format(output,output2))
print("Amount = ₹",amount)