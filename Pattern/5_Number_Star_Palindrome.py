'''5_Number_Star_Palindrome.py
    12344321
    123**321
    12****21
    1******1
'''

n = int(input("Enter number = "))




for i in range(n-1):

    print()
    
    for z in range(1,n-i):


        print(z,end="")

    
    for x in range(n-i,n):

        print("*"*2,end="")



    for j in range((n-1)-i,0,-1):

        print(j,end="") 