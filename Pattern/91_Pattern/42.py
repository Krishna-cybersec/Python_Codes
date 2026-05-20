'''
54321
5432
543
54
5
'''

n = int(input("Enter number "))

temp = n
j = 1

for i in range(n,0,-1):

	print()
	for j in range(temp,j-1,-1):

		print(j,end="")

		j+=1




