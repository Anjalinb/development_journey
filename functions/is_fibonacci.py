def is_fibonacci(num):
    a,b=0,1
    while a<num:
        a,b=b,a+b
        if a==num:
            print(True)
            break
    else:
        print(False)


is_fibonacci(55)
is_fibonacci(24)
is_fibonacci(144)
