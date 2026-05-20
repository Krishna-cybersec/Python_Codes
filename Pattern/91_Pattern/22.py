'''
A
AB
A C
A  D
ABCDE
'''

n = int(input("Enter n "))
asci = 64
str1 = ""

for i in range(1,n+1):

	if i == 1 or i ==2:
		asci +=1
		str1 += chr(asci)
		print(str1)

	elif i ==n:
		asci +=1
		str1 += chr(asci)
		print(str1)

	else:
		asci +=1
		str1 += chr(asci)
		print(str1[0]+" "*(i-2)+str1[i-1])



