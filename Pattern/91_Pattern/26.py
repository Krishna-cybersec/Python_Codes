n = int(input("Enter number "))

str1="*"

for i in range(1,n+1):

	if i %2 !=0:

		print(str1)
		str1+="#"


	else:
		print(str1)
		str1+="*"

