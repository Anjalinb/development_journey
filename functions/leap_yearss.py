def leap_years(start,stop):
    for i in range(start,stop+1):
        if (i%100==0 and i%400==0) or (i%100!=0 and i%4==0):
            print(i)


leap_years(2000,2026)