'''1.Digit Product Analyzer System

A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

For every entered number, the system analyzes relationships between its digits.

Write a program to:

Find the product of every pair of adjacent digits
Display all the products
Find the sum of all these products
Find the smallest product value
If the sum of products is divisible by the total number of digits, print Stable Number
Otherwise print Unstable Number

Use loops wherever required.

Input:
57294

Output:
Products: 35 14 18 36
Sum = 103
Smallest = 14
Unstable Number
'''

n = int (input("Enter the number = "))

count = 0

pro = ""

sum = 0 

digit = len(str(n))

for i,j in enumerate(str(n)):

	j = int(j)


	if i == 0:

		count = j
		continue

	else:

		count *= int(j)
		pro  += str(count)+" "
		sum += count
		count = j





#print(count)
print("product = ",pro)
print("sum = " ,sum)

smallest = sum




for i,z in enumerate((str(n))):


	z = int(z)
	if i == 0:

		count = z
		continue

	else:

		count *= int(z)

		#print(count)

		if count < smallest:

			smallest = count

		count = z
	

print("smallest",smallest)


if sum %  digit == 0:

	print("Stable Number")

else:

	print("Unstable Number")

'''


n = input("Enter the number = ")

total_sum = 0
product_str = ""
digit_count = len(n)

smallest = None

for i in range(len(n) - 1):
    a = int(n[i])
    b = int(n[i + 1])

    prod = a * b

    product_str += str(prod) + " "
    total_sum += prod

    if smallest is None or prod < smallest:
        smallest = prod

# Edge case: single digit
if smallest is None:
    smallest = 0

print("Products =", product_str)
print("Sum =", total_sum)
print("Smallest =", smallest)

if total_sum % digit_count == 0:
    print("Stable Number")
else:
    print("Unstable Number")

'''