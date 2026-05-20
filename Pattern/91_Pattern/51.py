'''
12345
 1__4
  1_3
   12
    1
'''

n = int(input("Enter number "))



for i in range(n,0,-1):

	print()
	print(" "*(n-i),end="")

	if i ==1 or i ==2 or i ==n:

		for j in range(1,i+1):

			print(j,end="")


	else:

		for j in range(1,i+1):

			if j == 1 or j==i:

				print(j,end="")

			else:
				print("_",end="")