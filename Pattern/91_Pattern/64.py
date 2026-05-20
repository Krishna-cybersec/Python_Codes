'''
*********
 *******
  *****
   *** 
    *
'''


n = int(input("Enter n "))

for i in range(n,0,-1):

	print()
	print(" "*(n-i),end="")


	for j in range(i*2,1,-1):

		print("*",end="")
