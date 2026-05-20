'''5_Banking_Security.py 
5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password
'''

user =  input("Enter username:")
Pass = input("Enter password:")

if user == "admin":
   print("Enter username: admin")

if len(Pass) >=8:
   print("Strong password")

