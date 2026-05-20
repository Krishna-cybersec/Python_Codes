'''Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern
'''

n = input("Enter the number = ")

y = ""

count = 0

max1 = 0

uni = "uniform"

for  i in range(len(n)-1):
	
	x = abs(int(n[i])-int(n[i+1]))

	print(x,end=" ")
	y += str(x)


	count += 1 if x % 2 == 0 else 0

	if x > max1:
		max1 = x




for z in range(len(y)-1):

	if y[z] != y[z+1]:
		uni = "non uniform"



print("\n")
print(count)
print(max1)
print(uni)