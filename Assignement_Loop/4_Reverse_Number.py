'''4_Reverse_Number.py
A security system stores OTP codes in reverse format for encryption to increase data safety. Reversing a number means extracting digits and rebuilding it in reverse order.
Write a program to **reverse a given integer using loops**.

Input: 1234
Output: 4321
'''

'''
n = int(input("Enter number = "))

j = 0

while n > 0:
	r = n%10
	print(r,end="")
	j = j*10+r

	n = n//10

print("output",int(j))

'''

''' Note : Original number mein reverse ni hai 

n = int(input("Enter number = "))

while n > 0:
	r = n%10
	print(r,end="")
	n = n//10

'''

# For loop with str

''' 
n = input("Enter number = ")#123

rev = ""

for i in n:

	rev = i +rev #3+2+1 = 321

print("Reverse number is ",rev)
'''



