def getMatrix(r,c):
    
    matrix = []
     
    for i in range(r):
        row = []
        for j in range(c):
            value = eval(input("Enter an element and press enter "))
            row.append(value)
        matrix.append(row)
    for row in matrix:
        print(row)
    return matrix
        
def getLargestElement(matrix):
    m = matrix
    print(m)
    row = []
    
    
    for i in m:
        row.extend(i)
        
    largest = max(row)
    print(largest)
    return largest
    
def getIndexLargest(matrix, largest):
    index = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == largest:
                index = [i,j]
                break
    return index
    
m = getMatrix(3,3)
largest = getLargestElement(m)   
print("Index of largest value is ",getIndexLargest(m, largest))   