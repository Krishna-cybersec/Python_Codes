'''
123456
54321
1234
321
12
1
'''


n = int(input("Enter number "))

temp = n
str1 =""


for i in range(1,n+1):

	if i %2 !=0:
		
		print()

		for j in range(1,temp+1):

			print(j,end="")


	else:

		print()


		for j in range(temp,0,-1):

			print(j,end="")


	temp-=1





