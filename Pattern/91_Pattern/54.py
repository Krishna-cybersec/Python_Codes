'''
ABCDE
 ABCD
  ABC
   AB
    A
'''

n = int(input("Enter number "))

ch = 64


for i in range(n,0,-1):

	print()
	print(" "*(n-i),end="")


	for j in range(1,i+1):

		print(chr(ch+j),end="")


