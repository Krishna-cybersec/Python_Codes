'''4_E-Learning_Course_Access.py

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test
'''

sub = input("Subscription = ").lower()

prog = int(input("Progress = "))

score  = int(input("Test score = "))

if sub == "premium":

	if prog >=80:

		if score >=70:

			print("Certificate Unlocked")

		else:
			print("Retry")


	else:
		print("Complete course")


elif sub == "basic":

	if prog >=50:
		print("Limit access")

	else:
		print("Content locked")


else:

	print("Access Denied")

