from L6_2 import *

N = int(input())

coordinates = []
max_d = 0 
max_id = 0
for i in range(N): 
    coordinates.append(Vector(input()))
    distance = abs(coordinates[i])
    if max_d < distance:
        max_d = distance
        max_id = i
print('самая удаленная точка ', coordinates[max_id])