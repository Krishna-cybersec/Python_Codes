'''8_Count_Multiples_of_5.py 
A supermarket gives coupons to customers whose token numbers are multiples of 5. The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.

Input:
1 20

Output:
Count = 4
'''



n,m = map(int,input("Enter two number: ").split(" "))

count =0

for i in range(n,m+1):

	if i %5 ==0:

		count +=1

print(count)


