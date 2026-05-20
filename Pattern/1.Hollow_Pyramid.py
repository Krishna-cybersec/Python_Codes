'''1.Hollow_Pyramid.py
        *
       * *
      *   *
     *     *
    *********
'''

n = int(input("Enter number"))

for i in range(0,n):

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


print()

for k in range(1,n*2):

        print( "*",end="")


                



        

        






