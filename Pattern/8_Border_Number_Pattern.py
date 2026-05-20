'''8_Border_Number_Pattern.py

    1 2 3 4 5
    2       5
    3       5
    4       5
    5 5 5 5 5
'''


n = int(input("Enter number = "))

for k in range(1,n+1):

    print()

    if k ==1 or k == n-1:

        for i in range(1,6):

            print(i,end="")




    else:

        for j in range(1,6):

            if j == 1 or j ==5 :

                print(j,end="")

            else:

                print(" ",end="")
