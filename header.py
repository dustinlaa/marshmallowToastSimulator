# HackNJIT 2022 - Adrianna Rust, Andrew Dickman, Dustin La, and Hrishikesh Sakunala
import random

# Globals
global limit
limit = random.randint(20,50)
global marshToast
marshToast = 0
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

def getLimit(): # Generates a random max limit between 20 and 50 (going over results in burnt)
    limit = random.randint(20,50)
    return limit

def reset(): # Resets both global variables that would need to be reset
    global marshToast
    global currStreak
    global checkStreak
    marshToast = 0
    checkStreak = False

def holdOver(time, limit): # The amount of time holding marshmallow over campfire and its result
    #time = hold over choice, limit = limit
    if time == 1:
        randTimes = random.randint(limit//12,limit//9) # Between 1/12 and 1/9 the limit
    elif time ==2:
        randTimes = random.randint(limit//8,limit//5) # Between 1/8 and 1/5 the limit
    elif time == 3:
        randTimes = random.randint(limit//4,limit//2) # Between 1/4 and 1/2 the limit
    return randTimes

def toastMarshmallow(time): # Roasts marshamllow based on duratino of time and adds it to the total
    global marshToast
    global randTime
    randTime = holdOver(time, limit)
    marshToast = randTime + marshToast 

def incrStreak(case): # Increments streak for each golden brown marshmallow
    global currStreak
    if case == 4:
        currStreak = currStreak + 1
    else:
        currStreak = 0
    return currStreak

def stopToasting(case,marshToast): # Final status of marshmallow
    statement = []
    if case == 1: # Squishy
        statement = ["Not even close! Your lil marshmallow was cooked for " + str(marshToast) + " seconds", "and looks pretty squishy"]
    elif case == 2: # Starting to get brown
        statement = ["Somewhat passable. Your lil marshmallow was cooked for " + str(marshToast) + " seconds", "and looks slightly brown and a lil scrumptious"]
    elif case == 3: # Very nice brown
        statement = ["Oooh you almost had it. Your lil marshmallow was cooked for " + str(marshToast) + " seconds", "and looks very good with a nice brown tint"]
    elif case == 4: # Golden Brown
        statement = ["Congrats! Your lil marshmallow was cooked for " + str(marshToast) + " seconds", "and looks a perfect golden brown :O"]
    elif case == 5: # Burnt
        statement = ["Your marshmallow burnt and is now icky :("]
    return statement

def checkIfBurnt(limit, marshToast): # Checks status of Marshmallow
    distToBurnt = limit - marshToast
    global case
    if (distToBurnt > .6*limit): # > 60% of the limit
        status = "Your Marshmallow is still pretty squishy"
        case = 1
    elif (distToBurnt >= .35*limit): # > 35% of the limit
        status = "Your Marshmallow is starting to get brown"
        case = 2
    elif (distToBurnt >= .1*limit): # >= 10% of the limit
        status = "Your Marshmallow is a very nice brown. ;)"
        case = 3
    elif (distToBurnt < limit and distToBurnt > 0): # over the limit and results in burnt
        status = "Your Marshmallow is golden brown uwu"
        case = 4
    else:
        status = "burnt lol"
        case = 5
    return status,case

def getHighScore(): # Gets the current high school
    global scoreArray
    scoreArray.sort(reverse=True)
    highScore = scoreArray[0]
    return highScore