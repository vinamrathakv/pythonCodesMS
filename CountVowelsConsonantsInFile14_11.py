# count vowels and consonants in file
vowels = {"a", "e", "i", "o", "u"}

fileName = input("Enter filename to count vowels and consonants : ")
file = open(fileName, "r")
fileData = file.read()
print(len(fileData))

v = 0
c = 0

for i in fileData:
    i.lower()
    if i in vowels:
        v += 1
    else:
        c +=1
print("vowels : ",v)
print("consonants : ",c )
    