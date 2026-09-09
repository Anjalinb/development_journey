attendance=[1,-1,0,1,-1,1,-1,0,0]
new=["p" if a==1 else "o" if a==-1 else "h" for a in attendance]
print(new)