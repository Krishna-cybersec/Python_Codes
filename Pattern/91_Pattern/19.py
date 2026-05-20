n = int(input("Enter number = "))

star = "*"
space = 1
for i in range(1,n+1):
	print()
	if i == 1:
		print(star,end="")

	elif i == n:
		print(star*(n-1)*2,end="")

	else:

		print(star+" "*space+star,end="")
		space +=2


