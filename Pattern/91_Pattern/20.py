'''
1
12
1 3
1  4
12345
'''
n = int(input("Enter number = "))

str1 = ""

for i in range(1,n+1):

	if i == 1 or i ==2:
		str1+=str(i)
		print(str1)

	elif i ==n:
		str1+=str(i)
		print(str1)
	
	else:
		str1+=str(i)
		print(str1[0]+" "*(i-2)+str(i))



	



