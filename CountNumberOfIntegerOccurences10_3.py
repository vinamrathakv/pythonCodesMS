#Count number of occurences of a number in a list


numbers = input("Enter numbers between 1 and 100 separated by space")

list = numbers.split()

length = len(list)

for i in range(0,length):
    parsed_list = list[0 : i]
    if list[i] in parsed_list:
        continue
    
    else:
        count = list.count(list[i])
        if count == 1:
            print(list[i],"occurs", count, "time")
        
        else:
            print(list[i],"occurs", count, "times")
        










'''num_list = numbers.split()

for i in range(0, len(num_list)) :
    count = 0
    number = num_list[i]
    repeat = False
    for j in range(0,i-1):
        if number != num_list[j]:
            repeat = False
            
        else:
            repeat = True
            
        if repeat == False:
           count = num_list.count(number)
           
           if count == 1:
               
               print(number, "occurs 1 time.")
                
           else:
               print(number, "occurs",count, " times")
           
        else:
            continue'''
            
            
    
        