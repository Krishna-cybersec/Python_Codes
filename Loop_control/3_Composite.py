'''3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number
'''

import math

n = int(input("Enter number = "))

prime = "prime number"

if n <=1:
	prime = "Not prime nor composite "


else:

	for i in range(2,int(math.sqrt(n))+1):

		if n%i==0:
			prime = "composite number "
			break


print(prime)


