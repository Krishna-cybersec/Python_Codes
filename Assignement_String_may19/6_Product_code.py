'''
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
'''

n = input("Enter 1st code ").lower()
m = input("Enter 2nd code ").lower()


n = n.replace(" ","")
m = m.replace(" ","")



for i in n:


	if n.count(i) == m.count(i):

		print(i,n.count(i),m.count(i))

		continue

	else:
		print("Both Product Codes are NOT  Matching")
		break

else:
	print("Both Product Codes are Matching")