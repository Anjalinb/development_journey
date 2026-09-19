text="@hello@"

new=text.strip("@") #removes value from both ends, not in between
print(new)
new_l=text.lstrip("@") #removes value from left
new_r=text.rstrip("@") #removes value from right
print(new_l)
print(new_r)

print("a" in "apple")
"""
textwrap has functions/methods such as:

textwrap.wrap() → splits text into a list of lines
textwrap.fill() → splits text and returns it as one string with \n
textwrap.shorten() → shortens text to a given width
"""