'''
12345
 1234
  123
   12
    1
'''

n = int(input("Enter number "))



for i in range(n,0,-1):

	print()
	print(" "*(n-i),end="")


	for j in range(1,i+1):

		print(j,end="")