# Calculate future tuition and tuition for 4 years 10 years from now


tuition = 10000
total = 0

for year in range(1,14):
   
    tuition = tuition * 1.05
    print(tuition)
    if (year == 10):
        print("Tuition in ten years will be : $",round(tuition,2))
        total = tuition
        
    elif(year > 10):
        total += tuition
        
print("Total tuition for 4 years, 10 years from now will be : $",round(total,2))
        
    