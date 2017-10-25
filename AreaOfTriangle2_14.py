# Calculate area of a triangle given 3 vertices

x1, y1 = eval(input("Enter first point of the triangle : "))
x2, y2 = eval(input("Enter second point of the triangle : "))
x3, y3 = eval(input("Enter third point of the triangle : "))

side_1 = ((x1-x2)**2 + (y1-y2)**2)**0.5
side_2 = ((x2-x3)**2 + (y2-y3)**2)**0.5
side_3 = ((x3-x1)**2 + (y3-y1)**2)**0.5

if(((side_1 + side_2) <= side_3) or ((side_2 + side_3) <= side_1) or ((side_3 + side_1) <= side_2)):
    print("The entered points do not make a triangle.")
    
else:
    s = (side_1 + side_2 + side_3)/2

    area = (s*(s-side_1)*(s-side_2)*(s-side_3))**0.5

    print("The lengths of the 3 sides of the triangle are : ",round(side_1,2),", ",round(side_2,2),", ",round(side_3,2),
          " and it's area is : ",round(area,2))