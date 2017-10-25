def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        leftLst = lst[:mid]
        rightLst = lst[mid:]
        print(leftLst)
        print(rightLst)
        
        mergeSort(leftLst)
        print(leftLst)
        mergeSort(rightLst)
        print(rightLst)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(leftLst) and j < len(rightLst):
            if leftLst[i] < rightLst [j]:
                lst[k] = leftLst[i]
                i += 1
                
                
            else:
                lst[k] = rightLst[j]
                j += 1
                
            k += 1
            
        while i < len(leftLst):
            lst[k] = leftLst[i]
            i += 1
            k = k + 1
            
        while j < len(rightLst):
            lst[k] = rightLst[j]
            j += 1
            k +=1
            
    return lst
            
def main():
    lst = [3, 2, 1, 5, 4, 7, 9, 8, 6, 0, 20, 10]
    print(mergeSort(lst))
    
    
main()
                                
            
            
            
            
    

