import tkinter as tk
from tkinter import ttk
from functools import partial

from Template import Template
from Scale_Question import Scale_Question
from Chord_Question import Chord_Question
from Interval_Question import Interval_Question


class Screen:
	def __init__(self):

		self.window = tk.Tk()
		self.window.title("Python Quiz")
		self.window.minsize(600,400)
		
		self.tabControl = ttk.Notebook(self.window)

		#MAKE THE TABS
		self.scaleFrame = Template(self, "Scale", Scale_Question, 8, ["Ab", "A", "A#", "Bb", "B", "B#", "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#", "Gb", "G", "G#"])
		self.chordFrame = Template(self, "Chord", Chord_Question, 3, ["Ab", "A", "A#", "Bb", "B", "B#", "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#", "Gb", "G", "G#"])
		self.intervalFrame = Template(self, "Interval", Interval_Question, 1, ["m2", "M2", "m3", "M3", "P4", "aug4, d5, TT", "P5", "m6", "M6", "m7", "M7", "P8"])

		self.tabControl.pack(expand = 1, fill ="both")