from L6_2 import *

Vector_1 = Vector(input())
Vector_2 = Vector(input())
Vector_3 = Vector(input())

print('площадь параллелограмма на векторах 1 и 2 S = ', abs(Vector_1.cross_product(Vector_2)))
print('объём параллелепипеда на векторах 1, 2, 3 V = ', abs(Vector_1.cross_product(Vector_2.cross_product(Vector_3))))