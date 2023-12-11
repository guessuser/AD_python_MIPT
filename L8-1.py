"""def print_map(function, iterable):
    for i in iterable:
        print(function(i))"""

def print_map(function, iterable): 
    print(*list(map(function, iterable)))

#Example 

def around_the_world(n):
    return(n * ' Around the world ')
def sq(n):
    return(n**2)

a = [2, 3, 5, 11]

print_map(around_the_world, a)
print_map(sq, a)