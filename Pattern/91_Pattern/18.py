n = int(input("Enter number "))

m = "1"
for i in range(1,n+1):
	print()
	if i %2 !=0:
		print(m,end="")
		m+="0"

	else:
		print(m,end="")
		m+="1"


