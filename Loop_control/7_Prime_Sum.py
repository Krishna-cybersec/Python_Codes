'''7_Prime_Sum.py
A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number

'''
import math
n = int(input("Enter number"))

sum = 0

for i in str(n):
	sum += int(i)


print("Sum = ",sum)




prime = "lucky "

if sum <=1:
	prime = "rarest"


else:

	for i in range(2,int(math.sqrt(sum))):

		if sum%i==0:
			prime = "not so lucky"
			break


print(prime)








