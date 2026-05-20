'''5Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password


'''


n = input("Enter password ")

digit = 0




if len(n)> 8 and len(n)<15 and n[0] >='A' and  n[0]<='Z' and n[len(n)-1] >='0' and n[len(n)-1]<='9':


	for i in n:
		print("Valid")


	

