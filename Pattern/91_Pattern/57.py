'''
     1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5

'''


n = int(input("Enter number "))

for i in range(1,n+1):

	print()
	print(" "*(n-i),end="")

	for j in range(1,i+1):

		print(str(j)+" ",end="")
			