# Calculate and display account value after 6 months

x = eval(input("Enter monthly deposit amount :"))   #User input for monthly deposit
monthly_rate = .00417                               #5% divided by 12 months
total = 0

for i in range(1,7):
    total = ((total + x) * (1 + monthly_rate))
    #print("After ",i," months: ",(round(total,2))
    i += 1
    
print("Balance after 6 months : ",round(total,2))