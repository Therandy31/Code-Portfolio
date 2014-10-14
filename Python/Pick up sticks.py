# Randall Harper
# Pick-up-sticks
# 8/11/14

'''
Game Guide

Two players play the game, 'player 1' and 'player 2'.
The players will take turns, with the player 1 making the first move.
The game starts with 15 sticks displayed on the game board.
A move consists of either taking 1, 2, or 3 sticks from the board.
Players select the number of sticks they wish to take by clicking inside the circle that is labeled with that number.
The player who takes the last stick loses the game.


Data model for Pick-up-sticks is as follows:
A *player* is either 'player 1' or 'player 2'.
A *winner* is either '1' or '2'.
*sticks* is the remaining amount of sticks on the board.
A game state is a tuple of the form(s,p,w), where s is an integer in the range of [0,16), p is a player name, and w is a winner.
For example, the game state (12,'player 1','None') formally represents a state in which there are 12 sticks left on the board, and it is player 1's turn and there is no winner yet.
'''

# 1. Implement initialState()
# initialState(): state -- initialState() is the initial state of the game.
def initialState():
	s = (15,'player 1','None')
	return s

# 2. Implement sticksOnBoard(s)
# sticksOnBoard(s): state -> imageList -- sticksOnBoard(s) is a list of line segements representing the sticks on the board in a game state s.
# The board is a 600 by 500 pixel window and the sticks are displayed within a rectangle, whose bottom left corner is (0,0) and upper right corner is (450, 300).

def sticksOnBoard(s):
	(sticks,p,w) = s
	board = []
	k = 30

	for i in range[0,15):
		lines = [(30+i*k,100,30+i*k,200)]

	if w == 'None': return lines[0:sticks]
	else: return lines[0]

# 3. Implement successor(s,point)
'''
successor(s,point): state x point -> state -- successor(s,point) is the state resulting from clicking point in state s.
If there are more than 1 sticks left on the board and the point is within either of the following 3 circles, then it is *valid*, and *invalid* otherwise.
The 3 circles described in the form of the date model in "The Tiny Python Game Engine" are:
circle1: (125, 350, 15), circle2 = (225, 350, 15), and circle3 = (325, 350, 15).
If the point is valid, then successor(s,point) is the state resulting from clicking point in state s.
If the point is invalid, then successor(s,point) is the same state as the current one.
'''

def successor(s,point):
	(sticks,p,w) = s
	if s[0] == 1 and s[1] == 'player 1':
		(1,'player 1','2') = s
		return s
	elif s[0] == 1 and s[1] == 'player 2':
		(1,'player 2','1') = s
		return s

	if s[1] == 'player 1':
		if inCircleOne(point):	A = s[0]-1
			return (A,'player 2',s[2])
		elif inCircleTwo(point):	A = s[0]-2
			return (A,'player 2',s[2])
		elif inCircleThree(point):	A = s[0]-3
			return (A,'player 2',s[2])
		else: return s

	else:
		if inCircleOne(point):	A = s[0]-1
			return (A,'player 1',s[2])
		elif inCircleTwo(point):	A = s[0]-2
			return (A,'player 1',s[2])
		elif inCircleThree(point):	A = s[0]-3
			return (A,'player 1',s[2])
		else: return s

def inCircleOne(point):
	(x,y) = point
	c1 = 125
	c2 = 350
	r = 15
	return (x-c1)**2+(y-c2)<(r**2)

def inCircleTwo(point):
	(x,y) = point
	c1 = 225
	c2 = 350
	r = 15
	return (x-c1)**2+(y-c2)<(r**2)

def inCircleThree(point):
	(x,y) = point
	c1 = 325
	c2 = 350
	r = 15
	return (x-c1)**2+(y-c2)**2<(r**2)

# displayImages(s): state -> imageList -- displayImages(s) is a list of images to display on the screen in a state s.
# For this game, it consists of a text message and sticks displayed on the game board.
# The board is a 600 by 500 pixel window
def displayImages(s):
	images = textMessage(s) + sticksOnBoard(s)
	return images

# textMessage(s): state -> imageList -- textMessage(s) is a list of images displaying game messages on the board in game state s.
def textMessage(s):
	(sticks,p,w) = s

	#player
	if w == 'None':
		if p == 'player 1':	player = "Player 1's turn"
		else: player = "Player 2's turn"
	else:
		player = ''
	playerText = [(player,50,540,15)]

	#winner
	if w == '1':	winner = "Player 1 wins!"
	elif w == '2':	winner = "Player 2 wins!"
	else: winner = ''
	winnerText = [(winner,525,450,15)]

	#play again
	if not(w == '1' or '2'):
		playAgain = ''
		playAgainFrame = []
	else:
		playAgain = "Click here to play again."
		playAgainFrame = [(450,415,600,415)]+[(600,415,600,385)]+[(600,385,450,385)]+[(450,385,450,415)]
	playAgainText = [(playAgain,525,500,15)]+playAgainFrame

	#move option
	moveOption = "How many sticks would you like to take? (Click inside a circle)"
	moveOptionText = [(moveOption,225,375,15)]

	#circles for move option
	option1 = [('1',95,350,15)]+[(125,350,15)]
	option2 = [('2',195,350,15)]+[(225,350,15)]
	option3 = [('3',295,350,15)]+[(325,350,15)]
	options = option1 + option2 + option3

	#number of sticks left
	sticksLeft = str(sticks) + "sticks left."
	sticksLeft = [(sticksLeft,225,50,15)]

	return playerText + winnerText + playAgainText + moveOptionText + sticksLeft + options

#over(s): state -> Bool
# If there are less than 2 sticks left on the board, then over(s) is True, and False otherwise.
def over(s):
	(sticks,p,w) = s
	return sticks<2

#playAnotherGame(point): point -> Bool
# If the game is over and point is the point in the rectangle, whose bottom left corner is (385,415) and upper right corner is (415,500), then playAnotherGame(point) is True, and False otherwise.
def playAnotherGame(point):
	(x,y) = point
	return x>475 and y<500 and x>385 and y<415


###################################################################
###################################################################
# Tiny Python Game Engine

# displaySize() is the size of the display window, (width, height)
def displaySize(): return (600,500)
from graphics import *

# If x is an image, imageKind(x) is the type of image x is:
# 'circle', 'text', or 'lineSegment'
def imageKind(x):
	if len(x) == 3: return 'circle'
	elif type(x[0]) == str: return 'text'
	else: return 'lineSegment'

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
display = GraphWin("Sticks pick up", displaySize()[0], displaySize()[1])


# The main loop
#
# Set the state, draw the display, get a mouse click, set the new state,
# and repeat until the user closes the window.

S = initialState()
images = [convert(x) for x in displayImages(S)]

while(True):
    for x in images: x.draw(display)
    c = display.getMouse()
    click = (c.getX(),displaySize()[1] - c.getY())
    if over(S) and playAnotherGame(click):
        S=initialState()
    else: S = successor(S,click)
    for I in images: I.undraw()
    images = [convert(x) for x in displayImages(S)]
  
