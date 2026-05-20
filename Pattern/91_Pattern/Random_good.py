'''
    *
    * *
    * * *
    * * * *
    * * * * *
          *
          * *
          * * *
          * * * *
          * * * * *  

'''

n = int(input("Enter number "))


for i in range(1,n*2,2):
	print()

	print(" "*(n-1),end="")

	for j in range(1,i+1):

		if j%2==0:

			print(' ',end="")

		else:
			print("*",end="")


for i in range(1,n*2,2):
	print()

	print(" "*(n*2),end="")

	for j in range(1,i+1):

		if j%2==0:

			print(' ',end="")

		else:
			print("*",end="")

