'''
1
1 2
1  3
1   4
1  3
1 2
1
'''

n = int(input("Enter number "))

temp1 =""

c = n


#print(temp2)

for i in range(1,n*2):


	if i==1:
		temp1+=str(i)
		print(1)


	elif i <= n:

		temp1+=str(i)
		print(temp1[0]+" "*(i-1)+temp1[i-1])

	elif i >n:

		if i ==(n*2)-1:
			print(1)

		else:
			c-=1
			print(temp1[0]+" "*(c-1)+temp1[c-1])



		
