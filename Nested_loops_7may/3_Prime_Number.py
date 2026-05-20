'''3_Prime_Number.py

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47
'''

n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))

for i in range(n,m):

	count = 0
	for j in range(1,i):

		if i%j==0:
			count +=i


	if count == i:
		print(i)
