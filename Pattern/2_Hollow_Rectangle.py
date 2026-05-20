'''2_Hollow_Rectangle.py
    *********    
    *       *
    *       *
    *       *
    *********
'''


n = int(input("Enter number = "))

for k in range(n):

    print()

    if k ==0 or k == n-1:

        for i in range(9):

            print("*",end="")




    else:

        for j in range(9):

            if j == 0 or j ==8:

                print("*",end="")

            else:

                print(" ",end="")



