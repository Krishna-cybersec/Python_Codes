'''4_Digit_Gap.py
A number analysis system checks whether the gap between digits follows a consistent pattern.

Write a program to:

Find the absolute difference between first two digits
Compare this difference with all next adjacent digit differences
If any difference is not equal to the first difference, stop using break
Display:
- Initial gap
- Whether all gaps are same or not

Input:
8642

Output:
Initial Gap = 2
Consistent Pattern

Input:
97531

Output:
Initial Gap = 2
Consistent Pattern

Input:
5321

Output:
Initial Gap = 2
Pattern Break Detected
'''

n = input("Enter the number = ")

diff = 0 

for i in range(len(n)-1):

	if i == 0:


		a  = n[i]
		b  = n[i+1]

		diff  = abs(int(a) - int(b))

		print("Initial Gap =" ,diff)

	else:

		a = n[i]
		b = n[i+1]

		if abs(int(a) - int(b)) == diff:

			continue

		else:

			print("Pattern Break Detected")
			break

else:

	print("Consistent Pattern")






