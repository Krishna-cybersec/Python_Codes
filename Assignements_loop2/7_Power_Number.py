'''7_Power_Number.py
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32
'''


b,p = map(int,input("Enter base and power : ").split(" "))


count = 0
power = 1

while count < p:
	power *=b 
	count +=1

print(power)





