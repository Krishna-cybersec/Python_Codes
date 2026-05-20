'''
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2 
    1

'''
n = int(input("Enter number "))



for i in range(n,0,-1):

		print()
		print(" "*(n-i),end="")


		for j in range(1,i+1):

			print(str(i)+" ",end="")


