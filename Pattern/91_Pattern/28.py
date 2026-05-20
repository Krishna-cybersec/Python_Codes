n = int(input("Enter number "))

str1 = ""
count = 1

for i in range(1,n+1):


	row = "".join(map(str,range(1,count+i)))
	count+=1
	print(row)




