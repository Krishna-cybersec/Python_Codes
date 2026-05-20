'''

    #
   *#*
  **#**
 ***#***
****#****

'''


n = int(input("Enter n "))


for i in range(1,n+1):

	print()
	print(" "*(n-i),end="")
	for j in range(1,i+1):

		if j == i:

			print("#"+"*"*(i-1),end="")

		else:
			print("*",end="")
