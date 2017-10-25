#Find day of the week using Zeller's congruence
import sys

year = eval(input("Enter the year : "))
m = eval(input("Enter the month[1-12] :"))
if m < 1 or m > 12:
    print("Invalid month.")
    sys.exit()

if(m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) :
    q = eval(input("Enter the date of the month[1-31] : "))
    if q <1 or q > 31:
        print("Invalid date")
        sys.exit()
    
elif(m == 2):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        q =  eval(input("Leap year. Enter the date of the month[1-29] : "))
        if q < 1 or q > 29:
            print("Invalid date")
            sys.exit()
    
    else:
        q =  eval(input("Enter the date of the month[1-28] : "))
        if q < 1 or q > 28:
            print("Invalid date.")
            sys.exit()
            
elif((m == 4 or m == 6 or m == 9 or m == 11 )):
    q =  eval(input("Enter the date of the month[1-30] : "))
    if q < 1 or q > 30:
            print("Invalid date.")
            sys.exit()
    
if(m == 1 or m == 2):
    m += 12
    year -= 1
    
j = year // 100
k = year % 100


h = (q + (26 * (m+1) // 10) + k + (k // 4) + (j // 4) + 5 * j) % 7

if h == 0:
    print("Day of the week is Saturday")
    
elif h == 1:
    print("Day of the week is Sunday")
    
elif h == 2:
    print("Day of the week is Monday")
    
elif h == 3:
    print("Day of the week is Tuesday")
    
elif h == 4:
    print("Day of the week is Wednesday")
    
elif h == 5:
    print("Day of the week is Thursday")
    
elif h == 6:
    print("Day of the week is Friday")