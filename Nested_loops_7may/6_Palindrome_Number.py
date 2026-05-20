'''6_Palindrome_Number.py

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191
'''

n = int(input("Enter the number = "))
m = int(input("Enter second number = "))

for i in range(n,m+1):

	temp = i
	count = 0 

	while  temp>0:

		rem = temp%10

		count = (count*10)+rem

		temp = temp//10



	if count == i:

		print(i)


	
