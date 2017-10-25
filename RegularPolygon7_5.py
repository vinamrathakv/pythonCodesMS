'''Write a test program
that creates three RegularPolygon objects, created using RegularPolygon(),
using RegularPolygon(6, 4) and RegularPolygon(10, 4, 5.6, 7.8). For
each object, display its perimeter and area.'''


import math

class RegularPolygon:
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
        
    def getNumberOfSides(self):
        return self.__n
    
    def setNumberOfSides(self, n):
        self.__n = n
        
    def getLengthOfSide(self):
        return self.__side
    
    def setLengthOfSide(self,side):
        self.__side == side
        
    def getX(self):
        return self.__x
    
    def setX(self, x):
        self.__x = x
        
    def getY(self):
        return self.__x
    
    def setY(self, y):
        self.__y = y
        
    def getPerimeter(self):
        return self.__n * self.__side

    def getArea(self):
        area = round((self.__n * self.__side) / (4 * math.tan(math.pi/self.__n)),2)
        return area
    
def main():
    
    a = RegularPolygon()
    b = RegularPolygon(6, 4)
    c = RegularPolygon(10, 4, 5.6, 7.8)
    
    print("Polygon a")
    print("Perimeter : ",a.getPerimeter())
    print("Area : ",a.getArea())
    print()
    
    print("Polygon b")    
    print("Perimeter : ",b.getPerimeter())
    print("Area : ",b.getArea())
    print()
    
    print("Polygon c")
    print("Perimeter : ",c.getPerimeter())
    print("Area : ",c.getArea())
    print()
    
main()
        
        