'''Write a test
program that prompts the user to enter a, b, c, d, e, and f and displays the result.
If is 0, report that The equation has no solution.'''


class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d 
        self.__e = e 
        self.__f = f 
        
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getD(self):
        return self.__d
    
    def getE(self):
        return self.__e
    
    def getF(self):
        return self.__f
    
    def isSolvable(self):
        if(self.__a * self.__d) - (self.__b * self.__c) != 0:
            return True
        
        else:
            print("Equation is not solvable.")
            return False
        
    def getX(self):
        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
    
    def getY(self):
        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
    
def main():
    
    
    a = eval(input("Enter a :"))
    b = eval(input("Enter b :"))
    c = eval(input("Enter c :"))
    d = eval(input("Enter d :"))
    e = eval(input("Enter e :"))
    f = eval(input("Enter f :"))
    
    eqn1 = LinearEquation(a,b,c,d,e,f)
    
    
    
    if eqn1.isSolvable() == True:
        print("x = ",eqn1.getX())
        print("y = ",eqn1.getY())
        
    else:
        print("Equation has no solutions")
        
main()

    
    