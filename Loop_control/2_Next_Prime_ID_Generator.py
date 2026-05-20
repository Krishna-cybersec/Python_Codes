'''2_Next_Prime_ID_Generator.py

A multinational company auto-generates employee IDs in numeric sequence.
Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17
'''

import math

n = int(input("Enter number = "))# 14

n+=1

prime = "prime"

i = 2 

while i <= int(math.sqrt(n)): #2 <= 3


	if  n % i == 0:  

		n+=1  

		i = 2

		prime = "Not a prime"

		continue

	i+=1


print(n)








		




