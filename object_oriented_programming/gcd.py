class Gcd:
    def solution(self,num1,num2):
        small=min(num1,num2)
        for i in range (1,small+1):
            if num1%i==0 and num2%i==0:
                gcd=i
        print(gcd)

gcd_instance=Gcd()
gcd_instance.solution(6,24)
gcd_instance.solution(20,24)