'''4_E-commerce.py
4. E-Commerce Discount Engine


An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050
'''

purchase = int(input("Enter purchase amount:"))

if purchase > 5000:
	purchase = purchase-((purchase*20)//100)

	print("Final Amount" ,purchase)

elif purchase > 2000 and purchase < 5000:
	purchase -= (purchase*10)//100
	print("Final Amount" ,purchase)

elif purchase <= 2000:
	purchase-=(purchase*5)//100
	print("Final Amount ₹" ,purchase)

