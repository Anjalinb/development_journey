"""
      *       ->row-6,sp-5,c-1
     * *      ->row-5,sp-4,c
    *   *     ->row-4,sp-3,
   *     *    ->row
  *       *
 * * * * * *

"""
for r in range(1,6):
    for c in range(1,10):
        
        if r+c==6 or c-r==4 or r==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    

       
        
