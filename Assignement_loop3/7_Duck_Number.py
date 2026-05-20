'''7_Duck_Number.py

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number
'''

n = int(input("Enter number "))

zero = n//10**(len(str(n))-1)


duck = "not a duck number"


if zero == 0:
	print(duck)



else:

	for i in str(n):

		if int(i) ==0:

			duck = "Duck number"
			break


	print(duck)

			



		



