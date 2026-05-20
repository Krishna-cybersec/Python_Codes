'''
x
xx
xxx
xxxx
xxx
xx
x
'''

n = int(input("Enter number "))

temp1 =""

c = n
temp2="x"

#print(temp2)

for i in range(1,n*2):

	if i <= n:

		temp1+="x"
		print(temp1)

	elif i >n:

		c-=1
		print(temp2*c) 

		




	