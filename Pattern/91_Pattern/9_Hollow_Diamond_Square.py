'''9_Hollow_Diamond_Square.py
***** *****
****   ****
***     ***
**       **
*         *
*         *
**       **
***     ***
****   ****
***** *****

'''


n = 5  # number of rows for half pattern

for i in range(n):


    stars = n -i

    spaces = 2*i+1

    if i ==0:
        print("*"*(2*n+1))

    else:

        print("*"*stars+" "*spaces+"*"*stars)




