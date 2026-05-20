'''8_Largest_Smallest_Prime.py

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
'''
import math

n = int(input("Enter number = "))

largest = 0

smallest = 9

for i  in  str(n):

	i = int(i)
	if i > largest:

		largest = i


	if i < smallest:

		smallest = i


sum = largest + smallest

print(sum)
print(largest)
print(smallest)


prime = "prime number"

if sum <=1:
	prime = "Not prime nor composite "


else:

	for i in range(2,int(math.sqrt(sum))):

		if sum%i==0:
			prime = "composite number "
			break


print(prime)






	



