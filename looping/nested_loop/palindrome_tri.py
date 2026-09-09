"""
      1        ->sp=6 c=1
    2 1 2      ->sp=4 c=3
  3 2 1 2 3    ->sp=2 c=5
4 3 2 1 2 3 4  ->sp=0 c=7


"""
for r in range(6,2,-1):
    for sp in range(1,r+1):
        print(" ",end="")
   