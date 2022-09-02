import kb
import kb_UI as UI 

# Main game module

def start_game():
    '''
    Starts KnuckleBones game
    '''
    print("\nWelcome to a very scuffed KnuckleBones game on console\n")

    game = kb.KnuckleBones()
    game.create_achievements()
    UI.firstMove(game)

    while True:
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
            except kb.FullColumn: # 0 is not in list of line 34, place_die, full
                UI.fullColMsg()
        if game.boardFull():
            game.update_scores()
            UI.show_gb(game.top, game.bot)
            UI.show_achievements(game)
            UI.winner_output(game.winner())
            UI.stats_output(game)
            if UI.playAgain():
                game.reset()
            else:
                break


if __name__ == '__main__':
    start_game()
