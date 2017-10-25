#Display first day of each month of the year after taking user input for year and first day of the year.

print("Monday = 1\nTuesday = 2\nWednesday =3\nThursday = 4\nFriday =5\nSaturday = 6\nSunday = 0")
year = eval(input("Enter the year :")) 
firstDay = eval(input("Enter first day of the year using the above digit equivalents : "))


    
jan1 = firstDay
feb1 = jan1 + 31
mar1 = feb1 + 28
apr1 = mar1 + 31
may1 = apr1 + 30
jun1 = may1 + 31
jul1 = jun1 + 30
aug1 = jul1 + 31
sep1 = aug1 + 31
oct1 = sep1 + 30
nov1 = oct1 + 31
dec1 = nov1 + 30
    
if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    print("Year is a leap year.")
    mar1 = feb1 + 29
    
else:
    print("Year is not a leap year.")
    #mar1 = feb1 + 28
    
day = ((firstDay) % 7)
    
if(day == 1):
    dayOfWeek = "Monday"
    
elif(day == 2):
    dayOfWeek = "Tuesday"
        
elif(day == 3):
    dayOfWeek = "Wednesday"
        
elif(day == 4):
    dayOfWeek = "Thursday"
        
elif(day == 5):
    dayOfWeek = "Friday"
        
elif(day == 6):
    dayOfWeek = "Saturday"
        
elif(day == 0):
    dayOfWeek = "Sunday"
    
print("January 1st, ",year," is ",dayOfWeek)
    
day = ((firstDay + feb1) % 7)
    
if(day == 1):
    dayOfWeek = "Monday"
    
elif(day == 2):
    dayOfWeek = "Tuesday"
        
elif(day == 3):
    dayOfWeek = "Wednesday"
        
elif(day == 4):
    dayOfWeek = "Thursday"
        
elif(day == 5):
    dayOfWeek = "Friday"
        
elif(day == 6):
    dayOfWeek = "Saturday"
        
elif(day == 7):
    dayOfWeek = "Sunday"
    
print("February 1st, ",year," is ",dayOfWeek)
    
day = ((firstDay + mar1) % 7)
    
if(day == 1):
    dayOfWeek = "Monday"
    
elif(day == 2):
    dayOfWeek = "Tuesday"
        
elif(day == 3):
    dayOfWeek = "Wednesday"
        
elif(day == 4):
    dayOfWeek = "Thursday"
        
elif(day == 5):
    dayOfWeek = "Friday"
        
elif(day == 6):
    dayOfWeek = "Saturday"
        
elif(day == 7):
    dayOfWeek = "Sunday"
    
print("March 1st, ",year," is ",dayOfWeek)
    
day = ((firstDay + apr1) % 7)
    
if(day == 1):
    dayOfWeek = "Monday"
    
elif(day == 2):
    dayOfWeek = "Tuesday"
        
elif(day == 3):
    dayOfWeek = "Wednesday"
        
elif(day == 4):
    dayOfWeek = "Thursday"
        
elif(day == 5):
    dayOfWeek = "Friday"
        
elif(day == 6):
    dayOfWeek = "Saturday"
        
elif(day == 7):
    dayOfWeek = "Sunday"
    
print("April 1st, ",year," is ",dayOfWeek)
    
day = ((firstDay + may1) % 7)
    
if(day == 1):
    dayOfWeek = "Monday"
    
elif(day == 2):
    dayOfWeek = "Tuesday"
        
elif(day == 3):
    dayOfWeek = "Wednesday"
        
elif(day == 4):
    dayOfWeek = "Thursday"
        
elif(day == 5):
    dayOfWeek = "Friday"
        
elif(day == 6):
    dayOfWeek = "Saturday"
        
elif(day == 7):
    dayOfWeek = "Sunday"
    
print("May 1st, ",year," is ",dayOfWeek)
    
day = ((firstDay + jun1) % 7)
    
if(day == 1):
    dayOfWeek = "Monday"
    
elif(day == 2):
    dayOfWeek = "Tuesday"
        
