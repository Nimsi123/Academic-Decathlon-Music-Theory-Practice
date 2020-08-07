import tkinter as tk
from tkinter import ttk
from functools import partial

from AcadecMusicTutor.Algorithms_Verification.Question import Question

from AcadecMusicTutor.Algorithms_Verification.Verify import submitAnswer
from AcadecMusicTutor.Algorithms_Verification.Verify import nextQuestion

class Template:

    def __init__(self, parent, tabNombre, algorithmClase, selectionNombre, opciones):
    	#the parent is the main window that holds this tab
        #super().__init__(parent, tabNombre, algorithmClass)
        self.choices = opciones
        self.selectionNumber = selectionNombre
        self.tabName = tabNombre
        self.questionGenerator = algorithmClase()

        #make the frame
        self.questionFrame = ttk.Frame(parent.tabControl)
        parent.tabControl.add(self.questionFrame, text = self.tabName)
        #self.tabControl.pack(expand = 1, fill ="both")

        self.makeQuestionLayout()

        self.makeMenuInput(parent)
        self.makeButtons(parent)

    def makeQuestionLayout(self):
        #QUESTION LAY OUT                     *****ALGORITHM INPUT*****
        self.questionText = tk.StringVar()
        self.package = self.questionGenerator() #the package object is a list [question, answer] #goes to the __call__ method
        self.questionText.set(self.package[0])
        self.questionLabel = ttk.Label(self.questionFrame, textvariable = self.questionText)
        self.questionLabel.pack()

    def makeMenuInput(self, parent):
        #                                       Create a Tkinter OPTION-MENU object
        self.selection = []
        for i in range(self.selectionNumber):
            self.selection.append(tk.StringVar(parent.window))

        labelScale = tk.Label(self.questionFrame, text= "Select your scale").pack()

        for i in range(self.selectionNumber):
            tk.OptionMenu(self.questionFrame, self.selection[i], *self.choices).pack( side = "left" )
            #this returns something but i wont need it...right?

    def makeButtons(self, parent):
        #                                       MAKE BUTTONS
        self.scaleSubmitButton = ttk.Button(self.questionFrame, text = "Submit", command = partial(submitAnswer, self))
        self.scaleSubmitButton.pack()

        #   the user is NOT allowed to EFFECTIVELY press NEXT until SUBMIT has been pressed
        self.hasSubmitted = False
        
        self.scaleNextButton = ttk.Button(self.questionFrame, text = "Next", command = partial(nextQuestion, self))
        self.scaleNextButton.pack()