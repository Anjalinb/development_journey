placement_count=[10,15,22,9,17,18]
first_max=0
second_max=0
for count in placement_count:
    if count>first_max:
        second_max=first_max
        first_max=count
    elif count>second_max:
        second_max=count
print(second_max)

""" METHOD 2 """

maxx=max(placement_count)
placement_count.remove(maxx)
print(max(placement_count))