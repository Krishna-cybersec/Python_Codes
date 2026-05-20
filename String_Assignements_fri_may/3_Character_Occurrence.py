'''3_Character_Occurrence.py

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good  to
Enter character to check: o

Output: Character 'o' occurs: 4 times'''


str1 = input("Enter product review:  ")
numb = input("Enter character to check  ")

count = 0



for i in str1:

	if i == numb:

		count+=1


print(str1,count)