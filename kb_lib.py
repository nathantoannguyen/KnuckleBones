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
    print("Please enter a valid column number of 1, 2, or 3.")
    
def fullColMsg():
    '''
    Informs user that column number input is full 
    '''
    print("Column is full. Please try placing a die in another column.")

def winner_output(winner: str):
    '''
    Prints appropriate winner message based on winner input
    '''
    if winner != 'Tie':
        print(f"{winner} player wins!")
    else:
        print("The game ends in a tie!")

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
    print(f"\nScore: {top.score}")
    for i in range(3-1,-1,-1):
        for j in range(3):
            print(top.board[j][i],end=' ')
        print()
    
    print('-----')
    
    for i in range(3):
        for j in range(3):
            print(bot.board[j][i],end=' ')
        print()

    print(f"Score: {bot.score}\n")
