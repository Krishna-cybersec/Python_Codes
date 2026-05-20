'''2_Space_Counter.py

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5
'''

n = input("Enter string ")

count = 0
for i in range(len(n)-1):

	if n[i] == " ":

		count+=1



print("Total spaces = ",count)