'''
     *
    * *
   * * *
  * * * *
 * * * * *

'''



'''star space logic

n = int(input("Enter number "))

for i in range(1,n+1):

	print()
	print(" "*(n-i),end="")

	for j in range(1,i+1):

		print("* ",end="")
			

'''

# no nested loop

'''
n = int(input("Enter number "))

for i in range(1,n+1):

	print(" "*(n-i)+"* "*i)

'''
# odd method


n = int(input("Enter number "))

stars = 1

for i in range(1,n+1):
	print()
	print(" "*(n-i),end="")

	for j in range(stars):

		if j%2==0:

			print("*",end="")

		else:
			print(" ",end="")
	
	stars+=2
