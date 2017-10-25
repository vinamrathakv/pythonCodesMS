#recursive sum of digits

def sumDigits(n):
    if n == 0:
        return n
    else:
        return(n%10 + sumDigits(n//10))
       
    


number = eval(input("Enter a positive integer : "))
print("Sum of digits is : ", sumDigits(number))