# Solve 2 x 2 linear equation 

a = eval(input("Enter value of a : "))
b = eval(input("Enter value of b : "))
c = eval(input("Enter value of c : "))
d = eval(input("Enter value of d : "))
e = eval(input("Enter value of e : "))
f = eval(input("Enter value of f : "))

if ((a*d - b*c) == 0) :
    print("The equations have no solution.")
    
else :
    
    x = ((e * d) - (b * f)) / ((a * d) - (b * c))
    y = ((a * f) - (e * c)) / ((a * d) - (b * c))
    
    print("The system of equations has the following solution : \n x = ",x,", y = ",y)
    