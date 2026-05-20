'''
55555
 4__4 
  3_3
   22
    1
'''


n = int(input("Enter number "))

temp = n

for i in range(n,0,-1):

	print()
	print(" "*(n-i),end="")

	if i ==1 or i ==2 or i ==n:

		for j in range(1,i+1):

			print(temp,end="")


	else:

		for j in range(1,i+1):

			if j == 1 or j==i:

				print(temp,end="")

			else:
				print("_",end="")

	temp-=1