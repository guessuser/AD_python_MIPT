from typing import Any


class Complex(): 
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __str__(self):
        return(str(self.real) + ' + i*' + str(self.imaginary))
        #return(self.real, self.imaginary)
    def conjugate(self): 
        product = Complex(self.real, -self.imaginary)
        return(product)
    def __abs__(self): 
        abs_complex = (self.imaginary**2+self.real**2)**(1/2)
        return(abs_complex)
    def __add__(self, second):
        real_product = self.real + second.real
        imaginary_product = self.imaginary + second.imaginary
        product = Complex(real_product, imaginary_product)
        return(product)
    def __neg__(self): 
        product = Complex(-self.real, -self.imaginary)
        return(product)
    def __sub__(self, second):
        neg_second = second.negative() 
        product = self.sum_complex(neg_second)
        return(product)
    def __mull__(self, second): 
        real_product = self.real*second.real - self.imaginary*second.imaginary
        imaginary_product = self.real*second.imaginary + self.imaginary*second.real
        product = Complex(real_product, imaginary_product)
        return(product)

    def __truediv__(self, second): 
        denominator = second.real**2 - second.imaginary**2
        real_product = (self.real * second.real + self.imaginary*second.imaginary)/denominator
        imaginary_product = (self.imaginary*second.real - self.real*second.imaginary )/denominator
        product = Complex(real_product, imaginary_product)
        return(product)


#Example    
Z_1 = Complex(-1, -1)
Z_2 = Complex(2, 3)
print(Z_2)
print(abs(Z_1+Z_2))
print(Z_1/Z_2)
