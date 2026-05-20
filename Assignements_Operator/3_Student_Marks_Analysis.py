'''3_Student_Marks_Analysis.py
Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2

---

'''

mark1,mark2,mark3,mark4,mark5 = map(int,input("Marks of 5 subject = ").split(","))

total = mark1 + mark2 + mark3 + mark4 +mark5

avg = (mark1 + mark2 + mark3 + mark4 +mark5)/5

percentage = (total/500)*100

print("Total = ",total)
print("Average =",avg)
print("Percentage =",percentage,"%")