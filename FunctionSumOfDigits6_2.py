#calculate sum of digits using function

def sumDigits(number):
    sum = 0
    while(number > 0):
        digit = number % 10  #extract last digit
        sum += digit
        number = number // 10 #remove last digit from the integer
    return sum
    
    
n = eval(input("enter an integer : "))
print("Sum of the digits is : ",sumDigits(n))