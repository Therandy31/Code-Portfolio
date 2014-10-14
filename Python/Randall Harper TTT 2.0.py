# Randall Harper
# CS 1411 Section 502
# Tic Tac Toe 2.0
# modified 12/12/13
# added "play again same mode button"
# added "quit game button"

"""
A *cell* is an integer in the interval [1,10). 
The cells are visualized as corresponding to
squares on a 3x3 tic tac toe board as pictured
below:
 
  1  2  3
 
  4  5  6
 
  7  8  9
 
A *player* is either the string 'x' or the string 'o'. 'nuff said. 

A *mode* is one of the following strings: 'select', 'twoPlayer','easyAI', 'mediumAI', 'hardAI'. 
These are thought of as modes of the pgoram, where 'select' is the initial state of the program
and the other four modes indicate a game in progress, corresponding to options 1-4 in the game
play description. 

A *state* is a triple (Xs,Os,m) where Xs and Os are lists of cells, and m is a mode. The state
(Xs,Os,m), where m is not 'select', is thought of as a game in progress in mode m, with x occupying
the cells in Xs and o occupying the cells on Os. The state ([],[],'select') is the initial
state of the program, where the selection screen is displayed.

'easyAI' strategy -> if empty(c,S), random insert cell
'mediumAI' strat  -> if win is possible move, if block is possible move, otherwise tie
'hardAI' strategy -> always win, or tie if cant win
"""

from random import randint

# initialState() is the state in which the game begins.
def initialState():
    return ([],[],'select')

# displayImages: state -> imageList
# displayImages(S) is a list containing the images to be displayed on 
# the screen in program state S. Images occurring later in the list overwrite 
# images that occur earlier if they overlap.

# selectionScreen is the displayImages function from Tic Tac Toe 1.0.
def displayImages(S):
    if S[2]=='select': return selectionScreen()
    else             : return gameScreen((S[0],S[1]))

# successor: state x point -> state
# successor(S,p) is the state resulting from clicking point p in state S.
def successor(S,p):
    mode = S[2]
    if mode =='select':
        return gameSelection(S,p) # you have to write this function
    elif over(S): 
        return overSuccessor(S,p)  # you have to write this function
    elif mode == 'twoPlayer':
        # the successor will be determined by the mouse click
        return twoPlayerSuccessor(S,p)  # this is the old successor function
    else:
        # we are in one of the AI modes
        return AISuccessor(S,p)

# selectionScreen: imageList
# selectionScreen() is a list containing the images to be displayed on the
# screen in the initial state. The images display info about following 4 modes
# that the player can select to play: 'twoPlayer', 'easyAI', 'mediumAI', and
# 'hardAI'.
def selectionScreen():
    List = gameBoard1() + selections()
    return List

# gameSelection: state x point -> state
# If S is a selection state, gameSelection(S,p) is the state resulting from
# clicking point p in state S.
def gameSelection(S,p):
    if p[0]<400 and p[0]>100 and p[1]<450 and p[1]>350: return (S[0],S[1],'easyAI')
    if p[0]<400 and p[0]>100 and p[1]<350 and p[1]>250: return (S[0],S[1],'mediumAI')
    if p[0]<400 and p[0]>100 and p[1]<250 and p[1]>150: return (S[0],S[1],'hardAI')
    if p[0]<400 and p[0]>100 and p[1]<150 and p[1]>50:  return (S[0],S[1],'twoPlayer')
    else: return S

# gameScreen: state -> imageList 
# gameScreen(S) is a list containing the images to be displayed on the screen
# while a game is in progress.
def gameScreen(S):
    List = gameBoard() + playerTokens(S)
    if over(S): List = List + playAgainButton() + winnerMessage(S)
    else: List = List + turnMessage(S)
    return List

# gameBoard : imageList
# gameBoard() is a list of eight line segments, which are the hash marks
# of the tic tac toe board.
# The game board is a 300 by 300 pixel rectangle,
# whose bottom left coner is point (100,100) and upper right corner is point (400,400)
# The game board is divided into 9 boxes evenly and each box is 100 by 100 pixel.
def gameBoard():
    L1 = (200,100,200,400)
    L2 = (300,100,300,400)
    L3 = (100,200,400,200)
    L4 = (100,300,400,300)
    L5 = (100,100,400,100)
    L6 = (400,100,400,400)
    L7 = (100,100,100,400)
    L8 = (100,400,400,400)
    Lines = [L1,L2,L3,L4,L5,L6,L7,L8]
    return Lines

