import tkinter as tk
from tkinter import ttk
import random
from functools import partial

#NOTE: self.hasSubmitted appears for each type of scale/chord/interval question
from Quizzer import Quizzer
from Chord_Question import Chord_Question
from Scale_Question import Scale_Question
from Interval_Question import Interval_Question


class Screen():
    
    def __init__(self):
        
        #MAKE THE WINDOW
        self.window = tk.Tk()
        self.window.title("Python Quiz")
        self.window.minsize(600,400)


        #MAKE THE TABS

        self.tabControl = ttk.Notebook(self.window) 

        self.scaleQuestions = ttk.Frame(self.tabControl) 
        self.tabControl.add(self.scaleQuestions, text ='Scale')

        self.chordQuestions = ttk.Frame(self.tabControl) 
        self.tabControl.add(self.chordQuestions, text ='Chord')

        self.intervalQuestions = ttk.Frame(self.tabControl) 
        self.tabControl.add(self.intervalQuestions, text ='Interval')


        
        self.missedQuestions = ttk.Frame(self.tabControl) 
        self.tabControl.add(self.missedQuestions, text ='Missed Questions')
        
        self.tabControl.pack(expand = 1, fill ="both")

        #CODE FOR QUESTIONS

        #   KEEP TRACK OF SCORE
        self.correctCountScale = 0
        self.correctCountChord = 0
        self.correctCountInterval = 0
        self.scoreKeeperString = tk.StringVar()
        self.scoreKeeperString.set(f"You've got {self.correctCountScale} scale questions correct.\nYou've got {self.correctCountChord} chord questions correct.\nYou've got {self.correctCountInterval} interval questions correct.")
        self.scoreCountLabel = ttk.Label(self.scaleQuestions, textvariable = self.scoreKeeperString)
        self.scoreCountLabel.pack()

        #   GENERATE QUESTIONS

        """
        self.questionText = tk.StringVar()
        self.package = Quizzer.generateQuestion()
        self.questionText.set(self.package[0])
        
        self.questionLabel = ttk.Label(self.takingQuestions, textvariable = self.questionText)
        self.questionLabel.pack()

        self.scaleAnswer = tk.StringVar()
        self.scaleAnswerEntry = ttk.Entry(self.scaleQuestions, width = 15, textvariable = self.scaleAnswer)
        self.scaleAnswerEntry.pack()
        """

        #---------------------------------------------------------------------------

        #   SCALE QUESTION LAY OUT

        #                           START: Create a Tkinter OPTION-MENU object
        self.scaleSelection = []
        for i in range(8):
            self.scaleSelection.append(tk.StringVar(self.window))

        # Dictionary with options
        self.choices = ["Ab", "A", "A#", "Bb", "B", "B#", "Cb", "C", "C#",
                    "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#",
                    "Gb", "G", "G#"]

        labelScale = tk.Label(self.scaleQuestions, text= "Select your scale").pack()

        for i in range(8):
            tk.OptionMenu(self.scaleQuestions, self.scaleSelection[i], *self.choices).pack( side = "left" )
            #this returns something but i wont need it...right?


        #                           DONE
        #       MAKE BUTTONS
        
        self.scaleSubmitButton = ttk.Button(self.scaleQuestions, text = "Submit", command = partial(Screen.displayUserSelection, self.scaleSelection))
        #replace command with : command = partial(Quizzer.submitAnswer, self)
        self.scaleSubmitButton.pack()

        #   the user is NOT allowed to EFFECTIVELY press NEXT until SUBMIT has been pressed
        self.hasSubmitted = False
        
        self.scaleNextButton = ttk.Button(self.scaleQuestions, text = "Next", command = partial(print, "next"))
        self.scaleNextButton.pack()
        
        #---------------------------------------------------------------------------


        #   CHORD QUESTION LAY-OUT

        self.chordSelection = []
        for i in range(3):
            self.chordSelection.append(tk.StringVar(self.window))

        labelChord = tk.Label(self.chordQuestions, text= "Select your chord").pack()

        for i in range(3):
            tk.OptionMenu(self.chordQuestions, self.chordSelection[i], *self.choices).pack( side = "left" )
            #this returns something but i wont need it...right?


        #                           DONE
        #       MAKE BUTTONS
        
        self.chordSubmitButton = ttk.Button(self.chordQuestions, text = "Submit", command = partial(Screen.displayUserSelection, self.chordSelection))
        #replace command with : command = partial(Quizzer.submitAnswer, self)
        self.chordSubmitButton.pack()

        #   the user is NOT allowed to EFFECTIVELY press NEXT until SUBMIT has been pressed
        self.hasSubmitted = False
        
        self.chordNextButton = ttk.Button(self.chordQuestions, text = "Next", command = partial(print, "next"))
        self.chordNextButton.pack()        

        #---------------------------------------------------------------------------
        
        self.intervalSelection = []

        self.intervalSelection.append(tk.StringVar(self.window))

        labelInterval = tk.Label(self.intervalQuestions, text= "Select your interval").pack()

        self.intervalChoices = ["m2", "M2", "m3", "M3", "P4", "aug4, d5, TT", "P5", "m6", "M6", "m7", "M7", "P8"]

        tk.OptionMenu(self.intervalQuestions, self.intervalSelection[0], *self.intervalChoices).pack( side = "left" )
        #this returns something but i wont need it...right?


        #                           DONE
        #       MAKE BUTTONS
        
        self.intervalSubmitButton = ttk.Button(self.intervalQuestions, text = "Submit", command = partial(Screen.displayUserSelection, self.intervalSelection))
        #replace command with : command = partial(Quizzer.submitAnswer, self)
        self.intervalSubmitButton.pack()

        #   the user is NOT allowed to EFFECTIVELY press NEXT until SUBMIT has been pressed
        self.hasSubmitted = False
        
        self.intervalNextButton = ttk.Button(self.intervalQuestions, text = "Next", command = partial(print, "next"))
        self.intervalNextButton.pack()

        #---------------------------------------------------------------------------

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


        




