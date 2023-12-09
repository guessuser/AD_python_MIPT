class Vector(): 
    def __init__(self, xyz = str):
        x, y, z = xyz.split(',')
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def __str__(self): 
        return('('+str(self.x)+ ', '+ str(self.y) +', '+ str( self.z) + ')')
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        xyz = str(x)+','+str(y)+','+str(z)
        return(Vector(xyz))
    def __abs__(self):
        product = (self.x**2+self.y**2+self.z**2)**(0.5)
        return(product)
    def dot_product(self, other):
        dot_product = self.x*other.x + self.y*other.y + self.z*other.z
        return(dot_product)
    def cross_product (self, other): 
        i = self.y*other.z - self.z*other.y
        j = self.x*other.z - self.z*other.x
        k = self.x*other.y - self.y*other.x
        product = str(i)+','+str(-j)+','+str(k)
        product = Vector(product)
        return(product)
    def __mul__(self, value): 
        product = str(value*self.x)+','+str(value*self.y)+','+str(value*self.z)
        return(Vector(product))
