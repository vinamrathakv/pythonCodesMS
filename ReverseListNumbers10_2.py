# Reverse the list and display_path

list1 = []

item = eval(input("Enter item :"))
while (item != 0):
    list1.append(item)
    item = eval(input("Enter item. Enter 0 to stop entering"))
    
print(list1)

rev_list =[]
for i in range(0, len(list1)):
  #print(list1[len(list1)-i-1])
  n = list1[len(list1)-i-1]
  rev_list.append(n)
  
print(rev_list)
    

