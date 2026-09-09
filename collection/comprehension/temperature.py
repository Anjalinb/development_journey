temp=[18,22,35,28,15]
new=["cold" if t<=20 else "warm" if t>20 and t<=30 else "hot" for t in temp]
print(new)