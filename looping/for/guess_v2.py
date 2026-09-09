from random import randint
secret_num=randint(1,10)
for i in range(1,6):
    num=int(input('Guess the number from 1-10:'))
    if num==secret_num:
        print("Congrats✨")
        print(f"You won in {i} attemt")
        break
    elif num<secret_num :
        print("Too low!")
    elif num>secret_num :
        print("Too high")

else:
    print("Bad luck💀")
