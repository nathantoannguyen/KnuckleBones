import kb
import kb_lib as lib


def start_game():
    
    print("\nWelcome to a very scuffed KnuckleBones game on console\n")

    game = kb.KnuckleBones()

    lib.firstMove(game)
    lib.show_gb(game.top, game.bot)

    while True:
        lib.current_turn(game)
        dieNum = lib.rollDie()
        colNum = lib.promptMove()
        game.place_move(game.turn, colNum, dieNum)
        lib.show_gb(game.top, game.bot)

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
