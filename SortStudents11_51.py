'''(Sort students) Write a program that prompts the user to enter the students
names and their scores on one line, and prints student names in increasing order
of their scores. (Hint: Create a list. Each element in the list is a sublist with two
elements: score and name. Apply the sort method to sort the list. This will sort
the list on scores.)'''

namesScores  = input("Enter student's name and score in a line : ")
lst = namesScores.split()

scoreslist = []
[scoreslist.append(lst[i : i+2]) for i in range(0, len(lst), 2)]
    
print(scoreslist)

sortedlist = sorted(scoreslist,key=lambda x: (x[1]))

print("Sorted list on scores : ")
for i in range(len(sortedlist)):
    for j in range(len(sortedlist[i])):
        print (sortedlist[i][j], end = " ")
    print()


