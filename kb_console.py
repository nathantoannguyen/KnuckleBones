import kb
import kb_lib as lib


def start_game():
    
    print("\nWelcome to a very scuffed KnuckleBones game on console\n")

    game = kb.KnuckleBones()
    lib.firstMove(game)

    while not game.boardFull():
        lib.show_gb(game.top, game.bot)
        lib.current_turn(game)
        dieNum = lib.rollDie()
        while True:
            colNum = lib.promptMove()
            try:
                game.place_move(game.turn, colNum, dieNum)
                game.remove_die(game.turn, colNum, dieNum)
                game.update_scores()
                break
            except ValueError: # 0 is not in list of line 34, place_die, full
                lib.fullColMsg()
                
    game.update_scores()
    lib.show_gb(game.top, game.bot)

# TODO
# Add UI for game overs and method for checking winner

# while True
    # prompt move
    # check if move is valid
    # place move
    # checkIfCancelsOut
    # checkifBoardFull
    # if board is full, display final board with score
# TODO: Show gb again every time they enter an invalid input?
#       Implement score with showing gb

if __name__ == '__main__':
    start_game()
