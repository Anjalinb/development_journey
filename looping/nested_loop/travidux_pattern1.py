"""
1
2 7
3 8 12
4 9 13 16
5 10 14 17 19
6 11 15 18 20 21
"""
n=int(input("Enter no of rows:"))
num=1
diff=n-1

for r in range(1,n+1):
    print(num,end=" ")
    for c in range(1,r):
        new=new+diff
        print(new,end=" ")
        diff-=1
    num+=1
    new=num
    diff=n-1
    print()


