'''
55555
 4444
  333
   22
    1
'''


n = int(input("Enter number "))

temp = n


for i in range(n,0,-1):

	print()
	print(" "*(n-i),end="")


	for j in range(1,i+1):

		print(temp,end="")

	temp-=1