import Scale_Question, Chord_Question, Interval_Question

scale = Scale_Question.Scale_Question()
chord = Chord_Question.Chord_Question()
interval = Interval_Question.Interval_Question()

for i in range(8):
    scale()
    chord()
    interval()
