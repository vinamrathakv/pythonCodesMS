# sort a list using bubble sort_attributes

def bubbleSort(lst):
        swapCount = 0
    
    #while(swapCount != 0):
        for i in range(0, len(lst) - 1):
            #print(i)                                        #check no. of iterations
            for j in range(0, len(lst) - 1):
                if lst[j] > lst[j+1]:                           #swap pair if not in ascending order
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    swapCount += 1
            
                else:
                    continue
            if swapCount == 0:
                break    
        print("Sorted list is ", lst)
    
def main():
    lst = []
    item = eval(input("Enter numbers in the list. Enter -9999 to stop input :"))
    
    while item != -9999:
        lst.append(item)
        item = eval(input("Enter numbers in the list. Enter -9999 to stop input :"))
        
    bubbleSort(lst)
    
main()