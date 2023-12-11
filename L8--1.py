from itertools import product
def get_cartesian_product(a, b):
    return(list(product(a,b, repeat= 1)))
a = ['s', 'l']
b = [23, 45]

print(get_cartesian_product(a, b))
