'''9_Check_All_Digits_Are_Even.py
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to **check whether all digits of a number are even using loops**.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even

---

'''

n =int(input("N = "))


result = ""
while n>0:
	rem = n%10

	if rem %2!=0:
		print("Not all even")
		break

	else:
		result ="All even"

	n = n//10

print(result)

