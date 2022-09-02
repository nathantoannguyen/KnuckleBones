from kb import GameBoard, KnuckleBones
import kb_UI as UI

class Achievement:
    def __init__(self, name, func):
        self.name = name
        self.unlocked = False
        self.func = func
    
    def achieved(self, kb):
        if result:= (self.func(kb)):
            self.unlocked = True
        return result
    

def run_achievements(kb):
    for func in kb.achievements:
        if func(kb):
            #show game ui
            pass

def low_roll(kb: KnuckleBones):
    return [[1,1,1],[1,1,1],[1,1,1]] in [kb.top.board, kb.bot.board]

def high_roll(kb: KnuckleBones):
    return [[6,6,6],[6,6,6],[6,6,6]] in [kb.top.board, kb.bot.board]

def afk(kb: KnuckleBones):
    return [[0,0,0],[0,0,0],[0,0,0]] in [kb.top.board, kb.bot.board]