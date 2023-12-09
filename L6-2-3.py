from L6_2 import *

N = int(input())

coordinates = []
mass_center = (Vector('0,0,0'))

for i in range(N): 
    coordinates.append(Vector(input()))
    mass_center += coordinates[i]
mass_center = mass_center*(1/N)
print(mass_center)
    