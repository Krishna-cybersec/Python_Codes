'''6_Number_Triangle_with_Dashes.py
    - - - - 1
    - - - 2 3
    - - 3 4 5
    - 4 5 6 7
    5 6 7 8 9
'''


n = int(input("Enter number = "))

for i in range(1,n+1):

        print()

        for z in range(0,n-i):

                print("-",end="")

        #print(i,end="")

        for j in range(i,i*2):

            print(j,end="")



