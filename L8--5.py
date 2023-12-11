import itertools 
def keyfunc():
    pass
def compress_string(s):
    return(list(itertools.groupby(s)))

print(compress_string('1222311'))