# gameBoard1: imageList
# gameBoard1() is a list of seven line segments, which are the buttons
# of the tic tac toe selection screen.
# The board is 300 by 400 pixel rectangle, whose bottom left corner is
# point (100,100) and upper right corner is point (400,500).
# The game board is divided into 4 even boxes, with each box being 400 by 100 pixels.
def gameBoard1():
    L1 = (100,50,400,50)
    L2 = (400,50,400,450)
    L3 = (400,450,100,450)
    L4 = (100,450,100,50)
    L5 = (100,150,400,150)
    L6 = (100,250,400,250)
    L7 = (100,350,400,350)
    Lines = [L1,L2,L3,L4,L5,L6,L7]
    return Lines

# selections: imageList
# selections() is a list of text images, which are the titles of the buttons
# for the selectionScreen().
def selections():
    easyAI = [("Click here for Easy AI",250,400,12)]
    mediumAI = [("Click here for Medium AI",250,300,12)]
    hardAI = [("Click here Hard AI",250,200,12)]
    twoPlayer = [("Click here for Two Players",250,100,12)]
    title = [("Please select a mode below",250,475,12)]
    buttons = easyAI + mediumAI + hardAI + twoPlayer + title
    return buttons

# twoPlayerSuccessor: state x point -> state
# twoPlayerSuccessor(S,p) is the state resulting from clicking point
# p in state S 
def twoPlayerSuccessor(S,p):
    # If the game is not over and an empty cell is clicked, return the game state
    # place an 'x' or 'o' in that cell, depending on whose turn it is in S.
    # Since we must do this for every cell, it uses a for-loop. You can think
    # of this as a short way of writing a separate if statement for each cell.
    for c in range(1,10):
        if not over(S) and insideCell(p,c) and empty(c,S):
            return insert(turn(S),c,S)
    # If the game is over and the playAgain buttton, return initial state.
    if over(S) and clickedPlayAgain(p): return initialState()
    # otherwise, return input S
    else: return S
    
# overSuccessor: state x point -> state
# if S is a state that is over, overSuccessor(S,p) is the state resulting from clicking
# point p in state S.
def overSuccessor(S,p):
    if over(S) and clickedPlayAgain(p): return initialState()
    else: return S

# AISuccessor: state x point -> state
# If S is not over, it is x's turn in S, and S[2] is one of the  three AI
# modes, then AISuccessor(S,p) is the state resulting from clicking point
# p in state S.
def AISuccessor(S,p):
    for c in range(1,10):
        # over(S), insideCell(p,c), and empty(c,S) are the functions from tic tac toe version 1.0
        if not over(S) and insideCell(p,c) and empty(c,S):
           newS = insert('x',c,S)  
           if over(newS): 
                # x won the game or filled the last empty square
                # the game is over.
                return newS  
           else: 
               # It is the AI player's move    
               return insert('o', AImove(newS),newS)
    if over(S) and clickedPlayAgain(p): return initialState()
    else: return S

# AImove : state -> cell
# If S is a state in which it is o's move, AImove(S) is the 
# cell in which 'o' will move. 
def AImove(S):
    mode = S[2]
    if mode == 'easyAI': return easyAImove(S)
    elif mode == 'mediumAI': return medAImove(S)
    elif mode == 'hardAI': return hardAImove(S)

# easyAImove: state -> cell
# If S is not over, S is a state in which it is o's move and S[2] is "easyAI",
# easyAImove(S) is the cell in which 'o' will move based on 'easyAI' strategy
def easyAImove(S):
    cells = [1,2,3,4,5,6,7,8,9]
    x = randint(0,len(cells)-1)
    cell = cells[x]
    if empty(cell,S):
        print(cell)
        return cell
    if not empty(cell,S): return easyAImove(S)
        
