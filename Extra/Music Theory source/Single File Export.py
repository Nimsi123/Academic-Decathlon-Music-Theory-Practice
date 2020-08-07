import tkinter as tk
from tkinter import ttk
import random
from functools import partial

class Question:
  #class variables
  circ = {0: "C" , 1: "G", 2: "D", 3: "A", 4: "E", 5: "B",
          6: "F#", 7: "C#", -1: "F", -2: "Bb", -3: "Eb",
        -4: "Ab", -5: "Db", -6: "Gb", -7: "Cb"}

  on_keyboard = {0: ["C", "B#"], 1: ["C#", "Db"], 2: ["D"], 3: ["D#", "Eb"], 4: ["E", "Fb"],
                5: ["F", "E#"], 6: ["F#", "Gb"], 7: ["G"], 8: ["G#", "Ab"], 9: ["A"],
                10: ["A#", "Bb"], 11: ["B", "Cb"]}

  intervals = ["m2", "M2", "m3", "M3", "P4", "aug4, d5, TT", "P5", "m6", "M6", "m7", "M7", "P8"]

  key_lett = ["A", "B", "C", "D", "E", "F", "G"]
  neck = ["B", "E", "A", "D", "G", "C", "F"]
  accidental = ["#", "b"]

  def ret_indice_on_keyboard(letter):
    for key, value in Question.on_keyboard.items():
      if letter in value:
        return key

  def search_keyboard(search_note): 
    #what number is the keyboard on?
    
    for j, note in Question.on_keyboard.items():
      if search_note in note:
        return j

  def numOnCircle(): 
    #choose a key on circle and find its number of accidentals
    n = random.randint(-7, 7)

    #if there are keys to choose from
    if type(Question.circ[n]) == list:
      ww = random.randint(0, 1)
      start_note = Question.circ[n][ww]
    else:
      start_note = Question.circ[n]

    first_loc = Question.search_keyboard(start_note)

    #start_note is the key, n is the number of accidentals, j is the location of the first note in the key on the keyboard
    return start_note, first_loc, n

  def check_user_input(user_input, answer):
    if user_input == answer:
      print("CORRECT")
    else:
      print("WRONG. Here is the answer\n", answer)


  """def check_user_input_indices(user_input, answer):
    #get the int value of keyboard position
    for i in range(8):
      if user_input[i] != answer[i]:
        print("WRONG. Here is the answer\n", answer)
        return
    print("CORRECT")"""


  def return_keyboard_position(split_answer):
    keyboard_answer = []
    for note in split_answer:
      for int_position, key in Question.on_keyboard.items():
        if note == key:
          keyboard_answer.append(int_position)
          break
    return keyboard_answer

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
    return [f"Find the interval from {root} - {end_note}", answer]

    #Question.check_user_input(user_guess, answer)

