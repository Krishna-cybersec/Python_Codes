'''
123456789
 1234567
  12345
   123
    1
'''


n = int(input("Enter n "))


for i in range(n,0,-1):

		print()
		print(" "*(n-i),end="")


		for j in range(1,i*2):

			print(j,end="")


