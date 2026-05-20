num = int(input("Enter number "))
count = 1
for i in range(num+1,0,-1):

	row = "".join(map(str,range(count,i)))

	print(row)
