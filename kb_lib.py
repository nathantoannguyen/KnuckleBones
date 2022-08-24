
def promptMove() -> int:
    '''
    Prompts current player to enter a valid column number
    and returns the col num if valid
    '''
    while True:
        print("Please input which column (1-3) from left to right you would like to place your die in: ")
        col = input()
        if not col.isdigit(): continue 
        
        colNum = int(col)
        if colNum not in range(1,4): continue
    
        return colNum
