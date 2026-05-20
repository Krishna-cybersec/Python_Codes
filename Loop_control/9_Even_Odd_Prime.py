'''9_Even_Odd_Prime.py

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime

'''

import math

n = int(input("Enter number = "))

even = 0
odd = 0
for i in str(n):

	i = int(i)

	if i %2 ==0:

		even +=1

	else:
		odd +=1


diff = abs(even - odd)



prime = "prime number"

if diff <=1:
	prime = "Not prime nor composite "


else:

	for i in range(2,int(math.sqrt(diff))):

		if diff%i==0:
			prime = "composite number "
			break


print(odd)
print(even)
print("diff",diff)
print(prime)




