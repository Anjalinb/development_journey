num=int(input("Enter the number:"))
sum=0
while num!=0:
    digit=num%10
    cube=digit**3
    sum+=cube
    num=num//10
print("Sum of cube of digits:",sum)