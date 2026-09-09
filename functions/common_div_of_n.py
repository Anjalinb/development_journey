def common_div_of_n(number):
    for i in range(1,number+1):
        if number%i==0:
            print(i,end=" ")

common_div_of_n(7)
common_div_of_n(13)
common_div_of_n(22)
common_div_of_n(15)