# check if matrix is Markov Matrix

def getMatrix(r,c):
    matrix = []
    for i in range(r):
        row = []
        for j in range(c):
            value = eval(input("Enter a values and press enter "))
            row.append(value)
        matrix.append(row)
    for i in matrix:
        print(i)
    return matrix

def isMarkov(matrix):
    columnSum = 0
    count = 0
    for i in range(len(matrix)):
        columnSum = 0
        for j in range(len(matrix[i])):
            
            if matrix[i][j] < 0:
                print ("not markov")
                break
            else:
                columnSum += matrix[j][i]
                print(columnSum)
                continue
        if columnSum == 1:
            count += 1
                
            continue
        else:
            print("not markov")
            break
        
    if count == len(matrix):
        print("The Matrix is a Markov matrix")
    else:
        print("Not Markov")

m = getMatrix(3,3)
isMarkov(m)
                
                
    