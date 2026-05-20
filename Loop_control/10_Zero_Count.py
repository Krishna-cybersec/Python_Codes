'''10_Zero_Count.py

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime


'''

import math 

n = int(input("Enter number = "))

smallest = 9

zero_c = 0

sum = 0


for i  in  str(n):

	i = int(i)

	sum +=i

	if i == 0:
		zero_c +=1


	if i < smallest:

		smallest = i


print(sum)
print(zero_c)
print(smallest)
total = (sum+zero_c)*smallest

print(total)



prime = "prime number"

if total <=1:
	prime = "Not prime nor composite "


else:

	for i in range(2,int(math.sqrt(total))):

		if total%i==0:
			prime = "composite number "
			break


print(prime)

