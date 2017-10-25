#Display number pyramid

n = eval(input("Enter an integer between 1 and 15 : "))

if(n>0 and n<16):
    

    for i in range(1, n+1):
        for j in range(n-i ,0, -1):
            print("   ", end ="")
            
        for j in range (i, 0, -1):
            
            print(format(j, "2d"), end = " ")
        for j in range(2, i+1):
            print(format(j, "2d"), end = " ")
        print("\n")
            


