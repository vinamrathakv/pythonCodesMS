import math


class Point:
    '''Creates a point on a coordinate plane with values x and y.'''

    COUNT = 0

    def __init__(self, x = 0, y = 0):
        '''Defines x and y variables'''
        self.__x = x
        self.__y = y

    

    def __str__(self):
        return print("Point : ", self.__x, self.__y) 


    def getX(self):
        return self.__x

    def getY(self):
        return self.__y


    def isNearby(self, x1, y1):
        dx = self.__x - x1
        dy = self.__y - y1
        
        distance = math.sqrt(dx**2 + dy**2)
        print("Distance is : ", distance)
        if distance < 5 : 
            print("Points are nearby.")
        else:
            print("Points are not nearby")
        
    
def main():
    x, y = eval(input("Enter first point : "))
    p1 = Point(x,y)

    x1, y1 = eval(input("Enter second point : "))
    p1.isNearby(x1, y1)

main()
