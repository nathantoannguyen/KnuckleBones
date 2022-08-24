
class KnuckleBones():
    
    def __init__(self):
        self.gameboardTop = [[0,0,0],[0,0,0],[0,0,0]]
        self.gameboardBot = [[0,0,0],[0,0,0],[0,0,0]]
        # Each board has a diff score so sep attributes for top and bot score
        # tbh I feel like it might be better to make a new gameboard class
        # with their own 2d list attribute and score attribute instead of making an attribute for both top and bottom
        # in the knucklebones class but also like. doing it this way isnt that bad so. up 2 u.
        self.scoreTop = 0
        self.scoreBot = 0
    
    def board_full(self):
        '''
        Returns true if any boards are full.
        '''
        def _check_single_gb(gb: list[list[int]]) -> bool:
            for lst in gb:
                if 0 in lst:
                    return False
            return True
        
        return _check_single_gb(self.gameboardTop) or _check_single_gb(self.gameboardBot)

    def update_score(self):
        ''' Updates score of both boards. '''
        def calc_score(gb: list[list[int]]) -> int:
            ''' Calculate total score given gameboard list. '''
            total = 0
            for outer in gb:
                for num in set(outer):
                    total += num * outer.count(num) * outer.count(num)
            return total
        self.scoreTop = calc_score(self.gameboardTop)
        self.scoreBot = calc_score(self.gameboardBot)
    
    def place_move(self, player: str, diceNum: int, col: int):
        '''
        T = Top
        B = Bottom
        I used an else statement though
        '''

        if player == 'T':
            gameboard = self.gameboardTop
            opposite = self.gameboardBot
        else:
            gameboard = self.gameboardBot
            opposite = self.gameboardTop

        current_spot = 0

        # Simpler way to calculate current_spot imo, the way you were doing it had the list assign to the dice num happen multiple times
        # instead of doing a for loop i just had it check if there was an empty spot and if there was, current_spot was assigned to first index of 0
        if 0 not in gameboard[col-1]:
            GameUI.fullCol(self)
            return
        else:
            current_spot = gameboard[col-1].index(0)
    
        gameboard[col-1][current_spot] = diceNum

        # Fixed bug where it doesn't remove all the dice of the same num
        for value in opposite[col-1][:]:
            if value == diceNum:
                opposite[col-1].remove(diceNum)
                opposite[col-1].append(0)
        self.update_score()

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
            for j in range(3):
                print(bot[j][i],end=' ')
            print()

        print()
    
    def fullCol(self):
        '''
        displays error message for a full column
        '''
        print("Column is full. Please select another column")

    def showScore(self, top, bot):
        pass

    # okay yeah we should prolly make gameboard its own class
    # so that we can pass the gameboard objects to the functions in gameui
    # and then print the board given its board attribute and then
    # also print score given its score attribute, instead of passing
    # the board list and the board score every time


'''
player1 = KnuckleBones()
player1.place_move('T',4,2)
player1.place_move('B',3,2)
player1.place_move('T',4,2)
player1.place_move('B',1,3)
player1.place_move('T',3,2)
print(player1.scoreTop)
print(player1.scoreBot)

player1 = KnuckleBones()
'''

# eheheh fake game. u can actually play 2 player game except its endless bc i didnt put in game over logic in dis
player1 = KnuckleBones()
person = "T"
while True:
    dice = rollDie()
    print()
    print("it is", person, "turn")
    print("your dice is", dice)
    col = int(input("what col: "))
    player1.place_move(person, dice, col)
    if person == "T":
        person = "B"
    else:
        person = "T"
    print("top score is", player1.scoreTop)
    print("bot score is", player1.scoreBot)


#   Below is example scoreboard from article linked in readme, using this 2 test the calculating score
#   can probably make a unit testing module if u wanna do that
'''
x = KnuckleBones()
x.place_move('T', 2, 1)
x.place_move('T', 4, 2)
x.place_move('T', 1, 2)
x.place_move('T', 2, 3)
x.place_move('T', 3, 3)
x.place_move('T', 3, 3)
x.place_move('B', 6, 1)
x.place_move('B', 3, 2)
x.place_move('B', 3, 2)
x.place_move('B', 4, 3)
x.place_move('B', 1, 3)
x.place_move('B', 1, 3)
print(x.gameboardTop)
print(x.gameboardBot)
print("score should be 21 and is calculated as", x.scoreTop)
print("score should be 26 and is calculated as", x.scoreBot)
'''
