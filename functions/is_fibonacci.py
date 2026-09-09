def is_fibonacci(num):
    first=0
    second=1
    next=first+second
    while next<num:
        first=second
        second=next
        next=first+second

    if next==num:
        print(True)
    else:
        print(False)

is_fibonacci(55)
is_fibonacci(24)
is_fibonacci(144)
