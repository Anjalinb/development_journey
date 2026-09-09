def sum_of_digits(num):
    sum=0
    while num!=0:
        digit=num%10
        sum+=digit
        num=num//10
    print(sum)

sum_of_digits(5432)
