'''1_Prime_Security.py

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number
'''

import math

n = int(input("Enter number = "))

prime = "prime number"

if n <=1:
	prime = "Not prime nor composite "


else:

	for i in range(2,int(math.sqrt(n))):

		if n%i==0:
			prime = "composite number "
			break


print(prime)




