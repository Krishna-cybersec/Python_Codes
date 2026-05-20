'''2_Factorial.py
In project scheduling, tasks are dependent on previous tasks, and the total number of ways to arrange them is calculated using factorial. Factorial of a number n is the product of all numbers from 1 to n.
Write a program to calculate the **factorial of a given number using loops**.

Input: n = 5
Output: Total Ways = 120

---
'''


n =int(input("N = "))

#while
'''
sum = 1

while n>0 :
	sum *=n
	n-=1


print(sum)
'''

#for -1

'''


sum =1
for i in range(1,n+1):
	sum*=i

print(sum)
'''
#for -2

'''


sum =1
for i in range(n,0,-1):
	sum*=i

print(sum)
'''

# By math

'''
import math

print("Factorial",math.factorial(n))
'''
