'''
* * * * *
 * * * *
  * * *
   * *
    *
'''

n = int(input("Enter number "))

for i in range(n,0,-1):

	print()
	print(" "*(n-i),end="")

	for j in range(i,0,-1):

		print("* ",end="")