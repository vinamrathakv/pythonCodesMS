#Calculate and display sum of series 1/3 ...... 97/99

numerator = 1
denominator = 3
total = 0

while(numerator <=97 and denominator <=99):
    total += numerator/denominator
    
    numerator += 2
    denominator += 2
    
    
print("The sum of the series 1/3 + 3/5 + 5/7 + 7/9 + .......97/99 is : ",total)
    