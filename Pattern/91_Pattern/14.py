n = int(input("enter n "))

x = 1

''' By nested loops
for i in range(n):
	temp = ""


	print()

	for j in range(i+1):

		print(temp+str(x),end="")
		x+=1

'''

for i in range(1,n+1):

	print()
	row = "".join(map(str,range(x,i+x)))
	print(row,end="")
	x+=i
	






