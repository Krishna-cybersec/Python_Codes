n = int(input("Enter number "))

str1 = "1"
str2 = "01"
for i in range(1,n+1):

	if i%2 ==0:

		print(str2*(i//2))

	else:
		print(str1)
		str1+="01"
		

