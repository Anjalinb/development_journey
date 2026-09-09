attendance = ["p","p","a","a","o","o","h"]
att_set=set(attendance)
att_count={}
for w in att_set:
    att_count[w]=attendance.count(w)

print(att_count)