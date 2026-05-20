n = int(input("Enter n "))

str1 ="1"

for i in range(1,n+1):

	if i %2 !=0:


		if i == 1 or i==n:

			print(str1)

		else:
			print(str1[0]+" "*(i-2)+str1[i-1])


		str1+="0"





	else:


		if i ==2 or i==n:
			print(str1)
		

		else:
			print(str1[0]+" "*(i-2)+str1[i-1])

		str1+="1"


