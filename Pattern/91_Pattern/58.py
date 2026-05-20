'''
    A
   ABC
  ABCDE
 ABCDEEF
ABCDEFGHI
'''



n = int(input("Enter number "))

ch = 64
stars =1 
for i in range(1,n+1):

	print()
	print(" "*(n-i),end="")

	for j in range(1,stars+1):

		print(chr(ch+j),end="")

	stars+=2
		

			