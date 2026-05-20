'''5_Tech_Number_Checker.py

A number is called a Tech Number if:

It has even number of digits
Split it into two equal halves
Add both halves
Square the sum
If result equals original number → Tech Number

Write a program to:

Count digits
If digits are even, split the number
Find sum of both halves
Square the sum
Display intermediate values
Check and print result

Input:
2025

Output:
First Half = 20
Second Half = 25
Sum = 45
Square = 2025
Tech Number
'''

n = input("Enter number = ")

first  = ""
second = ""

if len(n)%2==0:

	for i in range(len(n)//2):

		first+=n[i]

	for j in range(len(n)//2,len(n)):

		second+=n[j]

	print(first)
	print(second)
	sum1 = int(first)+int(second)
	print(sum1)
	print("sq",sum1**2)

	if sum1**2 ==int(n):

		print("tech number")

	else:
		print("Not a tech number")

else:
	print("length of Number ain't even")




