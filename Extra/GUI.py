import tkinter as tk
from tkinter import ttk
from functools import partial

root = tk.Tk()
root.title("Music GUI")
root.minsize(600,400)

# Add a grid
mainframe = tk.Frame(root)
mainframe.pack()

# Create a Tkinter variable
#selectionNumber
selOne = tk.StringVar(root)

selection = []
for i in range(8):
    selection.append(tk.StringVar(root))

# Dictionary with options
choices = ["Ab", "A", "A#", "Bb", "B", "B#", "Cb", "C", "C#",
            "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#",
            "Gb", "G", "G#"]
#tkvar.set('Pizza') # set the default option #not needed for me

label = tk.Label(mainframe, text= "Select your scale").pack()

for i in range(8):
    tk.OptionMenu(mainframe, selection[i], *choices).pack( side = "right")
    #this returns something but i wont need it...right?

submitButton = ttk.Button(mainframe, text = "Submit") #did not define command for this
submitButton.pack()

#how to get the user's selection? -->
#selection[0].get()

root.mainloop()
