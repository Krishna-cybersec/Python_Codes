'''
1
22
3 3
4  4
55555
'''
n = int(input("Enter number = "))



for i in range(1,n+1):

	if i == 1 or i ==2:
		print(i*str(i))

	elif i ==n:
		print(i*str(i))
	
	else:
		print(str(i)+" "*(i-2)+str(i))



	



