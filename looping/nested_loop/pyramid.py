"""
      *       ->row-6,sp-6,c-1
     * *      ->row-5,sp-5,c-2
    * * *     ->row-4,sp-4,c-3
   * * * *    ->row
  * * * * *
 * * * * * *

"""
for r in range(6,0,-1):
    for sp in range(1,r):
        print(" ",end="")
    for c in range(1,(7-r)+1):
        print("*",end=" ")
    print()
