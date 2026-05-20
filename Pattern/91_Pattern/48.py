'''
    1
   10
  101
 1010
10101
'''

n = int(input("Enter number "))

str1 ="1"

for i in range(1,n+1):
	print(" "*(n-i),end="")
	

	if i%2==0:

		print(str1)
		str1+="1"

	else:
		print(str1)
		str1+="0"