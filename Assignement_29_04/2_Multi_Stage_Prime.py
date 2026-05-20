'''2_Multi_Stage_Prime.py


A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime

'''

num = int(input())

temp = num
s = 0
p = 1

while temp > 0:
    d = temp % 10
    s += d
    p *= d
    temp //= 10

diff = p - s

temp = abs(diff)
count = 0
while temp > 0:
    count += 1
    temp //= 10

final = diff + count

print("Sum =", s)
print("Product =", p)
print("Difference =", diff)
print("Digits =", count)
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

