class Leap_yr:
    def solution(self,year):
        if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
            print("Leap year")
        else:
            print("Not a leap year")

leap_instance=Leap_yr()
leap_instance.solution(2024)
leap_instance.solution(2022)
