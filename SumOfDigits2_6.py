#Calculate sum of digits in an integer 

num = eval(input("Enter an integer between 0 and 1000 : "))

sum = 0
digit = 0

if(num < 0 or num > 1000):                          #check if input is within 0 and 1000
    print("The entered number is out of range.")
    
elif(isinstance(num,int) == False):                 #check if input is integer only
    print("you have to enter integer value only")
    
else:
    while (num != 0):
    
        sum += num % 10
        num = num // 10
        
    print("sum of digits is : ", sum)