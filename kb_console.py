
import kb
import kb_lib as lib


def start_game():
    
    print("\nWelcome to a very scuffed KnuckleBones game on console\n")

    game = kb.KnuckleBones()

    lib.firstMove(game)
    lib.show_gb(game.top, game.bot)

    while True:
        dieNum = lib.rollDie()
        colNum = lib.promptMove(game)
        game.place_move(game.turn, colNum, dieNum)
        lib.show_gb(game.top, game.bot)

# while True
    # place move
    # checkIfCancelsOut
    # checkifBoardFull
# TODO: Show gb every time they enter an invalid input stupid mf

if __name__ == '__main__':
    start_game()
