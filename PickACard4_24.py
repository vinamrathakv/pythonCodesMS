#Display rank and suit of the card picked

import random

card = random.randint(0,51)

rank = card // 4
suit = card % 4

if ((card // 4) == 0):
    rank = "Ace"
    
elif ((card // 4) == 1):
    rank = "2"
    
elif ((card // 4) == 2):
    rank = "3"
    
elif ((card // 4) == 3):
    rank = "4"
    
elif ((card // 4) == 4):
    rank = "5"
    
elif ((card // 4) == 5):
    rank = "6"
    
elif ((card // 4) == 6):
    rank = "7"
    
elif ((card // 4) == 7):
    rank = "8"
    
elif ((card // 4) == 8):
    rank = "9"
    
elif ((card // 4) == 9):
    rank = "10"
    
elif ((card // 4) == 10):
    rank = "Jack"
    
elif ((card // 4) == 11):
    rank = "Queen"
    
elif ((card // 4) == 12):
    rank = "King"
    
if ((card) % 4 == 0):
    suit = "Spades"
    
elif ((card % 4) == 1):
    suit = "Hearts"
    
elif ((card % 4) == 2):
    suit = "Diamonds"
    
elif ((card % 4) == 3):
    suit = "Clubs"
    
print(" You have picked ", rank, "of",suit)
    