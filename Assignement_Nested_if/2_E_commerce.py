'''2_E_commerce.py
2. An e-commerce website provides discounts based on the cart value and user type. 
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000, 
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise, 
no discount is applied. Display the final payable amount.

Input:
Cart Value = 6000
User Type = Premium

Output:
Final Amount = 4800

'''

cart = int(input("Cart Value = "))
u_type = input("User Type = ").lower()


if cart >=5000:

	if u_type =="premium":

		cart -= (20*cart)//100
		print("Final Amount =" ,cart)

	else:

		cart -= (10*cart)//100
		print("Final Amount =" ,cart)

else:

	if cart>=2000:
		cart -= (5*cart)//100
		print("Final Amount =" ,cart)

	else:
		print("No discount")
		print("Final Amount =",cart)


