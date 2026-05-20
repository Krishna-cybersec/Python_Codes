'''7_Cricket_Run_Rate.py

---

Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67

---
'''

runs = int(input("Total runs ="))
over,run = map(int,input("Overs = ").split("."))

total_ball = (over*6)+run
run_rate = runs/over

print("Total Balls =",total_ball)
print("Run Rate =",round(run_rate,2))
