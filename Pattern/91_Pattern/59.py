'''
    *
   *_*
  *___*
 *_____*
*********
'''



n = int(input("Enter number "))

stars = 1

for i in range(1,n+1):
	print()
	print(" "*(n-i),end="")




	for j in range(1,stars+1):

		if j == 1 or  j ==stars or i ==n:

			print("*",end="")

		else:
			print("_",end="")
	
	stars+=2
