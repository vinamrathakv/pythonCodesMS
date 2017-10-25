# add two matrices

def getMatrix(r,c):
    matrix = []
    
    noOfRows = r
    noOfColumns = c
    
    for row in range(0, noOfRows):
        matrix.append([])
        for column in range(0, noOfColumns):
            value = eval(input("Enter an element and press Enter : "))
            matrix[row].append(value)
            
    for i in matrix:
        print(i)
            
    return matrix

def addMatrix(m, n):
    s = []
    
    for i in range(0, len(m)):
        row = []
        for j in range(0, len(m[0])):
            
            print(len(m[i]))
            s[i][j] = m[i][j] + n[i][j] 
            row.append(s[i][j])
        s.append(row)
    print (s[i][j])
            
    print(s)
    return s
    
m = getMatrix(2,2)
n = getMatrix(2,2)

s = addMatrix(m, n)
            
        
    
            
            
    
    