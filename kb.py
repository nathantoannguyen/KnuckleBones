import random

# Game logic: Gameboard class and KnuckleBones class

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
        Initializes board for both players 
        0 = Top
        1 = Bot
        '''
        self.top = GameBoard()
        self.bot = GameBoard()
        self.turn = random.randint(0,1) # randomizes if bot or top goes first
    
    def boardFull(self) -> bool:
        '''
        Checks if any board is full
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
                
    def update_scores(self):
        '''
        Updates scores for both gameboards
        '''
        self.top.update_score()
        self.bot.update_score()
        
    def winner(self) -> bool:
        '''
        returns winner based on score
        '''
        if self.top.score > self.bot.score:
            return "Top" 
        elif self.top.score < self.bot.score:
            return "Bottom" 
        else: # tie
            return "Tie"
