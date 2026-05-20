'''
*1
**12
****1234
*******
***********
'''

n = int(input("Enter number "))

str1 ="*"
for i in range(1,n+1):

	print(str1)
	str1+="*"*i