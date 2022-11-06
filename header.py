# HackNJIT 2022 - Adrianna Rust, Andrew Dickman, Dustin La, and Hrishikesh Sakunala
import random

#Globals
#---------------
global limit
limit = random.randint(20,50)
global marshCook
marshCook = 0
global randTime
randTime = 0
flag = False
global currStreak
currStreak = 0
case = 0
global scoreArray
scoreArray = [0]
global checkStreak
checkStreak = False
#--------------

def getLimit():
    limit = random.randint(20,50)
    return limit

def reset():
    #resets both global variables that would need to be reset
    global marshCook
    global currStreak
    global checkStreak
    marshCook = 0
    checkStreak = False

def holdOver(time, limit):
    #time = hold over choice, limit = limit
    if time == 1:
        randTimes = random.randint(limit//12,limit//5)
    elif time ==2:
        randTimes = random.randint(limit//8,limit//3)
    elif time == 3:
        randTimes = random.randint(limit//4,limit//2)
    return randTimes

def roastMarshmallow(time):
    global marshCook
    global randTime
    randTime = holdOver(time, limit)
    marshCook = randTime + marshCook 

def incrStreak(case):
    global currStreak
    if case == 4:
        currStreak = currStreak + 1
    else:
        currStreak = 0
    return currStreak

def stopRoasting(case,marshCook):
    #case and time
    statement = []
    if case == 1:
        statement = ["Not even close! Your lil marshmallow was cooked for " + str(marshCook) + " seconds,", "and looks pretty squishy"]
    elif case == 2:
        statement = ["Somewhat passable. Your lil marshmallow was cooked for " + str(marshCook) + " seconds,", "and looks slightly brown and a lil scrumptious"]
    elif case == 3:
        statement = ["Oooh you almost had it. Your lil marshmallow was cooked for " + str(marshCook) + " seconds,", "and looks very good with a nice brown tint"]
    elif case == 4:
        statement = ["Congrats! Your lil marshmallow was cooked for " + str(marshCook) + " seconds,", "and looks a perfect golden brown :O"]
    elif case == 5:
        statement = ["Your marshmallow burnt and is now icky :("]
    return statement

def checkIfBurnt(limit, marshCook):
    distToBurnt = limit - marshCook
    global case
    if (distToBurnt > .6*limit):
        status = "Your Marshmallow is still pretty squishy"
        case = 1
    elif (distToBurnt >= .35*limit): 
        status = "Your Marshmallow is starting to get brown"
        case = 2
    elif (distToBurnt >= .1*limit):
        status = "Your Marshmallow is a very nice brown. ;)"
        case = 3
    elif (distToBurnt < limit and distToBurnt > 0):
        status = "Your Marshmallow is golden brown uwu"
        case = 4
    else:
        status = "burnt lol"
        case = 5
    return status,case

def getHighScore():
    global scoreArray
    scoreArray.sort(reverse=True)
    highScore = scoreArray[0]
    return highScore

def continueGame(startGame):
    if (startGame == True):
        start()
    elif startGame == False:
        print("Your current high score is:", getHighScore())
        print("Have a good day {}!".format(usern))
        return False
    else:
        print("Wrong input, please enter (Y) or (N).")

def inGame():
    global flag
    while flag:
        roastMarshmallow()

def start():
    global flag
    flag = True