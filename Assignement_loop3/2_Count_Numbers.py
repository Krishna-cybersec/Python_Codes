'''2_Count_Numbers.py

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4
'''


n,m = map(int,input("Enter range = ").split())

count = 0

for i in range(n,m+1):

	if i %7 ==0:

		count+=1


print("count =",count)




