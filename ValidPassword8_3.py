# Check validity of PasswordProtectedSiteTestCase

def isValid(string):
    num = 0    
    if len(string) >= 8:
        if string.isalnum():
            for ch in string:
                if ch.isnumeric():
                    num += 1
                    
                else:
                    continue
                    
            if num >= 2:
                print("Password is valid")
            else:
                print("Invalid Password. Must contain atleast 2 digits")
                    
        else:
            print("Invalid password. Should not contain special characters or whitespace.")
            
    else:
        print("Invalid Password. Should contain at least 8 characters") 
        
def main():
    
    password = input("Enter password : ")
    
    isValid(password)  
    
    
main()
        