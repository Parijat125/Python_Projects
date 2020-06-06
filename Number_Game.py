import tkinter
import random



incorrectSubmission  = 0
correctsubmission = 0
Attempts = 0
ListAnswers = []


def initializeGame():
    global Attempts
    global NumberToPass
    global Value
    global answer
    global operation
    operators = ['+','-','*','/']
    index = random.randint(0,3)
    operation = operators[index]
    check = False
    while (check == False):
        if operation == "*":
            NumberToPass = random.randint(0,99)
            Value = random.randint(0,99)
        elif operation == '+':
            NumberToPass = random.randint(0,999)
            Value = random.randint(0,999)
        elif operation == '-':
            NumberToPass = random.randint(0,999)
            Value = random.randint(0,999)
        elif operation == "/":
            NumberToPass = random.randint(0,999)
            Value = random.randint(1,999)
        check = True
    answers()
    gameWindow.title("Compute the equations {} {} {} =".format(NumberToPass,operation,Value))
    statusLabel.configure(text= "please enter an answer")
    button1.configure(text = "Submit your answer", command=checkNumbers)

def answers():
    global NumberToPass
    global Value
    global answer
    global operation
    global ListAnswers
    check = False
    if operation == '*':
        answer = (NumberToPass * Value)
    elif operation == '-':
        if (NumberToPass - Value) < 0:
            while (check == False):
                NumberToPass = random.randint(0,999)
                Value = random.randint(0,999)
                if (NumberToPass - Value) < 0:
                    check = False
                else:
                    check = True
                    answer = (NumberToPass - Value)
        else:
            answer = (NumberToPass - Value)
    elif operation == '/':
        if (NumberToPass % Value) != 0:
            while (check == False):
                NumberToPass = random.randint(0,999)
                Value = random.randint(1,999)
                if (NumberToPass % Value) != 0:
                    check = False
                else:
                    check = True
                    answer = (NumberToPass / Value)
        else:
            answer  = (NumberToPass / Value)
    elif operation == '+':
        answer = (NumberToPass + Value)
    ListAnswers.append(answer)


def checks():
    global ListAnswers
    for items in range(len(ListAnswers)):
        if len(ListAnswers) == 1:
            pass
        if ListAnswers[items] == ListAnswers[items - 1]:
            answers()
        else:
            pass
        
def checkNumbers():
    global answer
    global Attempts
    global incorrectSubmission
    global correctsubmission
    submissionString = guessEntry.get()
    answer = guessEntry.get()
    submission = (submissionString)
    if (submission == answer):
        Attempts += 1
        correctsubmission += 1
        statusLabel.configure(text = str(submission) + "is correct! Would you like to play again")
        button1.configure(text = "New game", command = newGame)
        button3.configure(text = 'New Question', command = initializeGame)
    elif (submission != answer):
        incorrectsubmission += 1
        statusLabel.configure(text = str(submission) + "is not the correct answer.Try again")
        button2.configure(text = 'Quit', command = quitGame)
    guessEntry.delete(0,tkinter.END)
    
   
def newGame():
    initializeGame()
    

def quitGame():
    global Attempts
    global incorrectSubmission
    global correctsubmission
    if Attempts == 0:
        average = (incorrectSubmission)
    else:
        average = (incorrectSubmission/ Attempts)
    print("you attempted {} problems, of which you got {} correct, and {} incorrect. The average for each attempt is {}.".format(Attempts, correctsubmission , incorrectSubmission, average))
    gameWindow.destroy()

operation = None

gameWindow = None

button1 = None

button2 = None

button3 = None


def initializeGameWindow():
    global gameWindow
    global guessEntry
    global statusLabel
    global button1
    global statusLabel1
    global button2
    global button3 
    global root

    gameWindow = tkinter.Tk()

    topFrame = tkinter.Frame(gameWindow)
    topFrame.pack()
    bottomFrame = tkinter.Frame(gameWindow)
    bottomFrame.pack()
    label1 = tkinter.Label(topFrame, text = "Your Guess:")
    label1.pack(side=tkinter.LEFT)
    guessEntry = tkinter.Entry(topFrame)
    guessEntry.pack(side = tkinter.LEFT)
    button1 = tkinter.Button(topFrame, text = "checkSubmission" , command = checkNumbers)
    button1.pack()
    button2 = tkinter.Button(bottomFrame, text = "Quit", command = quitGame)
    button2.pack()
    button3 = tkinter.Button(bottomFrame, text = "New Question" , command = initializeGame)
    button3.pack()
    

    statusLabel = tkinter.Label(gameWindow, text="there are no current submissions")
    statusLabel.pack()
    statusLabel1 = tkinter.Label(gameWindow, text="Number of incorrect entries?")
    statusLabel1.pack()

def startGame():
    global NumberToPass
    global elements
    global operation
    initializeGameWindow()
    initializeGame()
    gameWindow.mainloop()
    
    
    

    

    
    



