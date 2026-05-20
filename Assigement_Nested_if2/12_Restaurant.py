'''12_Restaurant.p
12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680

'''

amount = eval(input("Enter bill amount = "))

if amount <= 1000:
  amount += (amount*5)//100
  print("Final Bill Amount = ₹ ",amount)


elif amount > 1000 and amount < 5000:
  
  amount+= (amount*12)//100
  
  if amount >=3000:

    amount+=200
    print("Final Bill Amount = ₹",amount)

  else:

    print("Final Bill Amount = ₹",amount)


else:
  amount+=((amount*18)//100)+200
  print("Final Bill Amount = ₹",amount)

