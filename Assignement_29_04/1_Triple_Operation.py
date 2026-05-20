'''1_Triple_Operation.py

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime

'''


num = int(input("Enter number"))

temp = num
sum_digits = 0
while temp > 0:
    sum_digits += temp % 10
    temp //= 10

temp = num
rev = 0
while temp > 0:
    rev = rev * 10 + (temp % 10)
    temp //= 10

diff = abs(num - rev)

final = sum_digits + diff

print("Sum of Digits =", sum_digits)
print("Reverse =", rev)
print("Difference =", diff)
print("Final Result =", final)

if final < 2:
    print("Not Prime")
else:
    for i in range(2, int(final**0.5) + 1):
        if final % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
```