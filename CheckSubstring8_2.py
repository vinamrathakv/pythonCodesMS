#Check if first string is a substring of second string

def find(string, subStr) :
    
    if subStr in string :                   #use in keyword to see if the first string is in the second string
        return True
    else:
         return False
     
def main():
    
    subStr = input("Enter first string : ")
    string = input("Enter second string : ")
    
    if find(string, subStr):
        print(subStr + " is a substring of " + string)    
        
    else:
        print(subStr + " is not a substring of " + string)
        
main()
        
    