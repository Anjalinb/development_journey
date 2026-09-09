def gcd_of_two_numbers(num1,num2):
    
    for i in range(1,min(num1,num2)+1):

        if num1%i==0 and num2%i==0:

            gcd=i

    print(gcd)

gcd_of_two_numbers(18,24)
gcd_of_two_numbers(10,20)