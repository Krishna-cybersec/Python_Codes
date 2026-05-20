'''
123456789
 1     7
  1   5
   1 3
    1
'''


n = int(input("Enter n "))


for i in range(n,0,-1):

		print()
		print(" "*(n-i),end="")

		if i ==n : 
			for j in range(1,i*2):

				print(j,end="")


		else:

			for j in range(1,i*2):


				if j == 1 or j == (i*2)-1:

					print(j,end="")

				else:

					print(" ",end="")





