

import random

def rollDie() -> int:
    dieNum = random.randint(1,6)
    print(f"You rolled a {dieNum}!\n")
    return dieNum

def invalidInput():
    print("Please enter a valid column number of 1, 2, or 3.\n")

def promptMove() -> int:
    '''
    Prompts current player to enter a valid column number
    :return: the col number if valid (1-3, int) and random die number
    '''
    while True:
        print("Please input which column (1-3) from left to right you would like to place your die in: ")
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
    print(f"{person} board goes first.\n")

def current_turn(kb):
    person = "Top" if kb.turn == 0 else "Bottom"
    print(f"It is {person}'s turn.")


def show_gb(top, bot):
    '''
    displays gameboard readable to user
    '''
    for i in range(3-1,-1,-1):
        for j in range(3):
            print(top.board[j][i],end=' ')
        print()
    
    print('-----')
    
    for i in range(3):
        for j in range(3):
            print(bot.board[j][i],end=' ')
        print()

    print()
