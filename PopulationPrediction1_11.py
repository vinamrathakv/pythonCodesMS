# Population prediction for each of next 5 years

curr_pop = 312032486        #current population
secs_year1 = 31536000       #secs per year

bsecs = dsecs = isecs = 0

print("Current population is : ", curr_pop)
print()

for i in range(1,6) :
    
    b_new_secs = bsecs % 7 + 31536000   #calculate secs + left over secs from previous year
    births = b_new_secs // 7
    bsecs = b_new_secs
    
    d_new_secs = dsecs % 13 + 31536000  #calculate secs + left over secs from previous year
    deaths = d_new_secs // 13
    dsecs = d_new_secs
    
    i_new_secs = isecs % 45 + 31536000  #calculate secs + left over secs from previous year
    immis = i_new_secs // 45
    isecs = i_new_secs
    
    new_pop = curr_pop + births - deaths + immis    #population at end of year i
    
    print("Population after year ",i," is ",new_pop)
    
    curr_pop = new_pop
    i += 1
    
    

