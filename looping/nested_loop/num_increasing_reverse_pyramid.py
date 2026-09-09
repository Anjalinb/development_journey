"""
1 2 3 4
1 2 3
1 2
1
"""

for r in range(4,0,-1):
    for c in range(1,r+1):
        print(c,end=" ")

    print()