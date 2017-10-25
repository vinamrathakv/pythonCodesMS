#Play rock, paper scissors continuously until computer or user wins more than 2 times
import random

print("Lets play Rock, Paper and Scissors!!")

cWin = 0
uWin = 0

while(cWin < 3 and uWin <3):
    
    user_choice = eval(input("Enter (0) for Rock, (1) for Paper and (2) for Scissors : "))
    computer_choice = random.randint(0,2)

    if(user_choice == 0 and computer_choice == 1):
        print("You chose : Rock, Computer chose : Paper\nComputer Wins!")
        cWin += 1
        if(cWin > 2):
            print("Game Over.")
        else:
            print("Play Again.")
        
    
    elif(user_choice == 0 and computer_choice == 2):
        print("You chose : Rock, Computer chose : Scissors\nYou Win!")
        uWin += 1
        if(uWin > 2):
            print("Game Over.")
        else:
            print("Play Again.")
    
    elif(user_choice == 1 and computer_choice == 0):
        print("You chose : Paper, Computer chose : Rock\nYou Win!")
        uWin += 1
        if(uWin > 2):
            print("Game Over.")
        else:
            print("Play Again.")
    
    elif(user_choice == 1 and computer_choice == 2):
        print("You chose : Paper, Computer chose : Scissors\nComputer Wins!")
        cWin += 1
        if(cWin > 2):
            print("Game Over.")
        else:
            print("Play Again.")
    
    elif(user_choice == 2 and computer_choice == 0):
        print("You chose : Scissors, Computer chose : Rock\nComputer Wins!")
        cWin += 1
        if(cWin > 2):
            print("Game Over.")
        else:
            print("Play Again.")
    
    elif(user_choice == 2 and computer_choice == 1):
        print("You chose : Scissors, Computer chose : Paper\nYou Win!")
        uWin += 1
        if(uWin > 2):
            print("Game Over.")
        else:
            print("Play Again.")
        
    else :
        print("You and Computer chose the same item. Play Again")
    print("Current score : Computer ",cWin," You ",uWin)    
    print("\n")
    