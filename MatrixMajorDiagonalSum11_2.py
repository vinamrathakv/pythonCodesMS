#Get sum of majjor diagonal of 4 x 4 matrix

def getMatrix(r, c):
    matrix = [] # Create an empty list

    numberOfRows = r
    numberOfColumns = c

    for row in range(numberOfRows):
        matrix.append([]) # Add an empty new row
        for column in range(numberOfColumns):
            value = eval(input("Enter an element and press Enter: "))
            matrix[row].append(value)
    for i in matrix:
        print(i)
    return matrix

def getMajorDiagonalSum(matrix):
     
    
    total = 0
    
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[row])):
            if row == column:
                total += matrix[row][column]
                
    print(total)
    
m = getMatrix(4,4)
getMajorDiagonalSum(m)
                
    
    