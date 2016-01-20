#Rock Paper Scissors
#Corey Smith

import random

#Global Varibales to keep track of score, i know it's frowned upon to use global variables
#So I would appreciate any feeback on a better solution
playerWins = 0
comWins = 0
#Keeps track of what round it currently is
#String Constants for player
playerRockGuess = "You chose Rock";
playerPaperGuess = "You chose Paper";
playerScissorsGuess = "You chose Scissors";

#String Constants for COM
comRockGuess = "Com chose Rock";
comPaperGuess = "Com chose Paper";
comScissorsGuess = "Com chose Scissors";

#String Constants for results
win = "You Win"
lose = "You Lose"
tie = "Its a Tie"

#Game Driver
def rockPaperScissors(guessIndex = 0):
    print "Rock Paper Scissors"
    guess = raw_input("Rock Paper or Scissors? >>")
    antiguess = random.randint(1, 3)
    print "------"
    if guess in ("R", "r","Rock", "rock", "ROCK"):
        print playerRockGuess
        guessIndex = 1
    elif guess in ("P", "p", "Paper", "paper", "PAPER"):
        guessIndex = 2
        print playerPaperGuess
    elif guess in  ("S", "s", "Scissors", "scissors", "SCISSORS"):
        guessIndex = 3
        print playerScissorsGuess
    else:
        print "Not an Answer"

    if guessIndex > 0:
        determineWinner(guessIndex, antiguess);
    print "------"

    playAgain = raw_input("Play again? (y/n) >>")
    if playAgain == "y":
        return 1
    #else
    return  0

#Determines winner and
def determineWinner(guessIndex, antiguess):
    global comWins
    global playerWins
    if guessIndex == 1: #Rock
        #Tie
        if antiguess == 1:
            print comRockGuess
            print tie
        #Lose
        elif antiguess == 2:
            comWins+=1
            print comPaperGuess
            print lose
        #Win
        elif antiguess == 3:
            playerWins+=1
            print comScissorsGuess
            print win
    if guessIndex == 2: #Paper
        #Win
        if antiguess == 1:
            playerWins+=1
            print comRockGuess
            print win
        #Tie
        elif antiguess == 2:
            print comPaperGuess
            print tie
        #Lose
        elif antiguess == 3:
            comWins+=1
            print comScissorsGuess
            print lose
    if guessIndex == 3: #Scissors
        #Lose
        if antiguess == 1:
            comWins+=1
            print comRockGuess
            print lose
        #Win
        elif antiguess == 2:
            playerWins+=1
            print comPaperGuess
            print win
        #Tie
        elif antiguess == 3:
            print comScissorsGuess
            print tie

def main(roundTracker = 1):
    print "--- Round ", roundTracker, " ---"
    while rockPaperScissors():
        roundTracker+=1
        print "--- Round ", roundTracker, " ---", "\nPlayer:", playerWins, "--- Com: ", comWins

#Starts program
main()
