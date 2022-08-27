import random

# UI module

def rollDie() -> int:
    '''
    Rolls die
    '''
    dieNum = random.randint(1,6)
    print(f"You rolled a {dieNum}!\n")
    return dieNum

def invalidInput():
    '''
    Informs user their input is not a valid column number
    '''
    print("\nPlease enter a valid column number of 1, 2, or 3.\n")
    
def fullColMsg():
    '''
    Informs user that column number input is full 
    '''
    print("\nColumn is full. Please try placing a die in another column.\n")

def winner_output(winner: str):
    '''
    Prints appropriate winner message based on winner input
    '''
    if winner != 'Tie':
        print(f"{winner} player wins!")
    else:
        print("The game is a draw!")

def stats_output(kb):
    '''
    Prints stats message
    '''
    print(f"\nOut of the {kb.rounds} game(s) played, Top player won {kb.topwins} time(s) and Bottom player won {kb.botwins} time(s).")
    print(f"You tied {kb.ties} time(s)")

def promptMove() -> int:
    '''
    Prompts current player to enter a valid column number
    :return: the col number if valid (1-3, int) and random die number
    '''
    while True:
        print("Enter which column (1-3) from left to right you would like to place your die in: ")
        col = input()
        if not col.isdigit(): 
            invalidInput()
            continue 
        
        colNum = int(col)
        if colNum not in range(1,4): 
            invalidInput()
            continue
    
        return colNum

def playAgain() -> bool:
    while True:
        answer = input("Would you like to play again? (Y/N): \n")
        if answer.upper() == "Y":
            return True
        elif answer.upper() == "N":
            return False
        else:
            print("\nInvalid input! Please enter Y or N")

def firstMove(kb):
    '''
    Outputs if top or bot is going first
    '''
    person = "Top" if kb.turn == 0 else "Bottom"
    print(f"{person} board goes first.")

def current_turn(kb):
    '''
    Prints current turn depending on KnuckleBones input
    '''
    person = "Top" if kb.turn == 0 else "Bottom"
    print(f"It is {person}'s turn.")


def show_gb(top, bot):
    '''
    Displays gameboard readable to user
    '''
    print()
    indent = "          "
    print(indent, '---------')
    for i in range(3-1,-1,-1):
        print(indent, "| ", end='')
        for j in range(3):
            print(top.board[j][i],end=' ')
        print("|", end="")
        if i == 0:
            print(f"  Score: {top.score}")
        else:
            print()
    
    print(indent, '---------')
    
    for i in range(3):
        if i != 0:
            print(indent, "| ", end='')
        else:
            print(f"Score: {bot.score: <4}| ", end='')
        for j in range(3):
            print(bot.board[j][i],end=' ')
        print("|")
    print(indent, '---------')
    print()
