num=int(input("Enter the number:"))
original=num
count=len(str(num))
sum=0
while(num!=0):
    digit=num%10
    sum=sum+digit**count
    num=num//10
print(sum)
if sum==original:
    print("Armstrong number")
else:
    print("Not Armstrong number")