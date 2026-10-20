"""
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *

"""
n=int(input("Enter no. of rows:"))
space=0
num=n//2

for r in range(n//2):

    for c in range(num):
        print("*",end=" ")

    for sp in range(space):
        print(" ",end=" ")

    for j in range(num):
        print("*",end=" ")

    space+=2
    num-=1
    print()


num=1
space=n-2
for r in range(n//2):

    for c in range(num):
        print("*",end=" ")

    for sp in range(space):
        print(" ",end=" ")

    for j in range(num):
        print("*",end=" ")

    space-=2
    num+=1
    print()
    

