from scripts.load_dictionary import load_words, filter_words
from scripts.game_classes import WordGame
from scripts.agent_class import Agent
from scripts.run_actor_critic_traces import run_actor_critic_traces
import cProfile, pstats, io


#######

def test_it_runs():

    #pr = cProfile.Profile()
    #pr.enable()
    words = load_words()
    filtered_words = filter_words(word_list=words, length_of_word=5)
    print(filtered_words)
    word_game = WordGame(filtered_words, 5)
    agent = Agent(epsilon=0.1, possible_actions=filtered_words)

    agent2 = run_actor_critic_traces(agent=agent,
                                     environment=word_game,
                                     start_state=word_game.state,
                                     n_iter=3,
                                     alpha_th=0.1,
                                     alpha_w=0.1,
                                     lambda_th=0.1,
                                     lambda_w=0.1,
                                     gama=0.9)