'''1_Vowel_Counter.py

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
'''

n = input("Enter = ").lower()

i = 0

count = 0
while i<len(n):

	

	if n[i] in "aeiou":
		count+=1
	i+=1


print(count)


