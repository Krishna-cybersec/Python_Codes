'''2_Smallest_Digit.py
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2
'''


n = int(input("Enter the number "))



while n>0 :
	
	rem = n%10
	#print(rem)

	s = rem

	if 	s < rem :

		s = rem

	n = n//10

print(s)