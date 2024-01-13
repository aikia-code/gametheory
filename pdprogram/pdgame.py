from random import choice

from pdplayer import Player
from pdsession import Session
from pdtypes import Choice, Score


gamechoices = [Choice.COOPORATE, Choice.DEFECT]

pl_A, pl_B = Player("P-A"), Player("P-B")

session = Session(pl_A, pl_B)

sessions = []


for i in range(10):
    try:
        if sessions[-1].get_choices(pl_B) == Choice.DEFECT:
            pl_A.choose(Choice.DEFECT)
        else:
            pl_A.choose(Choice.COOPORATE)
    except IndexError:
        pl_A.choose(Choice.COOPORATE)

    pl_B.choose(choice(gamechoices))

    session.compute_score()
    
    print(session.get_choices())
    
    sessions.append(session)
