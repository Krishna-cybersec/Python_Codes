'''5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code

'''


n = input("Enter code ")

m = n[::-1]

if n == m:

	print("Palindrome Code")

else:

	print("Not a Palindrome Code")