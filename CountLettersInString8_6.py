# Count number of letter in a string

def countLetters(string):
    count = 0
    for c in string:
        if c.isalpha():
            count += 1
            
        else:
            continue
        
    return count

def main():
    
    string =  input("Enter input string : ")
    
    print("there are ", countLetters(string), "number of letters in ",string)
    
main()
        