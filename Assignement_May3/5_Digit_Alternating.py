'''5_Digit_Alternating.py

A coding system calculates alternating sum of digits (add, subtract, add...).

Write a program to:

Traverse digits from left to right
Add first digit, subtract second, add third, and so on
Display final alternating sum
If result is positive → print Positive Pattern
Else → print Negative Pattern

Input:
1234

Output:
Result = -2
Negative Pattern

Input:
8642

Output:
Result = 8
Positive Pattern
'''

n = input("Enter number ")
a = 0 
b = 0

for i in range(len(n)):


	if i % 2 == 0:

		b = b + int(n[i])

	else:

		a+= int(n[i])




print("Result = ",b-a)

if (b-a) < 0:

	print("Negative Pattern")

else:

	print("Positive Pattern")


