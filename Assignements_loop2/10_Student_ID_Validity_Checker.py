'''10_Student_ID_Validity_Checker.py
A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.

Write a program to count the number of odd digits in a given student ID using loops.

Input:
572943

Output:
Odd Digits Count = 4
'''

num = int(input("Enter number "))

count = 0

while num > 0:

	rem = num%10

	if rem % 2 !=0:
		count+=1

	num = num//10


print("Odd Digits Count = ",count)