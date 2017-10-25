
class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled
        
    def getColor(self):
        return self.__color
    
    def isFilled(self):
        return self.__
    
    def setColor(self, color):
        self.__color = color
        
    def setFilled(self, filled):
        self.__filled = filled
        
    def __str__(self):
        return "color :" + self.__color + "and filled is " + str(self.__filled)
    
class Triangle(GeometricObject):
    def __init__(self, side1 = 1, side2 = 1, side3 = 1):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        
    def getSide1(self):
        return self.__side1
    
    def getSide2(self):
        return self.__side2
    
    def getSide3(self):
        return self.__side3
    
    def setSide1(self, side1):
        self.__side1 = side1
        
    def setSide2(self, side2):
        self.__side2 = side2
        
    def setSide3(self, side3):
        self.__side3 = side3
        
    def getArea(self):
        if self.__side1 + self.__side2 > self.__side3 \
        and self.__side2 + self.__side3 > self.__side1 \
        and self.__side3 + self.__side1 > self.__side2 :
            s = (self.__side1 + self.__side2 + self.__side3) / 2
            area = (s*(s - self.__side1)*(s - self.__side2)*(s - self.__side3))**0.5
            return area
        else:
            raise TriangleError(self.__side1, self.__side2, self.__side3)
    
    def getPerimeter(self):
        
        perimeter = (self.__side1 + self.__side2 + self.__side3)
        return perimeter
    
    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3)

class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        
    def getSide1(self):
        return self.__side1
    
    def getSide2(self):
        return self.__side2
    
    def getSide3(self):
        return self.__side3

        
try:
    triangle = Triangle()
    print(triangle.getArea())  
    
except TriangleError as ex:
    print("Sides don't make triangle.")
    

