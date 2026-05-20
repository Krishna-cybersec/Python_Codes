'''4_Armstrong_Number.py

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407
'''

n = int(input("Enter starting Number = "))
m = int(input("Enter ending number = "))

for i in range(n,m+1):

	temp = i 

	count = 0

	while  temp>0:

		rem = temp%10
		count += rem**len(str(i))
		temp = temp//10

	if count == i:
		print(i)
		
