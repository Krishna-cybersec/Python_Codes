'''2_Mobile_EMI_Calculation.py

Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0

---
'''

mobile=int(input("Mobile price ="))
down= int(input("Down payment="))
interset = int(input("Interset rate % ="))
months = int(input("Months = "))

rem = mobile-down

twi=((rem*interset)/100)+rem

emi= twi/months

print("Remaining Amount =",rem)
print("Total with Interest ",twi)
print("emi= rem/months",emi)