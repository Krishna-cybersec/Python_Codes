'''3_Digit.py

A system analyzes the relationship between a digit and its immediate neighbors.

Write a program to:

Traverse digits from left to right (ignore first and last digit)
For each digit, calculate sum of its adjacent digits
Check if current digit is equal to the sum of its neighbors
Display such digits
Count how many such digits exist
If none found → print No Matching Digit
Else → print Neighbor Sum Pattern Found

Input:
 121324

Output:
Matching Digits: 2 3
Count = 2
Neighbor Sum Pattern Found
'''


n = input("Enter number = ")

y = ""

count = 0
for i in range(len(n)-1):

	if i == 0:
		continue


	elif  int(n[i]) == int(n[i-1])+int(n[i+1]):
		
		y+=n[i]+" "
		count+=1

print(y)
print(count)
print("Neighbor Sum Pattern Found") if y !=" " else print("No Matching Digit")


	