# medAImove: state -> cell
# If S is not over, S is a state in which it is o's move and S[2] is "mediumAI",
# medAImove(S) is the cell in which 'o' will move based on 'mediumAI' strategy
def medAImove(S):
    for c in range(1,10):
        if empty(c,S):
            S1=insert('o',c,S)
            if winner(S1,'o'):
                return c
    for c in range(1,10):
        if empty(c,S):
            S1=insert('x',c,S)
            if winner(S1,'x'):
                return c
    for c in range(1,10):
        if empty(c,S):
            S1=insert('o',c,S)
            if not (winner(S1,'o') or winner(S1,'x')):
                return c

# hardAImove: state -> cell
# hardAImove(S) is a move to win all the time, if no win is possible, tie.
def hardAImove(S):
    for c in range(1,10):
        if empty(c,S):
            S1=insert('o',c,S)
            if winner(S1,'o'):
                return c
    for c in range(1,10):
        if empty(c,S):
            S1=insert('x',c,S)
            if winner(S1,'x'):
                return c
    for c in range(1,10):
        if empty(c,S) and safe(insert(turn(S),c,S)):
            return c

# safe: state -> bool
# A state S is safe(S) if player 'o' can force a win or tie from S.
# If over(S) and x has not won, then S is safe.
# If x's move, S is safe iff all of its legal successors are safe.
# If o's move, S is safe iff at least one of its legal successors are safe.
def safe(S):
    if over(S): return not threeXInRow(S)
    if turn(S)=='o': return someSafeSuccessor(S)
    if turn(S)=='x': return allSafeSuccessor(S)

# someSafeSuccessor: state -> bool
# If S is a state, someSafeSuccessor(S) means that S has
# at least one safe successor.
def someSafeSuccessor(S):
    flag = False
    for x in successors(S):
        if safe(x): flag = True
    return flag

# allSafeSuccessors: state -> Bool
# If S is a state, allSafeSuccessors(S) means that every
# successor of S is safe.
def allSafeSuccessor(S):
    flag = True
    for x in successors(S):
        if not safe(x): flag = False
    return flag

# successors: state -> stateList
# successors(S) is a list whose members are all of the successors of S.
def successors(S):
    successors=[]
    for i in range(1,10):
        if empty(i,S):
            aSuccessor=insert(turn(S),i,S)
            successors.append(aSuccessor)
    return successors

# insert: player x cell x state -> state
# If it is player p's turn and cell c is empty in state S,
# then insert(p,c,S) is the state resulting from player p
# moving in cell c in state S.
def insert(p,c,S):
    if p=='x': return (S[0]+[c],S[1],S[2])
    if p=='o': return (S[0],S[1]+[c],S[2])

# turn : state -> player
# If S is a state occurring in a game that is not over,
# then turn(S) is 'x' if it is x's turn in state S, and
# 'o' if it is o's turn in S.
# Assuming the same player hasn't moved more than once at a time.
def turn(S):
    if not over(S) and len(S[0])==len(S[1]): return 'x'
    else: return 'o'

# over: State -> bool
# over(S) means that the game is over in state S.
def over(S):
    return (winner(S,'x') or winner(S,'o') or full(S))

# full: state -> bool
# full(S) means that the board is full in state S.
def full(S):
    return (len(S[0])+len(S[1]))==9

# empty: cell x state -> bool
# empty(c,S) means that cell C is empty in state S.
def empty(c,S):
    return not (c in S[0] or c in S[1])

# winner: state x player -> bool
# winner(S,P) returns True if player P has won the game in game state S and False otherwise.
def winner(S,p):
    if p=='x':
        return threeXInRow(S)
    if p=='o':
        return threeOInRow(S)
    else: return False

# threeOInRow: state -> bool
# threeOInRow(S) means that in state S, player 'o' has three in a row.
def threeOInRow(S):
    win=False
    #horizontal wins
    if S[1].count(1) and S[1].count(2) and S[1].count(3):
        win=True
        return win
    if S[1].count(4) and S[1].count(5) and S[1].count(6):
        win=True
        return win
    if S[1].count(7) and S[1].count(8) and S[1].count(9):
        win=True
        return win
    #vertical wins
    if S[1].count(1) and S[1].count(4) and S[1].count(7):
        win=True
        return win
    if S[1].count(2) and S[1].count(5) and S[1].count(8):
        win=True
        return win
    if S[1].count(3) and S[1].count(6) and S[1].count(9):
        win=True
        return win
    #diagonal wins
    if S[1].count(1) and S[1].count(5) and S[1].count(9):
        win=True
        return win
    if S[1].count(3) and S[1].count(5) and S[1].count(7):
        win=True
        return win
    
