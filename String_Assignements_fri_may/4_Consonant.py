'''4_Consonant.py

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U

'''


n = input("Enter string = ").lower()

c = 0
for i in n:

	if i not in "aeiou" and i != " ":

		c+=1


print("Total consonants: ",c)