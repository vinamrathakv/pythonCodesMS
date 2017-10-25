#print n x n matrix. n is obtained from user
import random

def printMatrix(n):
    element = 0
    for i in range(0,n):        #n rows
        for j in range(0,n):    #n columns
            element = random.randint(0,1)
            print(element, end = " ")
            
        print("\n")
        
n = eval(input("Enter n :"))
printMatrix(n)