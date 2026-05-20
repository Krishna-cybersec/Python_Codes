n = int(input("Enter n "))

str1 =""

for i in range(1,n+1):

	if i == 1 or i ==2 or i ==n:

		str1+="*"

		print(str1)

	else:

		str1+="*"
		print(str1[0]+"@"*(i-2)+str1[i-1])