# threeXInRow: state -> bool
# threeXInRow(S) means that in state S, player 'x' has three in a row.
def threeXInRow(S):
    win=False
    #horizontal wins
    if S[0].count(1) and S[0].count(2) and S[0].count(3):
        win=True
        return win
    if S[0].count(4) and S[0].count(5) and S[0].count(6):
        win=True
        return win
    if S[0].count(7) and S[0].count(8) and S[0].count(9):
        win=True
        return win
    #vertical wins
    if S[0].count(1) and S[0].count(4) and S[0].count(7):
        win=True
        return win
    if S[0].count(2) and S[0].count(5) and S[0].count(8):
        win=True
        return win
    if S[0].count(3) and S[0].count(6) and S[0].count(9):
        win=True
        return win
    #diagonal wins
    if S[0].count(1) and S[0].count(5) and S[0].count(9):
        win=True
        return win
    if S[0].count(3) and S[0].count(5) and S[0].count(7):
        win=True
        return win

# insideCell : point x cell -> bool
# insideCell(p,C) means that point p is inside cell C on the board.
def insideCell(p,c):
##    (x,y)=p
##    return 100+100*((c-1)%3)<x<200+100*((c-1)%3) and 300-100*((c-1)//3)<y<400-100*((c-1)//3)

    if c==1: return 100<p[0]<200 and 300<p[1]<400
    if c==2: return 200<p[0]<300 and 300<p[1]<400
    if c==3: return 300<p[0]<400 and 300<p[1]<400
    if c==4: return 100<p[0]<200 and 200<p[1]<300
    if c==5: return 200<p[0]<300 and 200<p[1]<300
    if c==6: return 300<p[0]<400 and 200<p[1]<300
    if c==7: return 100<p[0]<200 and 100<p[1]<200
    if c==8: return 200<p[0]<300 and 100<p[1]<200
    if c==9: return 300<p[0]<400 and 100<p[1]<200
    else: return False
    
# playerTokens: State -> imageList
# playerTokens(S) is a list of images, one for each mark ('x' or 'o') on
# the board in state S.
def playerTokens(S):
    return xTokens(S)+oTokens(S)

# xTokens: State -> imageList
# xTokens(S) is a list of images, one for each mark 'x' in the state S.
def xTokens(S):
    xToks = []
    for c in S[0]:
        xToks = xToks + xImage(c)
    return xToks

# oTokens: State -> imageList
# oTokens(S) is a list of images, one for each mark 'o' in the state S.        
def oTokens(S):
    oToks = []
    for c in S[1]:
        oToks = oToks + oImage(c)
    return oToks

# oImage: cell -> imageList
# oImage(c) is a list of images based on cell c.
def oImage(c):
    return [("O",cellCenterX(c),cellCenterY(c),20)]

# xImage: cell -> imageList
# xImage(c) is a list of images based on cell c.
def xImage(c):
    return [("X",cellCenterX(c),cellCenterY(c),20)]

# cellCenterX: cell -> int
# cellCenterX(c) is an int based on cell c.
def cellCenterX(c):
    if (c==1 or c==4 or c==7):
        return 150
    if (c==2 or c==5 or c==8):
        return 250
    if (c==3 or c==6 or c==9):
        return 350
    
# cellCenterY: cell -> int
# cellCenterY(c) is a int based on cell c.
def cellCenterY(c):
    if (c==1 or c==2 or c==3):
        return 350
    if (c==4 or c==5 or c==6):
        return 250
    if (c==7 or c==8 or c==9):
        return 150
