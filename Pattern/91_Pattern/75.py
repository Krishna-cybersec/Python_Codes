'''
     *
    *_*
   *_*_*
  *_*_*_*
   *_*_*
    *_*
     *
'''


n = int(input("Enter number "))

temp1 =""

c = n
temp2="x"

#print(temp2)

for i in range(1,n*2):

	print(" "*(n-i),end="")
	if i <= n:

		temp1+="x"
	
		#if i != n:
		#	temp1 += "_"
		print("_".join(temp1))

	else:
		
		print(" "*(i-n), end="")
	
		c-=1

		print("_".join(temp1[:c])) 


