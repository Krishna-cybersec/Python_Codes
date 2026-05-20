'''6_sum_factors.py
6. Sum of Factors
A puzzle-based game rewards users based on the sum of all factors of a chosen number. The system calculates the total score using all factors of the entered number.
Write a program to find sum of factors using loops.

Input:
6

Output:
Sum = 12
'''


number = int(input("Enter number "))

count = number

for i in range(1,number//2+1):

	
	if number % i == 0:

		count+=i


print(count)