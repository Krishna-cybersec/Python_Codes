'''2_Employee_Salary.py

Scenario:
You are developing an Employee Salary Processing System for a company’s HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

- Salary > 50000 → 10% tax
- Otherwise → 5% tax
5 → Display Salary Slip
6 → Exit
'''

sal = 0
while True:

	print("1 → Enter Basic Salary")
	print("2 → Calculate HRA (20%) and DA (10%)")
	print("3 → Calculate Net Salary")
	print("4 → Tax Deduction")
	print("5 → Display Salary Slip")
	print("6 → Exit")
	print()

	choice = int(input("Enter the choice = "))


	match choice:

		case 1:
			sal = int(input("Enter Basic sal = "))
			print("Recorded successfully")

		case 2 if sal == 0 :
			print("please enter basic entry first")

		case 3 if sal == 0 :
			print("please enter basic entry first")

		case 4 if sal == 0 :
			print("please enter basic entry first")

		case 5 if sal == 0 :
			print("please enter basic entry first")
		


		case 2:

			hra = (20*sal)//100
			da = (10*sal)//100

			print(hra,"\n",da)

		case 3:

			hra = (20*sal)//100
			da = (10*sal)//100


			net = sal+hra
			print("sal ",net)

		case 4:

			hra = (20*sal)//100
			da = (10*sal)//100

			net = sal+hra+da
			print("sal ",net)

			if net > 50000:
				tax = (net*10)//100

			else:
				tax = (net*5)//100


		case 5 :

			hra = (20*sal)//100
			da = (10*sal)//100


			net = sal+hra+da
			
			if net > 50000:
				tax = (net*10)//100

			else:
				tax = (net*5)//100


			print("\n===== Salary Slip =====")
			print("Basic Salary :", sal)
			print("HRA          :", hra)
			print("DA           :", da)
			print("Net Salary   :", net)
			print("Tax Deduction:", tax)
		
		case 6:
			print("exiting")
			break

		case _:

			print("invalid")


