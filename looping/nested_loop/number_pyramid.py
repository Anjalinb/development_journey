"""
   1
  2 2
 3 3 3
4 4 4 4
"""

for r in range(4,0,-1):
    for sp in range(1,r):
        print(" ",end="")
    for c in range(1,(5-r)+1):
        print(5-r,end=" ")
    print()
