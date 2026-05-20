'''4_Vertical_Diamond.py
       *
      * *
     *   *
    *     *
     *   *
      * *
       *
'''

n = int(input("Enter number"))

for i in range(0,n//2+1):

       print()

       for z in range(0,n-i):

              print(" ",end="")

        #print(" ",end="")

       for j in range(0,i):


              if  j == 0:
                     print("*",end="")

              else:
                     print(" ",end="")

       for j in range(n,n+i):


              if j != (n-2)+i:

                     print(" ",end="")
              else:
                     print("*",end="")

for i in range((n//2)-1,0,-1):

       print()

       for z in range(0,n-i):

              print(" ",end="")

        #print(" ",end="")

       for j in range(0,i):


              if  j == 0:
                     print("*",end="")

              else:
                     print(" ",end="")

       for j in range(n,n+i):


              if j != (n-2)+i:

                     print(" ",end="")
              else:
                     print("*",end="")

