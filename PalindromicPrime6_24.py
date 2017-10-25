#check if entered integer is palindromic prime

#check if input is prime
def isPrime(number):
   
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False # number is not a prime
        divisor += 1
    return True # number is prime
            
#check if input is a palindrome
def isPalindrome(number):
    n = number
    count = len(str(number))
    rev_number = 0
    while(n > 0):
        digit = n % 10
        rev_number += digit * (10 ** (count-1))
        n = n // 10
        count -= 1
        
    if (rev_number == number):
        #print(rev_number, number)
        return True
    
    else:
        #print(rev_number,number)
        return False
    
    
count = 0
number = 2
i = 0

while count <100:
    if isPrime(number):
        if isPalindrome(number):
            print(format(number, "5d"), end = " ")
            i += 1
            if i == 10:
                print()
                i = 0
            number += 1
            count += 1
            
        
        else:
            number += 1
    else:
        number += 1
        
    
    
'''print(isPalindrome(232))
print(isPrime(13111379))            
user_input = eval(input("Enter any integer to be checked : "))

if(isPrime(user_input) == True):
    #print("Integer is Prime.")
    
    if(isPalindrome(user_input) == True):
        print("Integer is Palindromic Prime")
    else:
        print("Integer is Prime but not a Palindrome")
        
else : 
    print("Integer is neither Prime nor a Palindrome.")'''
        