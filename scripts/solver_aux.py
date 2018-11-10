from ortools.sat.python import cp_model


class xSolutionPrinter(cp_model.CpSolverSolutionCallback):
  """Print intermediate solutions."""

  def __init__(self, variables, bool_to_list_of_words):
    self.__variables = variables
    self.__solution_count = 0
    self.bool_to_list_of_words = bool_to_list_of_words
    self.bool_solutions_so_far = set()
    self.word_solutions_so_far = set()

  def NewSolution(self):
    bool_word = tuple([self.Value(v) for v in self.__variables])
    if bool_word in self.bool_solutions_so_far:
      pass
    else:
      self.__solution_count += 1
      self.bool_solutions_so_far.add(bool_word)
      t = tuple(self.bool_to_list_of_words[bool_word])
      self.word_solutions_so_far.add(t)


  def SolutionCount(self):
    return self.__solution_count

  def ReturnBoolSolutions(self):
    return self.bool_solutions_so_far

  def ReturnWordSolutions(self):
    return self.word_solutions_so_far

######

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
  """Print intermediate solutions."""

  def __init__(self, variables, bool_to_list_of_words):
    cp_model.CpSolverSolutionCallback.__init__(self)
    self.__variables = variables
    self.__solution_count = 0
    self.bool_to_list_of_words = bool_to_list_of_words
    self.bool_solutions_so_far = set()
    self.word_solutions_so_far = set()

  def OnSolutionCallback(self):
    self.__solution_count += 1
    for v in self.__variables:
      print('%s = %i' % (v, self.Value(v)), end = ' ')
    print()

  def SolutionCount(self):
    return self.__solution_count

  def NewSolution(self):
    bool_word = tuple([self.Value(v) for v in self.__variables])
    if bool_word in self.bool_solutions_so_far:
      pass
    else:
      self.__solution_count += 1
      self.bool_solutions_so_far.add(bool_word)
      t = tuple(self.bool_to_list_of_words[bool_word])
      self.word_solutions_so_far.add(t)

  def ReturnBoolSolutions(self):
    return self.bool_solutions_so_far

  def ReturnWordSolutions(self):
    return self.word_solutions_so_far
