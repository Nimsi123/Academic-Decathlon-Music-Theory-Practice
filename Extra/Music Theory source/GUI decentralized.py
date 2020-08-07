import tkinter as tk
from tkinter import ttk
import random
from functools import partial
import Scale_Question, Chord_Question, Interval_Question
from Question import Question

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
        self.questionGenerator = Scale_Question.Scale_Question()
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
        self.questionGenerator = Chord_Question.Chord_Question()
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
        self.questionGenerator = Interval_Question.Interval_Question()
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











        
