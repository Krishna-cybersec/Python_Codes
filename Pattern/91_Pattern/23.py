'''
a
bc
d f
g  j
klmno
'''

n = int(input("Enter n "))
asci = 97
str1 = ""

for i in range(1,n+1):
	print()

	if  i <3:
		for j in range(i):
			print(chr(asci),end="")
			asci+=1


	elif i == n:
		for j in range(i):

			print(chr(asci),end="")
			asci+=1

	else:

		for j in range(i):

			if j == 0:

				print(chr(asci),end="")
				asci+=1

			elif j == i-1:
				print(chr(asci),end="")
				asci+=1

			else:
				print(" ",end="")
				asci+=1






