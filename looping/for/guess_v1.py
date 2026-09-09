from random import randint
secret_num=randint(1,10)
for i in range(1,6):
    num=int(input('Guess the number from 1-10:'))
    if num==secret_num:
        print("Congrats✨")
        break
else:
    print("Bad luck💀")
