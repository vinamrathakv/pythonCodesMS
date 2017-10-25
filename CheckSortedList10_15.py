# check if input list is sorted in ascending order_comparisons

def isSorted(lst):
    sort_asc = True
    for i in range(0, len(lst) - 1):
        if lst[i] <= lst[i+1]:
            continue
        else:
            sort_asc = False
            
    if sort_asc == True:
        print("List is sorted in ascending order")
        
    else:
        print("List is not sorted in ascending order")
        
def main():
    lst = []
    item = eval(input("Enter numbers in the list. Enter -9999 to stop input. Press Enter after each number :"))
    
    while item != -9999:
        lst.append(item)
        item = eval(input("Enter numbers in the list. Enter -9999 to stop input. Press Enter after each number :"))
        
    isSorted(lst)
    
main()