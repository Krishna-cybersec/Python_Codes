'''13_Employee_performance.py
13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600

'''

sal = int(input("Enter salary = "))
rate = int(input("Enter rating = "))

if rate == 1:

  print("No hike")

elif rate == 2:

  sal+= (sal*5)//100
  print("Revised Salary: ₹",sal)

elif rate == 3:
  sal+= (sal*10)//100
  print("Revised Salary: ₹",sal)

elif rate ==4:

  if sal < 20000:
    sal+= ((sal *20)//100)+2000

    print("Revised Salary: ₹",sal)

  else:
    sal+= (sal *20)//100
    print("Revised Salary: ₹",sal)

elif rate ==5:

  if sal < 20000:
    sal+=((sal *25)//100)+2000
    print("Revised Salary: ₹",sal)

  else:
    sal+=(sal *25)//100
    print("Revised Salary: ₹",sal)
