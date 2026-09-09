def product(*args):
    product=1
    for i in args:
        product=product*i

    return(product)

print(product(2,3,4))
print(product(1,3,2))