class Scale_Question(Question):

  possible_inputs = ['C', 'B#', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'Fb', 'F', 'E#', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', "Cb", " "]

  major_pattern = [0, 2, 4, 5, 7, 9, 11, 12]

  def create(self):
    #this function creates the question for the user
    #root represents the scale note (ex. Eb Major Scale)
    #scale_indices represents the answer. this list holds the numeric indices of
    #   the answers on the keyboard
    
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
    #for every individual note inputted by the user, this method determines
    #   if the input is valid
    
    if guess not in Scale_Question.possible_inputs:
      return True
    else:
      return False

  def inp(self):
    #this method organizes the user's inputting process
    #guess_integer represents all of the user's inputs in numeric index form
    #   with respect to the piano

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
    guess_integer = []
    for note in guess_list:
      index = Question.ret_indice_on_keyboard(note)
      guess_integer.append(index)

    print(guess_integer)
    #return a numerical representation of the user's scale guess
    return guess_integer

  def __call__(self):
    #when the instance of the class is called, the process starts
    
    root, answer = self.create()
    return [f"Write the {root} Major scale", answer]
  
    #Question.check_user_input(user_guess, answer)

class Quizzer():
    #This class is the brains behind this program. It will generate a question for the user, validate the question for the user,
    #clean the user's input after each submission, and keep question missed for later review
    
    def submitAnswer(page, parent):

        if (page.hasSubmitted):
            return
        else:
            page.hasSubmitted = True

        #an exception for bad inputs is needed here

        for i in page.selection:
            if i.get() == "":
                page.hasSubmitted = False
                page.questionText.set(page.package[0] + "\nMake sure to choose for every selection. Review your answer!")
                return

        #convert user input to integers (for all except Interval)
        if (len(page.selection) != 1):
            user_guess = []
            for note in page.selection:
                index = Question.ret_indice_on_keyboard( note.get() )
                user_guess.append(index)
        else:
            user_guess = page.selection[0].get()

        #what's the verdict?
        if user_guess == page.package[1]:
            #the user inputted the correct answer
            page.questionText.set(page.questionLabel.cget("text") + "\nCORRECT")
            page.correctCount += 1
            page.scoreKeeperString.set(f"You've got {page.correctCount} questions correct")
        else:
            #the user did NOT input the correct answer
            if (len(page.selection) != 1):
                answer = []
                for i in page.package[1]:
                    answer.append( Question.on_keyboard[ i ] )
            else:
                answer = page.package[1]
            page.questionText.set(page.package[0] + f"\nThe correct answer is {answer}")
            parent.listOfIncorrectString.set(parent.missedCompilationLabel.cget("text") + f"\n{page.package[0]} --> {answer}")
    
    def nextQuestion(page):

        if (not page.hasSubmitted):
            return
        else:
            page.hasSubmitted = False
            #the user may continue. on the next turn, it CANNOT hit NEXT until it hits SUBMIT

        #clean the entry
        for element in page.selection:
            element.set("")

        #generate a new question
        page.package = page.questionGenerator()
        page.questionText.set(page.package[0])

class ScaleScreen():
    def __init__(self, parent):
        
        self.scaleQuestions = ttk.Frame(parent.tabControl) 
        parent.tabControl.add(self.scaleQuestions, text ='Scale')

        self.correctCount = 0
        self.scoreKeeperString = tk.StringVar()
        self.scoreKeeperString.set(f"You've got {self.correctCount} questions correct.")
        self.scoreCountLabel = ttk.Label(self.scaleQuestions, textvariable = self.scoreKeeperString)
        self.scoreCountLabel.pack()

        #SCALE QUESTION LAY OUT

        self.questionText = tk.StringVar()
        self.questionGenerator = Scale_Question()
        self.package = self.questionGenerator()
        self.questionText.set(self.package[0])

        self.questionLabel = ttk.Label(self.scaleQuestions, textvariable = self.questionText)
        self.questionLabel.pack()


        #OPTION-MENU object
        self.selection = []
        for i in range(8):
            self.selection.append(tk.StringVar(parent.window))

        labelScale = tk.Label(self.scaleQuestions, text= "Select your scale").pack()

        for i in range(8):
            tk.OptionMenu(self.scaleQuestions, self.selection[i], *parent.choices).pack( side = "left" )
            #this returns something but i wont need it...right?

        #MAKE BUTTONS
        
        self.scaleSubmitButton = ttk.Button(self.scaleQuestions, text = "Submit", command = partial(Quizzer.submitAnswer, self, parent))
        #replace command with : command = partial(Quizzer.submitAnswer, self)
        self.scaleSubmitButton.pack()

        #the user is NOT allowed to EFFECTIVELY press NEXT until SUBMIT has been pressed
        self.hasSubmitted = False
        
        self.scaleNextButton = ttk.Button(self.scaleQuestions, text = "Next", command = partial(Quizzer.nextQuestion, self))
        self.scaleNextButton.pack()

class ChordScreen():
    def __init__(self, parent):

        self.chordQuestions = ttk.Frame(parent.tabControl) 
        parent.tabControl.add(self.chordQuestions, text ='Chord')

        self.correctCount = 0
        self.scoreKeeperString = tk.StringVar()
        self.scoreKeeperString.set(f"You've got {self.correctCount} questions correct.")
        self.scoreCountLabel = ttk.Label(self.chordQuestions, textvariable = self.scoreKeeperString)
        self.scoreCountLabel.pack()

        #CHORD QUESTION LAY OUT

        self.questionText = tk.StringVar()
        self.questionGenerator = Chord_Question()
        self.package = self.questionGenerator()
        self.questionText.set(self.package[0])

        self.questionLabel = ttk.Label(self.chordQuestions, textvariable = self.questionText)
        self.questionLabel.pack()

        #OPTION-MENU object
        
        self.selection = []
        for i in range(3):
            self.selection.append(tk.StringVar(parent.window))

        labelChord = tk.Label(self.chordQuestions, text= "Select your chord").pack()

        for i in range(3):
            tk.OptionMenu(self.chordQuestions, self.selection[i], *parent.choices).pack( side = "left" )
            #this returns something but i wont need it...right?

        #MAKE BUTTONS
        
        self.chordSubmitButton = ttk.Button(self.chordQuestions, text = "Submit", command = partial(Quizzer.submitAnswer, self, parent))
        #replace command with : command = partial(Quizzer.submitAnswer, self)
        self.chordSubmitButton.pack()

        #   the user is NOT allowed to EFFECTIVELY press NEXT until SUBMIT has been pressed
        self.hasSubmitted = False
        
        self.chordNextButton = ttk.Button(self.chordQuestions, text = "Next", command = partial(Quizzer.nextQuestion, self))
        self.chordNextButton.pack()    

class IntervalScreen():
    def __init__(self, parent):
        
        self.intervalQuestions = ttk.Frame(parent.tabControl) 
        parent.tabControl.add(self.intervalQuestions, text ='Interval')

        self.correctCount = 0
        self.scoreKeeperString = tk.StringVar()
        self.scoreKeeperString.set(f"You've got {self.correctCount} questions correct.")
        self.scoreCountLabel = ttk.Label(self.intervalQuestions, textvariable = self.scoreKeeperString)
        self.scoreCountLabel.pack()

        #INTERVAL QUESTION LAY OUT

        self.questionText = tk.StringVar()
        self.questionGenerator = Interval_Question()
        self.package = self.questionGenerator()
        self.questionText.set(self.package[0])

        self.questionLabel = ttk.Label(self.intervalQuestions, textvariable = self.questionText)
        self.questionLabel.pack()

        #OPTION-MENU object

        self.selection = []

        self.selection.append(tk.StringVar(parent.window))

        labelInterval = tk.Label(self.intervalQuestions, text= "Select your interval").pack()

        self.intervalChoices = ["m2", "M2", "m3", "M3", "P4", "aug4, d5, TT", "P5", "m6", "M6", "m7", "M7", "P8", ""]

        tk.OptionMenu(self.intervalQuestions, self.selection[0], *self.intervalChoices).pack( side = "left" )
        #this returns something but i wont need it...right?

        #MAKE BUTTONS
        
        self.intervalSubmitButton = ttk.Button(self.intervalQuestions, text = "Submit", command = partial(Quizzer.submitAnswer, self, parent))
        #replace command with : command = partial(Quizzer.submitAnswer, self)
        self.intervalSubmitButton.pack()

        #   the user is NOT allowed to EFFECTIVELY press NEXT until SUBMIT has been pressed
        self.hasSubmitted = False
        
        self.intervalNextButton = ttk.Button(self.intervalQuestions, text = "Next", command = partial(Quizzer.nextQuestion, self))
        self.intervalNextButton.pack()

class Screen():
    
    def __init__(self):
        
        #MAKE THE WINDOW
        self.window = tk.Tk()
        self.window.title("Python Quiz")
        self.window.minsize(600,400)

        # Dictionary with options
        self.choices = ["Ab", "A", "A#", "Bb", "B", "B#", "Cb", "C", "C#",
                    "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#",
                    "Gb", "G", "G#", ""]

        #MAKE THE TABS

        self.tabControl = ttk.Notebook(self.window)

        #the code for each Frame is now decentralized
        self.scaleFrame = ScaleScreen(self)
        self.chordFrame = ChordScreen(self)
        self.intervalFrame = IntervalScreen(self)

        self.missedQuestions = ttk.Frame(self.tabControl) 
        self.tabControl.add(self.missedQuestions, text ='Missed Questions')
        
        self.tabControl.pack(expand = 1, fill ="both")

        #CODE FOR MISSED QUESTIONS
        self.listOfIncorrectString = tk.StringVar()
        self.listOfIncorrectString.set("Look over later:")
        self.missedCompilationLabel = ttk.Label(self.missedQuestions, textvariable = self.listOfIncorrectString)
        self.missedCompilationLabel.pack()

    def displayUserSelection(selection):
        for i in range(len(selection)):
            print(selection[i].get())
        return



#DRIVER CODE
page = Screen()

page.window.mainloop()











        
