'''
11111
 2222
  333
   44
    5
'''

n = int(input("Enter number "))

ch = 1


for i in range(n,0,-1):

	print()
	print(" "*(n-i),end="")


	for j in range(1,i+1):

		print(ch,end="")


	ch+=1

