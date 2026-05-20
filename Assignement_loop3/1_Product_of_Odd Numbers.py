'''1_Product_of_Odd Numbers.py

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15
'''

n = eval(input("Enter number = "))

count = 1

for i in range(1,n+1):

	if i%2 !=0:

		count*=i



print(count)






