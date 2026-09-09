"""
1
0 1
1 0 1
0 1 0 1
"""

for r in range(1,5):
    for c in range(1,r+1):
        if r==c or r-c==2:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
