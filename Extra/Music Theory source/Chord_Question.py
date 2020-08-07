from Question import Question
import random

class Chord_Question(Question):

  #possible_inputs = ['C', 'B#', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'Fb', 'F', 'E#', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', "Cb", " "] #why is the space there
  possible_inputs = ['C', 'B#', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'Fb', 'F', 'E#', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', "Cb"]

  chord_options = ["M", "m", "aug", "dim"]

  def bad_input(guess):
    if guess not in Chord_Question.possible_inputs:
      return True
    else:
      return False

  def inp(self):

    #recieve input from the user, one note at a time
    guess_list = []
    for i in range(3):
      guess = input(f"Note {i}: ").strip()
      while(Chord_Question.bad_input(guess)):
        print("case sensitive, beware the letters you type")
        guess = input(f"Note {i}: ").strip()
      guess_list.append(guess)
    #guess list is populated with notes on the keyboard
    print(guess_list)

    #convert to integers
    guess_integer = []
    for note in guess_list:
      index = Question.ret_indice_on_keyboard(note)
      guess_integer.append(index)

    print(guess_integer)
    #return a numerical representation of the user's scale guess
    return guess_integer

  def create(self):
    #choose a chord type
    chord_name = random.choice(Chord_Question.chord_options)

    #find a note on the circle of fifths
    #find its index on the keyboard
    num_on_circ = random.randint(-7,7)
    root = Question.circ[num_on_circ]
    num_on_key = Question.ret_indice_on_keyboard(root)
    
    #find the indices of the keys in the scale
    chord_indices = []

    if chord_name == "aug":
      pattern = [0, 4, 8]
    elif chord_name == "M":
      pattern = [0, 4, 7]
    elif chord_name == "m":
      pattern = [0, 3, 7]
    else:
      pattern = [0, 3, 6]


    for i in pattern:
      chord_indices.append( (num_on_key + i) % 12)

    return root, chord_indices, chord_name

  def __call__(self):
    root, answer, chord_name = self.create()
    return [f"Write the {root} {chord_name} chord", answer]

    #Question.check_user_input(user_guess, answer)
