
def reverse(number):
    count = len(str(number))
    rev_number = 0
    while(number > 0):
        digit = number % 10
        rev_number += digit * (10)**(count-1)
        count = count - 1
        number = number // 10
        
    return rev_number

def isPalindrome(number):
    if (number == reverse(number)):
        print("The integer is a palindrome.")
        
    else:
        print("The integer is not a palindrome.")

original_number = eval(input("Enter any positive integer : "))
print("Reverse is : ",reverse(original_number))
isPalindrome(original_number)



'''def sumDigits(number):
    sum = 0
    while(number > 0):
        digit = number % 10  #extract last digit
        sum += digit
        number = number // 10 #remove last digit from the integer
    return sum
    
    
n = eval(input("enter an integer : "))
print("Sum of the digits is : ",sumDigits(n))'''