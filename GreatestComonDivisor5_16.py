#Calculate GCD

n1, n2 = eval(input("Enter 2 numbers : "))

if (n1 < n2):
    gcd = n1
else:
     gcd = n2

while(gcd > 1):
    

    if(n1 % gcd == 0 and n2 % gcd == 0) :
        print("Greatest Common Divisor is : ",gcd)
        break
    else :
        gcd = gcd-1
        if(gcd == 1):
            print("GCD is 1")
        

