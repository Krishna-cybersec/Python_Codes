'''9.Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
'''

n = int(input("Enter number = ")) #5729

l = 0#1

count = 0#5

sum = 0

step = ""

biggest = 0

for i in str(n):#7

	if l >0: 
		count = abs(count - int(i)) 

		if count > biggest:
			biggest = count

		sum += count 

		step = step + str(count) + " "
			
		count = int(i)



	l = 1 
	count =int(i)#7


print("step",step)
print("sum",sum)
print("largest",biggest)



''' method 2
num  = int(input("Enter number = "))

temp = num

count = 0

sum = 0




for j in str(num):

	if [j] ==1:
		continue

	count = abs(count - int(j))
	
	print(count,end=" ")
	count = int(j)

'''


