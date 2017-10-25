# calculate mean and std deviation using lists and functions


def mean(lst):
    sum = 0
    for num in lst:
        sum += num
    mean = sum / len(lst)
    return mean

def stdDev(lst):
    
    s = 0
    avg = mean(lst)
    for num in lst:
        s += (num-avg)**2
        
    stdDeviation = (s / len(lst)-1)**0.5
    return stdDeviation

def main():
    
    #lstInput = input("Enter the nummbers in the list with space in between each number :")
    lst = []
    item = eval(input("Enter numbers in the list. Enter -9999 to stop input :"))
    
    while item != -9999:
        lst.append(item)
        item = eval(input("Enter numbers in the list. Enter -9999 to stop input :"))
        
    
    print("Mean is : ", mean(lst))
    print("Standard deviation is : ",stdDev(lst))
    
main()