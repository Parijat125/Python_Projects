import tkinter
import random
import math

Attemped = 0
probmlemSolved = 0
IncorrectSolved = 0
problemPresented= 0
CurrentProblemNumber = 0
operators = [ '+' , '-' , '*' , '/' ]
Clist = []


def chechValidity (problem):
    if problem in problemPresented:
        return False
    return True



def initializeGame():
    global CurrentProblemNumber
    opIndex = random.randint(0,3)
    operator = operators[opIndex]
    valid = False 
    while (valid == False):
        if operator == '*':#2
            n1 = random.randint(0,99)
            n2 =random.randint(0,99)
        elif operator == '+': #0
            n1 = random.randint(0,999)
            n2 =random.randint(0,999)      
        elif operator == '-': #1
            n1 = random.randint(0,999)
            n2 = random.randint(0, n1)
        elif operator == '/':#3
            n1 = random.randint(0,999)
            n2 = random.randint(1,n1)
            while (n1 % n2 != 0): 
                n1 = random.randint(0,999)
                n2 = random.randint(1, n1)
                pass
        valid = True
    if isDuplicate(operator,n1,n2):
        c = (-1,-1,-1)
        return c
    else:
        c= (operator, n1,n2)
        Clist.append(c)
        return c
    
    CurrentProblemNumber +=1
    gameWindow.title(text = "Math Problem")
    statusLabel.configure(text="You haven't made any guesses yet")
    button1.configure(text="Check It!", command=checkNumbers)
    button2.configure(text = "Show me a new game", command = initializeGame)
    button3.configure(text = "Quit", command = QuitGame)
    answers()

def isDuplicate (operator, n1,n2):
    global Clist
    for tup in Clist:
        if tup[1] == n1:
            if tup[0] == operator and tup[2] == n2:
                return True

    return False


   
def answers():
    global n1
    global n2
    global operator
    if operator == '*':
        answer = (n1 * n2)        
    elif operator == '+':
        answer = (n1 + n2)              
    elif operator == '-':
          answer = (n1 - n2)
    elif operator == '/':
        answer = (n1 / n2)    
   

# read number entered into GUI by player, check whether it's correct, and
# give appropriate feedback in the statusLabel
#
def checkNumbers():
    global answer
    global correctNumberSolved
    global IncorrectSolved
    global Attemped
    guessAsString = guessEntry.get()
    guess = int(guessAsString)
    if( guess == answer):
        correctNumberSolved +=1
        statusLabel.configure(text = str(guess)+" is right answer! - you win! ")
        button2.configure(text = "Show me a new game", command = initializeGame) 
        button3.configure(text = "Quit", command = QuitGame)
        Attemped +=1
    else:
        statusLabel.configure(text =  " Incorrect !")
        button2.configure(text = "Show me a new game", command = initializeGame)
        button3.configure(text = "Quit", command = QuitGame)
        IncorrectSolved +=1
        Attemped +=1
    guessEntry.delete(0, tkinter.END)
# global variables 



# during a game, the number that is to be guessed
answer = None

# the main window, where interaction and feedback will occur
gameWindow = None

# the only button in the GUI
button1 = None

button2 = None

button3 = None


def initializeGameWindow():
    global gameWindow
    global guessEntry
    global statusLabel
    global button1
    global button2
    global button3
    global c
    c = initializeGame()
    while c ==(-1,-1,-1):
        c = initializeGame()
    problemLabText = str(c[1]) +str(c[0]) +str(c[2])
    
    gameWindow = tkinter.Tk()
    
    # topFrame is a container to hold three widgets in the top row of the window
    # 1) a label, 2) an Entry, where users can type guesses, 3) a button to press
    topFrame = tkinter.Frame(gameWindow)
    topFrame.pack()
    bottomFrame = tkinter.Frame(gameWindow)
    bottomFrame.pack()


    label1 = tkinter.Label(topFrame, text = problemLabText)
    label1.pack(side=tkinter.LEFT)
    guessEntry = tkinter.Entry(topFrame)
    guessEntry.pack(side=tkinter.LEFT)
    button1 = tkinter.Button(topFrame, text= "Check It!", command = checkNumbers)
    button1.pack()
    button2 = tkinter.Button(bottomFrame, text = "Show me a new game", command = initializeGame)
    button2.pack()
    button3 = tkinter.Button(bottomFrame, text = "Quit", command = gameWindow.destroy)
    button3.pack()

    # create and place a Label below the topFrame container. Messages about
    # game status will be shown on this label.
    statusLabel = tkinter.Label(gameWindow, text="You haven't made any guesses yet")
    statusLabel.pack()




# Call this function to start the GUI and game!
#
def startGameGUI():
    global c
    initializeGameWindow()
    initializeGame()
    gameWindow.mainloop()


