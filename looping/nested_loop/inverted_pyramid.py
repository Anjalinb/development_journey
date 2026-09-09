"""
* * * * * *  ->row-6,sp-0,c-6
 * * * * *   ->row-5,sp-1,c-5
  * * * *
   * * *
    * *
     *
"""
for r in range(6,0,-1):
    for sp in range(0,(6-r)):
        print(" ",end="")
    for c in range(r,0,-1):
        print("*",end=" ")
    print()