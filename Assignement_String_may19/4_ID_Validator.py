'''
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
'''

n = input("Enter ID ")

validity = "Invalid"

if len(n) ==8:

	if n[0:3] =="EMP":


		for i in n[3:9]:

			if i >='0' and i<='9':

				validity = "Valid Employee ID"

print(validity)