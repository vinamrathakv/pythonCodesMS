import urllib.request

file = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Lincoln.txt")
fileData = file.read().decode()
fileData = fileData.replace(",",'')
fileData = fileData.replace(".",'')
fileData = fileData.replace("-",'')
print(fileData)
fileList = fileData.split()

count = 0
for i in fileList:
    if i.isalpha():
        count += 1
    
print(count)

    
print(fileList)
print("Number of words : ",len(fileList))