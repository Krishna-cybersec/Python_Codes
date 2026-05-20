'''
     *
    *_*
   *___*
  *_____*
   *___*
    *_* 
     *

'''




n = int(input("Enter number "))

c = 1

for i in range(1,n*2,2):

	print()
	print(" "*(n-c),end="")

	for j in range(i):

		if j ==i-1 or j ==0:

			print("*",end="")

		else:
			print("_",end="")

	c+=1


c = n

for x in range((n*2)-1,0,-2):

	print()
	print(" "*(n-c),end="")

	for j in range(x):

		if j == x-1 or j==0:
			print("*",end="")

		else:
			print("_",end="")

	c-=1


	