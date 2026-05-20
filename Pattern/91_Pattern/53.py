'''
ABCDE
 A__D
  A_C
   AB
    A
'''


n = int(input("Enter number "))

ch = 64


for i in range(n,0,-1):

	print()
	print(" "*(n-i),end="")

	if i ==1 or i ==2 or i ==n:

		for j in range(1,i+1):

			print(chr(ch+j),end="")


	else:

		for j in range(1,i+1):

			if j == 1 or j==i:

				print(chr(ch+j),end="")

			else:
				print("_",end="")