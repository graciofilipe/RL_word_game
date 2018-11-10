from scripts.load_dictionary import return_words
from scripts.aux_functions import is_only_letters, has_no_duplicate_letter, does_not_end_with_s, \
                          word_to_list_of_bools, compute_word_overlap
from ortools.sat.python import cp_model
from string import ascii_letters as letters
from scripts.solver_aux import SolutionPrinter
from collections import defaultdict

lower_case_letters = letters[:26]


class WordGame:

    def __init__(self, word_list, length_of_word, word_to_guess=[]):

        self.length_of_word = length_of_word

        length_filtered_words = [w for w in word_list if len(w) == length_of_word]
        filtered_words = filter(is_only_letters, length_filtered_words)
        filtered_words = filter(has_no_duplicate_letter, filtered_words)
        filtered_words = filter(does_not_end_with_s, filtered_words)

        self.words = list(set(list(filtered_words)))
        self.words.sort()
        self.n_initial_words = len(self.words)
        self.constraints_passed = {}
        self.word_to_guess = word_to_guess

        ## create a dictionary mapping between bools and words
        bool_to_list_of_words = defaultdict(list)
        for word in self.words:
            bool_word = tuple(word_to_list_of_bools(word))
            bool_to_list_of_words[bool_word].append(word)
        self.bool_to_list_of_words = bool_to_list_of_words


        # SOLVER AND CONSTRAINTS #
        model = cp_model.CpModel()
        solver = cp_model.CpSolver()
        self.model = model
        self.solver = solver

        # the main variable
        word_solver_var = [self.model.NewBoolVar('letter_{i}'.format(i=lower_case_letters[i])) for i in range(26)]
        self.word_solver_var = word_solver_var
        print('len(self.word_solver_var)', len(self.word_solver_var))

        # Initial constraints
        self.model.AddSumConstraint(word_solver_var, lb=length_of_word, ub=length_of_word)

        # is in list of words constraint
        list_of_words_in_bool = [tuple(word_to_list_of_bools(word)) for word in self.words]
        print('len of list_of_words_in_bool', len(list_of_words_in_bool))
        self.model.AddAllowedAssignments(self.word_solver_var, list_of_words_in_bool)

        #self.state = self.solve()


    def add_constraint(self, guess_word, number_of_overlapping_letters):
        guess_word_bool = word_to_list_of_bools(guess_word)
        idxs = [i for i in range(len(lower_case_letters)) if guess_word_bool[i]==1]
        self.model.AddSumConstraint([self.word_solver_var[idx] for idx in idxs],
                                    lb=number_of_overlapping_letters, ub=number_of_overlapping_letters)
        self.constraints_passed[guess_word] = number_of_overlapping_letters


    def solve(self):
        solution_printer = SolutionPrinter(self.word_solver_var,
                                           self.bool_to_list_of_words)
        status = self.solver.SearchForAllSolutions(self.model, solution_printer)
        self.status = status
        return solution_printer.ReturnWordSolutions()

    def get_words_in_play(self):
        return self.solve()

    def set_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state


    def return_state_and_reward_post_action(self, action):

        overlap = compute_word_overlap(action, self.word_to_guess)

        self.add_constraint(guess_word=action,
                            number_of_overlapping_letters=overlap)

        new_state = self.solve()

        if len(new_state)==1:
            reward = 1
            terminal_flag = True
        else:
            reward = -1
            terminal_flag = False

        return new_state, reward, terminal_flag
