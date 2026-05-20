'''4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''


import math

n = int(input("Enter number = "))# 14

temp = n

i = 2 

while i <= int(math.sqrt(n)): #2 <= 3



	if  n % i == 0:  

		n-=1  

		i = 2

		continue



	i+=1






if temp == n:

	n+=1

	i = 2 

	while i <= int(math.sqrt(n)): #2 <= 3


		if  n % i == 0:  

			n+=1  

			i = 2

			continue

		i+=1


	print(n)

else:

	print(n)






