'''
*****
####
***
##
*
'''


n = int(input("Enter a number "))


for i in range(n,0,-1):

	print()
	for j in range(i):

		if j == 0  or i == n or j ==i-1:


			print("*",end="")

		else:

			print(" ",end="")
