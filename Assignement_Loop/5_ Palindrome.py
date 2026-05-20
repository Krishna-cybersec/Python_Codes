'''5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to **check whether a given number is a palindrome using loops**.

Input: 121
Output: Palindrome

---

'''

n = int(input("number : "))
z=n
j = 0 


while n>0:
	rem = n%10
	j = j*10+rem
	n = n//10



if j == z:
	print("Palindrome")

else:
	print("Not a Palindrome")

