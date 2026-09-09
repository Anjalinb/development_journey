def armstrong(num):
    original=num
    length=len(str(num))
    sum=0
    while num!=0:
        digit=num%10
        sum+=digit**length
        num=num//10
    if sum==original:
        print("Armstrong number")
    else:
        print("Not Armstrong number")


armstrong(153)
armstrong(123)