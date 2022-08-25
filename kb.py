import kb_lib as kb
import random

class GameBoard():

    def __init__(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.score = 0

    def update_score(self):
        ''' 
        Updates score of board
        '''

        total = 0
        for outer in self.board:
            for num in set(outer):
                total += num * outer.count(num) * outer.count(num)
        self.score = total  
    
    def fullBoard(self) -> bool:
        '''
        Checks if there are no 0s in all game columns, in which the game will end
        '''
        for col in self.board:
            if 0 in col:
                return False
        return True
    
    def place_die(self, colNum: int, dieNum: int):
        '''
        Updates gameboard with placing die in colNum and dieNum
        '''
        current_spot = self.board[colNum-1].index(0)
        self.board[colNum-1][current_spot] = dieNum
        

class KnuckleBones():
    
    def __init__(self):

        '''
        Initializes board for both players and (game?)
        0 = Top
        1 = Bot
        '''

        self.top = GameBoard()
        self.bot = GameBoard()
        self.turn = random.randint(0,1) # randomizes if bot or top goes first
    
    def boardFull(self):
        '''
        Checks if board is full
        '''
        return self.top.fullBoard() or self.bot.fullBoard()

    def place_move(self, turn: int, dieNum: int, colNum: int):
        '''
        Places move in top or bot board depending on turn then switches
        '''
        if turn == 0:
            self.top.place_die(dieNum, colNum)
            self.turn = 1 
        if turn == 1:
            self.bot.place_die(dieNum, colNum)
            self.turn = 0
            
    def remove_die(self, turn: int, colNum: int, dieNum: int):
        '''
        Updates gameboard by removing all of dieNum from colNum of board 
        turn if dieNum exists
        '''
        player = self.top if turn == 0 else self.bot
        for value in player.board[colNum-1][:]:
            if value == dieNum:
                player.board[colNum-1].remove(dieNum)
                player.board[colNum-1].append(0)
