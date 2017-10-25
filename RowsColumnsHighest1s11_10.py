import random


def getRandomMatrix(r,c):
    matrix = []
    noOfRows = r
    noOfColums = c
    
    for i in range(r):
        row = []
        for j in range(c):
            value = random.randint(0,1)
            row.append(value)
        matrix.append(row)
    for i in matrix:
        print(i)
    return matrix

def highRow(matrix):
    countList = []
    for row in matrix:
        countList.append(row.count(1))
    print("list with number of 1s per row = ",countList)
    highestRow = countList.index(max(countList))
    print("first row with max number of 1s is row number ",highestRow+1 )
    
def highColumn(matrix):
    countList = []
    allColumns = []
    for i in range(0,len(matrix)):
        column = []
        for j in range(0, len(matrix[i])):
            column.append(matrix[j][i])
        allColumns.append(column)
    #print("Transpose Matrix is :")
    #for i in allColumns:
     #   print(i)
        
    for row in allColumns:
        countList.append(row.count(1))
    print("list with number os rows per column is ",countList)
    highestColumn = countList.index(max(countList))
    print("first column with max number of 1s is column number ",highestColumn+1 )    

    

'''def highRow(matrix):
    countList = []
    high = 0
    
    for i in range(len(matrix)):
        count = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                count += 1
            
        countList.append(count)
        print(countList)
    high = max(countList)
    print("high = ", high)
    highRow = countList.index(high)
    print(highRow)
    return highRow'''
        

m = getRandomMatrix(4,4)
highRow(m)
highColumn(m)


    
    