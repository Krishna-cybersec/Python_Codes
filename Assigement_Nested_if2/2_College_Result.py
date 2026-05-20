'''2_College_Result.py
2. College Result Processing System


A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

* 90 and above → Grade A
* 75 to 89 → Grade B
* 60 to 74 → Grade C
* 50 to 59 → Grade D
* Below 50 → Fail

Write a Python program to display the grade of a student.

Input:
Enter marks: 67

Output:
Grade: C
'''

grade = int(input("Enter marks: "))

if grade >=90:

	print("Grade A")

elif grade>89 and grade<75:
	print("Grade B")

elif grade>60 and grade<74:
	print("Grade C")

elif grade>50 and grade<59:
	print("Grade D")

else:
	print("Fail")
