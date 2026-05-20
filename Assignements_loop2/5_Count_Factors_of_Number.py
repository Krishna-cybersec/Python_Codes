'''5_Count_Factors_of_Number.py
5. Count Factors of Number
A mathematics learning app gives practice questions where students must know how many factors a number has. The app should automatically count the total factors of the entered number.
Write a program to count total factors of a number using loops.

Input:
12

Output:
Factors Count = 6
'''

number = int(input("Enter number "))

count = 1

for i in range(1,number//2+1):

	
	if number % i == 0:

		count+=1


print(count)