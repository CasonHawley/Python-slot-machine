import random
print('''Abandon All Hope Ye Who Enter Here!!
You have $100 in your wallet.
Answer with yes/no using y/n
To win you must get one of the following combinations:
BAR\tBAR\tBAR\t\tpays\t$1000
BELL\tBELL\tBELL/BAR\tpays\t$100
PLUM\tPLUM\tPLUM/BAR\tpays\t$50
ORANGE\tORANGE\tORANGE/BAR\tpays\t$25
CHERRY\tCHERRY\tCHERRY\t\tpays\t$20
CHERRY\tCHERRY\t  -\t\tpays\t$15
CHERRY\t  -\t  -\t\tpays\t$10
''')
#Constants:
INIT_STAKE = 100
ITEMS = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR"]

firstWheel = None
secondWheel = None
thirdWheel = None
stake = INIT_STAKE

def play():
    global stake, firstWheel, secondWheel, thirdWheel
    playQuestion = askPlayer()
    while(stake != 0 and playQuestion == True):
        firstWheel = spinWheel()
        secondWheel = spinWheel()
        thirdWheel = spinWheel()
        printScore()
        playQuestion = askPlayer()

def askPlayer():
    '''
    Asks the player if he wants to play again.
    expecting from the user to answer with y, or n
    '''
    global stake
    while(True):
        answer = input("You have $" + str(stake) + ". Would you like to play? ")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("You ended the game with $" + str(stake) + " in your hand.")
            return False
        else:
            print("wrong input!")

def spinWheel():
    '''
    returns a random item from the wheel
    '''
    randomNumber = random.randint(0, 5)
    return ITEMS[randomNumber]

def printScore():
    '''
    prints the current score
    '''
    global stake, firstWheel, secondWheel, thirdWheel
    if((firstWheel == "CHERRY") and (secondWheel != "CHERRY")):
        win = 10
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel != "CHERRY")):
        win = 15
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel == "CHERRY")):
        win = 20
    elif((firstWheel == "ORANGE") and (secondWheel == "ORANGE") and ((thirdWheel == "ORANGE") or (thirdWheel == "BAR"))):
        win = 25
    elif((firstWheel == "PLUM") and (secondWheel == "PLUM") and ((thirdWheel == "PLUM") or (thirdWheel == "BAR"))):
        win = 50
    elif((firstWheel == "BELL") and (secondWheel == "BELL") and ((thirdWheel == "BELL") or (thirdWheel == "BAR"))):
        win = 100
    elif((firstWheel == "BAR") and (secondWheel == "BAR") and (thirdWheel == "BAR")):
        win = 1000
    else:
        win = -1

    stake += win
    if(win > 0):
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- YOU WIN!!!!!!! $' + str(win))
    else:
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You lose. Wanna spin again?')

play()