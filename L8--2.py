import itertools

def get_permutations(s, n):
    return(list(itertools.permutations(s, n)))

print(get_permutations('dog', 2))
#FIXME