class shape():
    def __init__(self, width, height):
        self.width = width
        self.height = height

class triangle(shape):

    def area(self): 
        return(self.height*self.width/2)

class rectangle (shape):
    def area(self): 
        return (self.width*self.height)

A = triangle(3, 4)
B = rectangle(4, 3)
print(A.area(), B.area())

