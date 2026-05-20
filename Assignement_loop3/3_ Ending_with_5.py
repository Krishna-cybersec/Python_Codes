'''3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35

'''



n,m = map(int,input("Enter range = ").split())


for i in range(n+1,m):

	if i %5 ==0 and i%10!=0:

		print(i , end = " ")






