import numpy as np
import itertools
import random
from scripts.aux_functions import softmax
from scripts.aux_functions import word_to_list_of_bools, compute_word_overlap
from collections import Counter


class Agent:
    def __init__(self,  epsilon, possible_actions):
        self.epsilon = epsilon
        self.possible_actions = possible_actions
        self.word_actions_taken = []
        self.bool_actions_taken = []
        self.initialize_w()
        self.initialize_th()

    def initialize_w(self):
        # get the number of features, so I know the number of w
        n_features = 27
        self.w = np.array([0 for _ in range(n_features)])

    def initialize_th(self):
        # get the number of features, so I know the number of w
        n_features = 12
        self.th = np.array([0 for _ in range(n_features)])

    def return_w(self):
        return self.w

    def return_th(self):
        return self.th

    def add_to_actions_taken(self, word_to_add):
        self.word_actions_taken += [word_to_add]
        self.bool_actions_taken += [tuple(word_to_list_of_bools(word_to_add))]



    def state_to_feature_vec(self, state):
        n_letters = 26
        abs_freq = np.array([0 for let in range(n_letters)])
        for bool_word in state:
            for i in range(n_letters):
                abs_freq[i] += bool_word[i]
        total = np.sum(abs_freq)
        rel_freq = list(abs_freq/total)
        n_bools = [len(state)]
        return rel_freq + n_bools

    def state_value_estimate(self, state):
        feature_values = self.state_to_feature_vec(state)
        val_estimate = np.dot(a=self.w, b=feature_values)
        return val_estimate

    def state_value_estimate_gradient(self, state):
        g = self.state_to_feature_vec(state)
        return np.array(g)


    def rel_freq_of_dot_prod_of_bool_against_background(self, bool, list_of_bools):
        if len(list_of_bools)==0:
            return [0 for i in range(0, 6)]
        else:
            dot_prod_list = []
            for word_bool in list_of_bools:
                dot_prod_list.append(np.dot(a=bool,
                                            b=word_bool))
            c = Counter(dot_prod_list)
            abs_freq = [c.get(i, 0) for i in range(0, 6)]
            rel_freq = np.array(abs_freq)/np.sum(abs_freq)
            return rel_freq


    def state_action_to_feature_vec(self, state, action):
        action_bool = word_to_list_of_bools(word = action)

        rel_freq_against_words_left = \
            self.rel_freq_of_dot_prod_of_bool_against_background(
            bool=action_bool, list_of_bools=state)

        rel_freq_against_words_taken = \
            self.rel_freq_of_dot_prod_of_bool_against_background(
                bool=action_bool, list_of_bools=self.bool_actions_taken)

        return np.array(list(rel_freq_against_words_left) + list(rel_freq_against_words_taken))

    def from_state_action_to_q_estimate(self, state, action):
        feature_values = self.state_action_to_feature_vec(state, action)
        val_estimate = np.dot(a=self.th, b=feature_values)
        return val_estimate

    def get_state_action_values(self, state_to_interrogate):
        value_list = []
        possible_actions = self.possible_actions
        #random.shuffle(possible_actions)
        for action in possible_actions:
            val_estimate = self.from_state_action_to_q_estimate(state=state_to_interrogate,
                                                                action=action)
            value_list.append(val_estimate)
        return value_list

    def get_action_from_policy(self, state_to_interrogate):
        value_list = self.get_state_action_values(state_to_interrogate)
        possible_actions = self.possible_actions
        soft_values = softmax(value_list)
        action_indx_list = list(range(len(possible_actions)))
        chosen_indx = np.random.choice(a=action_indx_list, p=soft_values)
        chosen_action = possible_actions[chosen_indx]
        return chosen_action


    def ln_policy_gradient(self, state, action):
        x = self.state_action_to_feature_vec(state, action)
        z = np.dot(a=self.th, b=x)
        sm = softmax(z)
        out = x-sm
        return out


    def return_action(self, state):
        r = np.random.uniform()
        if r < self.epsilon:
            return self.possible_actions[np.random.choice(len(self.possible_actions))]
        else:
            return self.get_action_from_policy(state_to_interrogate=state)

    def update_w(self, new_w):
        assert len(self.w) == len(new_w)
        self.w = new_w

    def update_th(self, new_th):
        assert len(self.th) == len(new_th)
        self.th = new_th


    def increment_w(self, w_increment):
        assert len(self.w) == len(w_increment)
        self.w = np.array(self.w) + np.array(w_increment)

    def increment_th(self, th_increment):
        assert len(self.th) == len(th_increment)
        self.th = np.array(self.th) + np.array(th_increment)