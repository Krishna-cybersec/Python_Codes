'''4_Digit_Gap.py

A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number
'''

n = input("Enter number = ")

count =0

num = "smooth"

max1 = 0

for i in range(len(n)-1):

	diff = abs(int(n[i])-int(n[i+1]))

	if diff >max1:

		max1 = diff

	print(diff,end=" ")

	if diff>2:
		count+=1
		num = "Irregular"

print("\n")

print("count",count)
print("max diff",max1)
print(num)

