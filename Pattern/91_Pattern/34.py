n = int(input("Enter n "))

str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for i in range(n-1,-1,-1):

 	print(str1[i]*(i+1))