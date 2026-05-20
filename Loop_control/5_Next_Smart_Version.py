'''5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
'''


import math

n = int(input("Enter number = "))# 14

temp = n
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


print("Next Prime ID",n)
print("Gap",n-temp)
