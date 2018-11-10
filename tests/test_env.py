from scripts.game_classes import WordGame
from scripts.load_dictionary import return_words
import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()

#######

def test_env_loads():
    w = return_words()
    w1 = WordGame(w, 5)
    w1.add_constraint('spear', 2)
    w1.solve()