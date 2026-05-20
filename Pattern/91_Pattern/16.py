n = int(input("Enter method "))

num  = 1

for i in range(1,n+1)	:
	print()
	for j in range(i):

		print(chr(96+num),end="")
		num +=1