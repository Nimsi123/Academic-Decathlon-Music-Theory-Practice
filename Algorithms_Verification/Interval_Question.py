from AcadecMusicTutor.Algorithms_Verification.Question import Question
import random

class Interval_Question(Question):
  possible_inputs = ["m2", "M2", "m3", "M3", "P4", "aug4, d5, TT", "P5", "m6", "M6", "m7", "M7", "P8"]

  def create(self):
    i = random.randint(0, 11)
    inte = Question.intervals[i]
    true_distance = i+1

    num_on_circ = random.randint(-7,7)
    root = Question.circ[num_on_circ]
    num_on_key = Question.ret_indice_on_keyboard(root)

    end_index = (num_on_key + true_distance) % 12
    end_note = Question.on_keyboard[end_index]

    #if there are options
    
    if type(end_note) is list:
      choices = len(end_note)
      q = random.randint(0,choices-1)
      end_note = end_note[q]

    #inte is the name of the interval
    return inte, root, end_note

  def inp():
    guess = input("Answer: ").strip()

    while (guess not in Interval_Question.possible_inputs):
      print("case sensitive, beware the letters you type")
      guess = input("Answer: ").strip()

    return guess

  def __call__(self):
    answer, root, end_note = self.create()
    #print(f"Find the interval of {root} - {end_note}")
    #print(answer)
    #user_guess = Interval_Question.inp()
    #Question.check_user_input(user_guess, answer)

    question = f"Find the interval of {root} - {end_note}"
    return [question, answer]