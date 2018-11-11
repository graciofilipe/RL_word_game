from scripts.game_classes import WordGame
from scripts.load_dictionary import return_words
import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()

#######

def test_env_loads():

    #pr = cProfile.Profile()
    #pr.enable()

    w = return_words()
    w1 = WordGame(w, 5)
    w1.add_constraint('shark',
                      number_of_overlapping_letters=3)

    x = w1.solve()
    print(x)
    #pr.disable()
    #s = io.StringIO()
    #ps = pstats.Stats(pr, stream=s)
    #pr.print_stats(sort="cumtime")
    #print(s.getvalue())