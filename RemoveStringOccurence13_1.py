fileName = input("Enter filename to open : ")
file = open(fileName, "r")
fileData = file.read()

string = input("Enter string to be removed : ")
newFileData = fileData.replace(string, '')

file = open(fileName, "w")
file.write(newFileData)

file.close()
