#display the reverse of a 4 digit integer 

x = eval(input("Enter a 4 digit integer : "))
if(x < 1000 or x > 9999):
    print("Integer not in range.")
    
else:
    a = x % 10
    b = (x // 10) % 10
    c = (x//100) % 10
    d = (x // 1000)

    print("The reverse is :",a,b,c,d)
    print("The integer in reverse is : ",(a*1000)+(b*100)+(c*10)+d)