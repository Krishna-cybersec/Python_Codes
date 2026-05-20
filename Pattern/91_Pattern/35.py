'''
*****
*  *
* *
**
*
'''

n = int(input("Enter number "))

s =""

for i in range(n,0,-1):

	if i == n:

		s+="*"*i

		print(s)


	elif i ==1:
		print("*")
	else:

		print(s[0]+" "*(i-2)+s[i])
