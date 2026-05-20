'''
ABCDE
A  D
A C
AB
A
'''

n = int(input("Enter a number "))

x = 65

for i in range(n,0,-1):

	print()
	for j in range(i):

		if j == 0  or i == n or j ==i-1:


			print(chr(x+j),end="")

		else:

			print(" ",end="")



