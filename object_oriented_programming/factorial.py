class Factorial:
    def solution(self,num):
        factorial=1
        for i in range(1,num+1):
            factorial*=i
        print(factorial)

fc_instance=Factorial()
fc_instance.solution(4)