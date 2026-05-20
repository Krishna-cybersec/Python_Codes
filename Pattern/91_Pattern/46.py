'''
    1
   11
  1*1
 1**1
11111
'''


n = int(input("Enter number "))



for i in range(1,n+1):

	print()
	print(" "*(n-i),end="")

	if i == 1 or i ==2 or i ==n:

		for j in range(1,i+1):

			print("1",end="")


	else:


		for j in range(1,i+1):

			if j == 1  or j == i:

				print("1",end="")

			else:
				print("*",end="")






