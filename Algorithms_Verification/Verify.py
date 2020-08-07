from Question import Question

def submitAnswer(page):

    if (page.hasSubmitted):
        return
    else:
        page.hasSubmitted = True

    #an exception for bad inputs is needed here

    #validate the answer, and give the user feedback.
    if Question.check_user_input(page.selection, page.package[1], page.tabName):
        #the user inputted the correct answer
        print("CORRECT")
    else:
        #the user did NOT input the correct answer
        print("WRONG. Here is the answer\n", page.package[1])

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