elif(day == 3):
    dayOfWeek = "Wednesday"
        
elif(day == 4):
    dayOfWeek = "Thursday"
        
elif(day == 5):
    dayOfWeek = "Friday"
        
elif(day == 6):
    dayOfWeek = "Saturday"
        
elif(day == 7):
    dayOfWeek = "Sunday"
    
print("June 1st, ",year," is ",dayOfWeek)
    
day = ((firstDay + jul1) % 7)
    
if(day == 1):
    dayOfWeek = "Monday"
    
elif(day == 2):
    dayOfWeek = "Tuesday"
        
elif(day == 3):
    dayOfWeek = "Wednesday"
        
elif(day == 4):
    dayOfWeek = "Thursday"
        
elif(day == 5):
    dayOfWeek = "Friday"
        
elif(day == 6):
    dayOfWeek = "Saturday"
        
elif(day == 7):
    dayOfWeek = "Sunday"
    
print("July 1st, ",year," is ",dayOfWeek)
    
day = ((firstDay + aug1) % 7)
    
if(day == 1):
    dayOfWeek = "Monday"
    
elif(day == 2):
        dayOfWeek = "Tuesday"
        
elif(day == 3):
    dayOfWeek = "Wednesday"
        
elif(day == 4):
    dayOfWeek = "Thursday"
        
elif(day == 5):
    dayOfWeek = "Friday"
        
elif(day == 6):
    dayOfWeek = "Saturday"
        
elif(day == 7):
    dayOfWeek = "Sunday"
    
print("August 1st, ",year," is ",dayOfWeek)
    
day = ((firstDay + sep1) % 7)
    
if(day == 1):
    dayOfWeek = "Monday"
    
elif(day == 2):
    dayOfWeek = "Tuesday"
        
elif(day == 3):
    dayOfWeek = "Wednesday"
        
elif(day == 4):
    dayOfWeek = "Thursday"
        
elif(day == 5):
    dayOfWeek = "Friday"
        
elif(day == 6):
    dayOfWeek = "Saturday"
        
elif(day == 7):
    dayOfWeek = "Sunday"
    
print("September 1st, ",year," is ",dayOfWeek)
    
day = ((firstDay + oct1) % 7)
    
if(day == 1):
    dayOfWeek = "Monday"
    
elif(day == 2):
    dayOfWeek = "Tuesday"
        
elif(day == 3):
    dayOfWeek = "Wednesday"
        
elif(day == 4):
    dayOfWeek = "Thursday"
        
elif(day == 5):
    dayOfWeek = "Friday"
        
elif(day == 6):
    dayOfWeek = "Saturday"
        
elif(day == 7):
    dayOfWeek = "Sunday"
    
print("October 1st, ",year," is ",dayOfWeek)
    
day = ((firstDay + nov1) % 7)
    
if(day == 1):
    dayOfWeek = "Monday"
    
elif(day == 2):
    dayOfWeek = "Tuesday"
        
elif(day == 3):
    dayOfWeek = "Wednesday"
        
elif(day == 4):
    dayOfWeek = "Thursday"
        
elif(day == 5):
    dayOfWeek = "Friday"
        
elif(day == 6):
    dayOfWeek = "Saturday"
        
elif(day == 7):
    dayOfWeek = "Sunday"
    
print("November 1st, ",year," is ",dayOfWeek)
    
day = ((firstDay + dec1) % 7)
    
if(day == 1):
    dayOfWeek = "Monday"
    
elif(day == 2):
    dayOfWeek = "Tuesday"
        
elif(day == 3):
    dayOfWeek = "Wednesday"
        
elif(day == 4):
    dayOfWeek = "Thursday"
        
elif(day == 5):
    dayOfWeek = "Friday"
        
elif(day == 6):
    dayOfWeek = "Saturday"
        
elif(day == 7):
    dayOfWeek = "Sunday"
    
print("December 1st, ",year," is ",dayOfWeek)
    
    
    
    
    
    
    
    
    
