'''2_Digit_Sum_Mirror.py
A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number
'''


n = input("Enter number")

first = 0
second = 0

for i in range(len(n)//2):
	
	first+=int(n[i])


for j in range(len(n)//2,len(n)):

	second += int(n[j])


if first == second:

	print("Balance")

else:

	print("Not Balance")



	




