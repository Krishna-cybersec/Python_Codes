'''
5
44
333
2222
11111
'''


n = int(input("Enter number"))

temp = n
temp2 = 1

for i in range(1,n+1):

	print()
	print(" "*(temp-1),end="")

	
	for j in range(1,i+1):

		print(str(temp)*temp2,end="")

	temp-=1

temp2+=1



