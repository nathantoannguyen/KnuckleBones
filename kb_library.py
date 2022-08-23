
class KnuckleBones():
    
    def __init__(self):
        self.gameboardTop = [[0,0,0],[0,0,0],[0,0,0]]
        self.gameboardBot = [[0,0,0],[0,0,0],[0,0,0]]
        self.score = 0
    
    def update_score(self,num: int):
        self.score += num
    
    def place_move(self, player: str, diceNum: int, col: int):
        '''
        T = Top
        B = Bottom
        I used an else statement though
        '''
        gameboard = self.gameboardTop if player == 'T' else self.gameboardBot
        current_spot = 0
        
        for num in gameboard[col-1]:
            if num != 0:
                if current_spot == 2:
                    GameUI.fullCol(self)
                    return
                current_spot += 1
                continue
            else:
                gameboard[col-1][current_spot] = diceNum
        GameUI.show_gb(self, self.gameboardTop, self.gameboardBot)
        # TODO: after each move, 
        #       - update score
        #       - check if board is full to end game
        #       - print new gb

class GameUI():
    
    def show_gb(self, top, bot):
        '''
        displays gameboard readable to user
        '''
        for i in range(3-1,-1,-1):
            for j in range(3):
                print(top[j][i],end=' ')
            print()
        
        print('-----')
        
        for i in range(3):
            for j in range(3-1,-1,-1):
                print(bot[j][i],end=' ')
            print()

        print('-----')
        #print()
        # i think doing this is better for testing purposes
        # bc it has better readability since the former makes it
        # hard to distinguish between top and bottom when testing
        # w multiple moves. up 2 u tho

    def board_full(self, top, bot):
        '''
        Returns true if any boards are full.
        '''
        def _check_single_gb(gb):
            for lst in gb:
                if 0 in lst:
                    return False
            return True
        #oops srry if this is bad formatting but i likey my short circuiting vision.
        
        return _check_single_gb(top) or _check_single_gb(bot)
    

    def fullCol(self):
        '''
        displays error message for a full column
        '''
        print("Column is full. Please select another column")

player1 = KnuckleBones()
player1.place_move('T',4,2)
player1.place_move('B',3,2)
#print(player1.gameboardTop)
#print(player1.gameboardBot)
player1.place_move('T',4,2)
player1.place_move('B',1,3)
player1.place_move('T',3,2)
