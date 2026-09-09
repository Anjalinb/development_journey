placement_count=[10,15,22,9,17,18]
print("February:",placement_count[1])


placement_count[0]=12
print(placement_count)


print("Greater than 15-")
for count in placement_count:
    if count>15:
        print(count)



max=placement_count[0]
for i in placement_count:
    if i>max:
        max=i
print("Highest-",max)


min=placement_count[0]
for j in placement_count:
    if j<min:
        min=j
print("Lowest-",min)


second_high=0
for k in placement_count:
    if k>second_high and k!=max:
        second_high=k
print("Second highest=",second_high)


