fileName = input("Enter the file to open : ")
file = open(fileName, "r")
fileData = file.readlines()

numLines = len(fileData)
print ("File has " + str(numLines) + " lines" )

file.close()

file = open(fileName, "r")
fileData = file.read()
numChars = len(fileData)
print("File has ", numChars, " characters.")
numWords = fileData.split()
print(numWords)
print("File has " + str(len(numWords)) + "words.")


