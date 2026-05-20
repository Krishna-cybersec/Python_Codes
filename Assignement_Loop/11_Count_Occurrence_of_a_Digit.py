'''11_Count_Occurrence_of_a_Digit.py
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to **count how many times a given digit appears in a number using loops**.

Input: Number = 122312, Digit = 2
Output: 3

'''


n = int(input("Enter number = "))

d = int(input("Enter digit = "))

count = 0

while n >0:
	rem = n%10

	if rem == d:

		count+=1

	n=n//10


print(count)
