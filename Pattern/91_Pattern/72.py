'''
1
12
123
1234
123
12
1
'''
n = int(input("Enter number "))

temp1 =""

c = n


#print(temp2)

for i in range(1,n*2):

	if i <= n:

		temp1+=str(i)
		print(temp1)

	elif i >n:

		c-=1
		print(temp1[:c]) 

		
