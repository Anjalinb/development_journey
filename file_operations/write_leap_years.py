#1800-2026
fw=open("file_operations\\leap_years.txt","w")
for y in range(1800,2027):
    if (y%100==0 and y%400==0) or (y%100!=0 and y%4==0):
        fw.write(str(y)+"\n")
