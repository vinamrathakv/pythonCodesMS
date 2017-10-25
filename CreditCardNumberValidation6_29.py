#Validate credit card number using Luhn Check

def sumOfDoubleEvenPlace(n):
#n = 1234367864
    sum = 0
    while(n>1):
        
        digit = n%10
        n = n//10
        evenDigit = n%10
        twiceEvenDigit = 2 * evenDigit
        requiredDigit = getDigit(twiceEvenDigit)
                
        #print(twiceEvenDigit)
    
        sum += requiredDigit
        n = (n // 10)
    return sum

#sumOfDoubleEvenPlace(4567890871)

def getDigit(n):
    
    if(n <= 9):
        return n
    
    else:
        return (n-9)
    
    
def sumOfOddPlace(n):
    sum = 0
    while(n > 1):
        
    
        oddDigit = n%10
        #print(oddDigit)
        evenDigit = (n//10)%10
    
        sum += oddDigit
        n = (n // 10) // 10
    return sum
    
    
    
#sumOfOddPlace(4566889954320)

def isValid(n):
    
    if ((sumOfDoubleEvenPlace(n) + sumOfOddPlace(n)) % 10 == 0):
        return True
    else:
        return False
    
def getPrefix(number, k):
    if (getSize(number) < k):
        return number
    else:
        for i in range(0, (getSize(number))-k):
            number = number // 10 
            i += 1
           
        return number
    
def getSize(d):
    return len(str(d))

def prefixMatched(number, d):
    if(getPrefix(number, d) == 4):
        print("Visa Card")
        
    elif(getPrefix(number, d) == 5):
        print("Master Card")
        
    elif(getPrefix(number, d) == 6):
        print("Discover Card")
        
    elif(getPrefix(number, d) == 37):
        print("American Expess Card")
        
    else:
        print("Invalid Card number")
        
card_number = eval(input("Enter the credit card number : "))

if (len(str(card_number)) >= 13 and len(str(card_number)) <= 16):
    if(isValid(card_number) == True):
        if(getPrefix(card_number,1) == 4):               
            print("Valid Visa card number")
            
        elif(getPrefix(card_number,1) == 5):
            print("Valid Master card number")
            
        elif(getPrefix(card_number,1) == 6):
            print("Valid Discover card number")
            
        elif(getPrefix(card_number,2) == 37):
            print("Valid Aerican Express card number")
            
        else:
            print("Invalid Card number")
            
    else:
        print("invalid")
        
else:
    print("invalid")
            
    
        
        
        
    
        
    
    
    
    