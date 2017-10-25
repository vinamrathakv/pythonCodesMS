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

def multiplyTwoMatrices(m, n):
    
    z = []
    for i in range(len(m)):
        row = []
        for j in range(len(m[i])):
            row.append(m[i][0] * n[0][i] + m[i][1]*n[1][i] + m[i][2]*n[2][i])
        z.append(row)
    print(z)
        
m = getMatrix(3,3)
n = getMatrix(3,3)

z = multiplyTwoMatrices(m, n)        