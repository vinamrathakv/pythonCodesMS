#program to simulate ATM system
from Account7_3 import Account

accountList = []
for i in range(10):
    accountList.append(Account(id = i))
    print(accountList[i].getId())
    
ID = 0    

while ID >= 0:
    ID = eval(input("Enter Account ID : "))
    if ID not in range(10):
        print("Invalid Account ID. Try Again")
        
    else:
        print("MAIN MENU \n1: Check Balance \n2: Withdraw \n3: Deposit \n4: Exit")
        selection = eval(input("Enter corresponding number : "))
        if selection in range(1,5):
            if selection == 1:
                print(accountList[ID].getBalance())
                
            elif selection == 2:
                withdrawalAmount = eval(input("Enter withdrawal amount : "))
                accountList[ID].withdraw(withdrawalAmount)
                
            elif selection == 3:
                depositAmount = eval(input("Enter deposit amount :"))
                accountList[ID].deposit(depositAmount)
            
            else:
                continue
        
        else:
            continue
            
    
    


    
