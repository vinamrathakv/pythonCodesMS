#Calculate winnings as per user entry
import random
winningLottery = random.randint(100,999)
#print(winningLottery)

#get the 3 digits of winning lottery

winningDigit3 = winningLottery % 10
winningDigit2 = (winningLottery // 10) % 10
winningDigit1 = winningLottery // 100

userLottery = eval(input("Enter a 3 digit lottery number : "))

#get 3 digits of user lottery

userDigit3 = userLottery % 10
userDigit2 = (userLottery // 10) % 10
userDigit1 = userLottery // 100

if userLottery == winningLottery :
    print("Congratulations! You have an exact match. You win $10,000.00")
    
#check if all 3 digits match
    
elif ((userDigit1 == winningDigit1 or userDigit1 == winningDigit2 or userDigit1 == winningDigit3) \
      and (userDigit2 == winningDigit2 or userDigit2 == winningDigit1 or userDigit2 == winningDigit3) \
      and (userDigit3 == winningDigit3 or userDigit3 == winningDigit1 or userDigit3 == winningDigit2) ):
    print("The winning lottery is :",winningLottery," All 3 numbers match. You win $3000.00")
    
    #Check for match with single digit between both lotteries
     
elif (userDigit1 == winningDigit1 \
      or userDigit1 == winningDigit2 \
      or userDigit1 == winningDigit3 \
      or userDigit2 == winningDigit1 \
      or userDigit2 == winningDigit2 \
      or userDigit2 == winningDigit3 \
      or userDigit3 == winningDigit1 \
      or userDigit3 == winningDigit2 \
      or userDigit3 == winningDigit3 ):
    print("The winning lottery is :",winningLottery," You have 1 or 2 digit match. You win $1000.00")
    
    
    
else:
    print("The winning lottery number was :",winningLottery," Sorry you did not win.")


