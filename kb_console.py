import kb
import kb_UI as UI 

# Main game module

def start_game():
    '''
    Starts KnuckleBones game
    '''
    print("\nWelcome to a very scuffed KnuckleBones game on console\n")

    game = kb.KnuckleBones()
    UI.firstMove(game)

    while not game.boardFull():
        UI.show_gb(game.top, game.bot)
        UI.current_turn(game)
        dieNum = UI.rollDie()
        while True:
            colNum = UI.promptMove()
            try:
                game.place_move(game.turn, colNum, dieNum)
                game.remove_die(game.turn, colNum, dieNum)
                game.update_scores()
                break
            except ValueError: # 0 is not in list of line 34, place_die, full
                lib.fullColMsg()
                
    game.update_scores()
    UI.show_gb(game.top, game.bot)
    UI.winner_output(game.winner())

if __name__ == '__main__':
    start_game()
