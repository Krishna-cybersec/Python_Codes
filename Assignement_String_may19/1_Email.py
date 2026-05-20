'''
1_Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123
Output:
Valid Username
'''

user = input("Enter username ").lower()

digit = 0
underscore = 0


if len(user)>=5 and len(user)<=12:



	if user[0]>="a" and user[0]<="z":

		for i in user:

			if i ==" ":

				print("Invalid")

			else:

				if i >  '0' and i< '9':

					digit =1

				elif i == "_":

					underscore =1


	if digit  == 1 and underscore == 1:

		print("Valid")

	else:
		print("Invalid")

else:

	print("Invalid")