'''
CellCenter1=(150,350)
CellCenter2=(250,350)
CellCenter3=(350,350)
CellCenter4=(150,250)
CellCenter5=(250,250)
CellCenter6=(350,250)
CellCenter7=(150,150)
CellCenter8=(250,150)
CellCenter9=(350,150)
'''

# playAgainButton: imageList
# playAgainButton() is a list of images for a box in the upper right
# corner containing the text "Play Again".
# The button box is a rectangle whose bottom left corner is point (400,425)
# and upper right corner is point (500,475)
def playAgainButton():
    if not over(S):
        playAgain = ''
        playAgainFrame = []
    else:
        playAgain = "Click here to play again"
        playAgainFrame = [(400,400,600,400),(400,400,400,500)]
        playAgainText = [(playAgain,500,450,12)]+playAgainFrame
    return playAgainText
 
# clickedPlayAgain: point -> bool
# clickedPlayAgain(p) is true when the point is in the 'Play Again' button box, otherwise false.
def clickedPlayAgain(p):
    if playAgainButton(): return p[0]<600 and p[0]>400 and p[1]<500 and p[1]>400

# turnMessage: state -> imageList
# turnMessage(S) is a list, whose only element is the text message about whose turn it is in game state S.
# The text message is centered at point (100,450) of height 15 in pixel
def turnMessage(S):
    message = []
    if turn(S) == 'x':
        playerXturn = [("Player X's turn",100,450,15)]
        message = message + playerXturn
    if turn(S) == 'o':
        playerOturn = [("Player O's turn",100,450,15)]
        message = message + playerOturn
    return message

# winnerMessage(S) : state -> imageList
# If S is a state in which the game is over, winnerMessage(S) is
# a list whose only element is a text message in the upper left corner
# of the screen, saying who won the game (or that the cat won if it is
# a tie).
def winnerMessage(S):
    winMessage = []
    if over(S) == winner(S,'x'):
        printXWonGame=[("Player X Won!",60,450,12)]
        winMessage = winMessage + printXWonGame
    if over(S) == winner(S,'o'):
        printOWonGame=[("Player O Won!",60,450,12)]
        winMessage = winMessage + printOWonGame
    if full(S) and not (winner(S,'x') or winner(S,'o')):
        tie=[("Cat won",50,450,15)]
        winMessage = winMessage + tie
    return winMessage

######################################################################
######################################################################
######################################################################
# TPGE GAME ENGINE
#
# Student code is linked with this code to create a game.

# displaySize() is the size of the display window, (width, height)

def displaySize() : return (600,500)
from graphics import *


# If x is an image, imageKind(x) is the type of image x is:
# 'circle', 'text', or 'lineSegment'

def imageKind(x):
    if len(x)==3 : return 'circle'
    elif type(x[0])== str :return 'text'
    else : return 'lineSegment'

# If x is an image, convert(x) is the corresponding image in the
# graphics.py library. We turn the screen upside down so that the origin
# is in the lower left corner, so it matches what they learn in algebra
# class.


def convert(x):
    if imageKind(x)=='circle': return convertCircle(x)
    elif imageKind(x)=='lineSegment': return convertLine(x)
    elif imageKind(x)=='text' : return convertText(x)

def convertLine(x):
    (W,H) = displaySize()
    P1 = Point(x[0],H - x[1])
    P2 = Point(x[2],H - x[3])
    return Line(P1,P2)

def convertText(x):
    (W,H) = displaySize()
    center = Point(x[1],H-x[2])
    string = x[0]
    size = x[3]
    T = Text(center,string)
    T.setSize(size)
    return T

def convertCircle(x):
    (W,H) = displaySize()
    center = Point(x[0],H-x[1])
    radius = x[2]
    return Circle(center,radius)

# Create a window to play in
display = GraphWin("Tic Tac Toe 2.0", displaySize()[0], displaySize()[1])


# The main loop
# Set the state, draw the display, get a mouse click, set the new state,
# and repeat until the user closes the window.

S = initialState()
images = [convert(x) for x in displayImages(S)]

while(True):
    for x in images: x.draw(display)
    c = display.getMouse()
    click = (c.getX(),displaySize()[1] - c.getY())
    S = successor(S,click)
    for I in images: I.undraw()
    images = [convert(x) for x in displayImages(S)]
