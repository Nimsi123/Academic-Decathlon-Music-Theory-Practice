import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tk dropdown example")
root.minsize(600,400)

# Add a grid
mainframe = tk.Frame(root)
mainframe.pack()

# Create a Tkinter variable
tkvar = tk.StringVar(root)

# Dictionary with options
choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
tkvar.set('Pizza') # set the default option

popupMenu = tk.OptionMenu(mainframe, tkvar, *choices)
label = tk.Label(mainframe, text="Choose a dish").pack()
popupMenu.pack()

"""
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)
"""

root.mainloop()
