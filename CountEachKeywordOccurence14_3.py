import os
import sys


# create a dictionary with key as all the keywords and initialize all keys to 0

keywords = {"and" : 0, "as" : 0, "assert" : 0, "break" : 0, "class" : 0,
            "continue": 0, "def" : 0, "del" : 0, "elif" : 0, "else" : 0,
            "except" : 0, "False" : 0, "finally" : 0, "for" : 0, "from" : 0,
            "global" : 0, "if" : 0, "import" : 0, "in" : 0, "is" : 0, "lambda" : 0,
            "None" : 0, "nonlocal" : 0, "not" : 0, "or" : 0, "pass" : 0, "raise" : 0,
            "return" : 0, "True" : 0, "try" : 0, "while" : 0, "with" : 0, "yield" : 0}

fileName = input("Enter Python source file name : ")

if not os.path.isfile(fileName):
    print("File does not exist.")
    sys.exit()
   
file = open(fileName, "r")
fileData = file.read().split()
count = 0

for i in fileData:
    if i in keywords:
        if keywords[i] == 0:
            count += 1
        keywords[i] += 1
if count == 0:
    print("File contains no keywords.")

print("Number of different keywords : ", count)    
for i in keywords:
    if keywords[i] > 0:
        print(i, keywords[i])
        


