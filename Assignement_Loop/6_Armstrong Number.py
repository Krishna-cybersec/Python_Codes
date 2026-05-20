'''6_Armstrong Number.py
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to **check whether a number is an Armstrong number using loops**.

Input: 153
Output: Armstrong

---
'''

# For any digit with power of len(n)

n = int(input("Enter the number = "))
z=n
j =0
ln = len(str(n))

while n >0:
	rem = n%10
	j  = j+(rem**ln)
	n=n//10


if j ==z:
	print("Armstrong")

else:
	print("Not a Armstrong")




# Only for 3 digit with power of 3

'''while
n = int(input("enter the number "))
z=n
j =0

while n >0:
	rem = n%10
	j  = j+rem**3
	n=n//10

if j ==z:
	print("Armstrong")

else:
	print("Not a Armstrong")

'''

'''for
n =int(input("Enter the number"))

j = 0

for i in str(n):
	j+=int(i)**3


print(j)
if j ==n:
	print("Armstrong")

else:
	print("Not a Armstrong")
'''

