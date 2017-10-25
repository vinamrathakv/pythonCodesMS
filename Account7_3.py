#Write a test program that creates an Account object with an account id of 1122, a
#balance of $20,000, and an annual interest rate of 4.5%. Use the withdraw
#method to withdraw $2,500, use the deposit method to deposit $3,000, and print
#the id, balance, monthly interest rate, and monthly interest.

class Account:
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
        
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
        
    def getBalance(self):
        return self.__balance
    
    def setBalance(self, balance):
        self.__balance = balance
        
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
        
    def getMonthlyInterestRate(self):                           #calculate monthly interest rate
        monthlyInterestRate = self.__annualInterestRate / 12
        return monthlyInterestRate
    
    def getMonthlyInterest(self):                               #calculate monthly interest
        monthlyInterest = (self.__balance * self.getMonthlyInterestRate()) / 100
        return monthlyInterest
    
    def withdraw(self, amount):
        self.__balance -= amount
        print("Balance after withdrawal of ",amount," is : $", self.__balance)
        
    def deposit(self, amount):
        self.__balance += amount
        print("Balance after deposit of ",amount," is : $", self.__balance)
        
def main():

    account = Account(1122, 20000, 4.5)

    account.withdraw(2500)
    account.deposit(3000)

    print("Account ID : ",account.getId())
    print("Account Balance: $",account.getBalance())
    print("Monthly Interest Rate : ", account.getMonthlyInterestRate(),"%")
    print("Monthly Interest : $",account.getMonthlyInterest())   
    
main() 
    
    
        
    
        
