'''6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2
'''



n = int(input("Enter number = "))

prime = "prime number"

count = 2

lower = 9

if n <=1:
	prime = "Not prime nor composite "


else:

	for i in range(2,(n//2)+1):

		if n%i==0:
			prime = "composite number"
			count+=1

			if i < lower:
				lower = i
		

			


print(prime)
print(count)
print(lower)


