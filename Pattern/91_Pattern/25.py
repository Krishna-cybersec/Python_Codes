n = int(input("Enter n "))

str1 =""
temp = n

for i in range(1,n+1):

		str1+=str(temp)
		temp-=1

		print(str1)
