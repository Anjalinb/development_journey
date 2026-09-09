num=int(input("Enter the number:"))
while(num!=0):
    digit=num%10
    if digit%2==0:
        print(num)
        break
    else:
        num=num//10
