'''
    A
   B B
  C   C
 D     D
EEEEEEEEE

'''

n = int(input("Enter number "))

stars = 1

ch = 65

for i in range(1,n+1):
	print()
	print(" "*(n-i),end="")




	for j in range(1,stars+1):

		if j == 1 or  j ==stars or i ==n:

			print(chr(ch),end="")

		else:
			print(" ",end="")
	
	stars+=2
	ch+=1
