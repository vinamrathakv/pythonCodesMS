# Calculate area enclosed between 4 cities
import math

xc, yc = 35.2270869, -80.8431267            #co-ordinates of Charolette
xs, ys = 32.0835407, -81.0998342            #co-ordinates of Savannah
xo, yo = 28.5383355, -81.3792365            #co-ordinates of Orlando
xa, ya = 33.7489954, -843879824             #co-ordinates of Atlanta

cs = math.sqrt((xs-xc)**2 + (ys-yc)**2)     #distance between Charolette and Savannah
so = math.sqrt((xo-xs)**2 + (yo-ys)**2)     #distance between Savannah and Orlando
oa = math.sqrt((xa-xo)**2 + (ya-yo)**2)     #distance between Orlando and Atlanta
ac = math.sqrt((xc-xa)**2 + (yc-ya)**2)     #distance between Atlanta and Charolette
sa = math.sqrt((xs-xa)**2 + (ys-ya)**2)     #distance between Savannah and Atlanta

s1 = (ac + cs + sa)/2
area1 = math.sqrt(s1*(s1-ac)*(s1-cs)-(s1-sa))   #Area of triangle made of Atlanta, Charolette, Savannah

s2 = (so + oa + sa)/2
area2 = math.sqrt(s2*(s2-so)*(s2-oa)*(s2-sa))   #Area of triangle made of Savannah, Orlando and Atlanta

print("Area enclosed between Atlanta, Charolette, Savannah and Orlando is : ",area1+area2)
