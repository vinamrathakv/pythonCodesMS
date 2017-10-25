#Calculate number of years and days from just minutes

mins = eval(input("Enter the minutes : "))

mins_year = 365*24*60                       #minutes in a year

years = mins/mins_year
days = (mins%mins_year)/(24*60)


print("There are approximately ",round(years)," years and ",round(days), "days in ",mins," minutes")
