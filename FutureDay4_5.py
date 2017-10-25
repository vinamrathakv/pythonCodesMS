# Calculate future day based on number of days elapsed from today


print("Sunday : 0  Monday : 1  Tuesday : 2  Wednesday : 3  Thursday : 4  Friday : 5  Saturday : 6")
today = eval(input("Enter number for today's day : "))

if (today >= 0 and today <= 6):
   
    daysElapsed = eval(input("Enter number of days elapsed from today : "))

    futureDay = (daysElapsed + today) % 7

    if futureDay == 0:
        print(daysElapsed," days from today is : Sunday")
    
    elif futureDay == 1:
        print(daysElapsed," days from today is : Monday")
    
    elif futureDay == 2:
        print(daysElapsed," days from today is : Tuesday")
    
    elif futureDay == 3:
        print(daysElapsed," days from today is : Wednesday")
    
    elif futureDay == 4:
        print(daysElapsed," days from today is : Thursday")
    
    elif futureDay == 5:
        print(daysElapsed," days from today is : Friday")
    
    elif futureDay == 6:
        print(daysElapsed," days from today is : Saturday")
        
else :
    print("Enter valid number for today (between 0 and 6)")



