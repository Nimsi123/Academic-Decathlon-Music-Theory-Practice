from Question import Question
import random
class Scale_Question(Question):

  possible_inputs = ['C', 'B#', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'Fb', 'F', 'E#', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', "Cb", " "]

  major_pattern = [0, 2, 4, 5, 7, 9, 11, 12]

  def create(self):
    #find a note on the circle of fifths
    #find its index on the keyboard
    num_on_circ = random.randint(-7,7)
    root = Question.circ[num_on_circ]
    num_on_key = Question.ret_indice_on_keyboard(root)
    
    #find the indices of the keys in the scale
    scale_indices = []
    for i in Scale_Question.major_pattern:
      scale_indices.append( (num_on_key + i) % 12)

    return root, scale_indices

  def bad_input(guess):
    if guess not in Scale_Question.possible_inputs:
      return True
    else:
      return False

  def inp(self):

    #recieve input from the user, one note at a time
    guess_list = []
    for i in range(8):
      guess = input(f"Note {i}: ").strip()
      while(Scale_Question.bad_input(guess)):
        print("case sensitive, beware the letters you type")
        guess = input(f"Note {i}: ").strip()
      guess_list.append(guess)
    #guess list is populated with notes on the keyboard
    print(guess_list)

    #convert to integers
    guess_integer = Question.convertToInt(guess_list)

    print(guess_integer)
    #return a numerical representation of the user's scale guess
    return guess_integer

  def __call__(self):
    root, answer = self.create()
    #print(f"write the scale of {root}M")
    #print(answer)
    #user_guess = self.inp()
    #Question.check_user_input(user_guess, answer)

    #return a question, and the answer
    question = f"write the scale of {root}M"
    return [question, answer]