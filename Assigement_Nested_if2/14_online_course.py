'''14_online_course.py
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000
'''
course = input("Enter course category: ").lower()
user = input("Enter user type: ").lower()

if course == "programming":
  price = 5000

elif course == "design":
  price = 4000

elif course == "marketing":
  price = 3000


if user == "student":
  price-=(price*20)//100
  print("Final Course Fee:₹",price)

elif user == "professional":
  price -=(price*10)//100
  print("Final Course Fee:₹",price)

else:
  print("No discount")
  
