'''1_Largest_Digit.py
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9
'''


n = int(input("Enter the number "))

s = 0

while n>0 :
	
	rem = n%10
	#print(rem)

	if 	rem > s:

		s = rem

	n = n//10

print(s)