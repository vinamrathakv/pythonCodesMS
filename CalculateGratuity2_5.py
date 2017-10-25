#Calculate tips and total amount from sub-total

st, g_rate = eval(input("Enter Sub-Total and Gratuity Rate : ")) #get user input for sub total and gratuity rate

gratuity = st * ((g_rate)/100)                                  # Calculate gratuity as percentage of sub total
total = st + gratuity

print ("The Gratuity is ",round(gratuity,2),"and the total is ",round(total,2))
