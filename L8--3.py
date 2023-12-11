import itertools
def get_combinations(s, n):
    return(list(itertools.combinations(s, n)))

print(get_combinations('cat', 2))
#FIXME