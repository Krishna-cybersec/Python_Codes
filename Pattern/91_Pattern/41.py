'''
A
BCD
EFGHI
JKLMNOP
'''

n = int(input("Enter number "))
ch = 65



for i in range(1,2*n,2):

	print()
	for j in range(i):
		print(chr(ch),end="")

		ch+=1

	





