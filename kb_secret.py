from kb import GameBoard, KnuckleBones
import kb_UI as UI

class Achievement:
    def __init__(self, name, func, desc):
        self.name = name
        self.unlocked = False
        self.func = func
        self.desc = desc
    
    def achieved(self, kb):
        return self.func(kb)

def all_vals(value: int):
    '''
    Returns a function that returns True if all spaces in either board are occupied by a specific value.
    '''
    def new_func(kb: KnuckleBones):
        return [[value,value,value],[value,value,value],[value,value,value]] in [kb.top.board, kb.bot.board]
    return new_func