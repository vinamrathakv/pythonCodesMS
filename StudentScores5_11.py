#Display the highest and second highest score

numberOfStudents = eval(input("Enter the number of students : "))

i = 0
high1 = 0
high2 = 0
score = 0

print("Enter each student's score :")
while (i < numberOfStudents):
    print("score", i+1, end = " ")
    score = eval(input())
    if(high1 <= score):
        high2 = high1
        high1 = score
        
    i = i+1
    
print("Highest score is : ",high1)
print("Second highest score is : ",high2)
    