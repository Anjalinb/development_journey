text="@hello@"

new=text.strip("@") #removes value from both ends, not in between
print(new)
new_l=text.lstrip("@") #removes value from left
new_r=text.rstrip("@") #removes value from right
print(new_l)
print(new_r)

print("a" in "apple")