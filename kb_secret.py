from kb import GameBoard, KnuckleBones
import kb_UI as UI

def run_achievements(kb):
    #func_dict = {"Achieved": blah, "Not Achieved": low_roll}
    
    pass

def low_roll(kb: KnuckleBones):
    return [[1,1,1],[1,1,1],[1,1,1]] in [kb.top.board, kb.bot.board]

def high_roll(kb: KnuckleBones):
    return [[6,6,6],[6,6,6],[6,6,6]] in [kb.top.board, kb.bot.board]

def afk(kb: KnuckleBones):
    return [[0,0,0],[0,0,0],[0,0,0]] in [kb.top.board, kb.bot.board]