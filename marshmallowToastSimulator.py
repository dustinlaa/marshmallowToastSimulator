# HackNJIT 2022 - Adrianna Rust, Andrew Dickman, Dustin La, and Hrishikesh Sakunala
import pygame
import ctypes
import header
from pygame.locals import *
from pygame import mixer
import sys

from button import Button

pygame.init()

width = 1280
height = 720
global currentStreak
currentStreak = False
SCREEN = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

BG = pygame.image.load("assets/camping_background.jpg")

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

# pressing play leads to the duration screen
def play(): # Play Screen
    while True:
        header.getLimit()
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#7d7992")
        # Background
        DEFAULT_IMAGE_POSITION = (70, 250)
        DEFAULT_IMAGE_SIZE = (400, 500)
        image = pygame.image.load("assets/art_timer.jpg").convert()
        image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
        SCREEN.blit(image, DEFAULT_IMAGE_POSITION)

        # Play info
        PLAY_TEXT = get_font(16).render("How long of a duration would you like to hold your marshmallow over the fire?", True,
                                        "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # Short button
        PLAY_SHORT = Button(image=None, pos=(640, 260), text_input="Short", font=get_font(50), base_color="#d7fcd4",
                            hovering_color="White")
        PLAY_SHORT.changeColor(PLAY_MOUSE_POS)
        PLAY_SHORT.update(SCREEN)

        # Medium button
        PLAY_MEDIUM = Button(image=None, pos=(640, 360), text_input="Medium", font=get_font(50), base_color="#d7fcd4",
                             hovering_color="White")
        PLAY_MEDIUM.changeColor(PLAY_MOUSE_POS)
        PLAY_MEDIUM.update(SCREEN)

        # Long button
        PLAY_LONG = Button(image=None, pos=(640, 460), text_input="Long", font=get_font(50), base_color="#d7fcd4",
                           hovering_color="White")
        PLAY_LONG.changeColor(PLAY_MOUSE_POS)
        PLAY_LONG.update(SCREEN)

        # Displays Highscore
        highscore = "HIGHSCORE: " + str(header.getHighScore())
        HIGHSCORE_TEXT = get_font(20).render(highscore, True, "White")
        HIGHSCORE_RECT = HIGHSCORE_TEXT.get_rect(center=(640, 550))
        SCREEN.blit(HIGHSCORE_TEXT,HIGHSCORE_RECT)

        # Events for Short, Medium, Long
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_SHORT.checkForInput(PLAY_MOUSE_POS):
                    header.toastMarshmallow(1)
                    cont()
                if PLAY_MEDIUM.checkForInput(PLAY_MOUSE_POS):
                    header.toastMarshmallow(2)
                    cont()
                if PLAY_LONG.checkForInput(PLAY_MOUSE_POS):
                    header.toastMarshmallow(3)
                    cont()
        pygame.display.update()

def cont(): # Continue Screen
    while True: 
        CONT_MOUSE_POS = pygame.mouse.get_pos()

        # Changes background base on marshmalow status
        if header.case == 1: # Squishy
            SCREEN.fill("#ab6589")
        if header.case == 2: # Starting to get brown
            SCREEN.fill("#bb6977")
        if header.case == 3: # Very nice brown
            SCREEN.fill("#c86a68")
        if header.case == 4: # Golden Brown
            SCREEN.fill("#df7555")
        if header.case == 5: # Burnt
            SCREEN.fill("#886372")

        # Seconds toasted
        currResult = "Your marshmallow has been toasted for " + str(header.randTime) + " seconds"
        CONT_TEXT = get_font(20).render(currResult, True, "White")
        CONT_RECT = CONT_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(CONT_TEXT, CONT_RECT)

        # Total seconds toasted
        total = "Total: " + str(header.marshToast) + " seconds"
        CONT_TEXT2 = get_font(20).render(total, True, "White")
        CONT_RECT2 = CONT_TEXT2.get_rect(center=(640, 100))
        SCREEN.blit(CONT_TEXT2, CONT_RECT2)

        # Checks if Marshallow has been burnt
        status, case = header.checkIfBurnt(header.limit, header.marshToast)

        # If burnt, immediately go to results
        if case == 5:
            results()
        
        # Status message of marshmallow
        CONT_TEXT3 = get_font(15).render(str(status), True, "White")
        CONT_RECT3 = CONT_TEXT3.get_rect(center=(640, 150))
        SCREEN.blit(CONT_TEXT3, CONT_RECT3)

        # Continue and Stop Buttons
        CONTINUE_BUTTON = Button(image=None, pos=(320, 650),
                             text_input="CONTINUE", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        STOP_BUTTON = Button(image=None, pos=(960, 650),
                             text_input="STOP", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        CONTINUE_BUTTON.changeColor(CONT_MOUSE_POS)
        CONTINUE_BUTTON.update(SCREEN)

        STOP_BUTTON.changeColor(CONT_MOUSE_POS)
        STOP_BUTTON.update(SCREEN)

        # Changes image based on marshmallow status
        if case == 1: # Squishy
            DEFAULT_IMAGE_POSITION = (435, 180)
            DEFAULT_IMAGE_SIZE = (400, 400)
            image = pygame.image.load("assets/art_squishy_white.jpg").convert()
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            SCREEN.blit(image, DEFAULT_IMAGE_POSITION)
        if case == 2: # Starting to get brown
            DEFAULT_IMAGE_POSITION = (435, 180)
            DEFAULT_IMAGE_SIZE = (400, 400)
            image = pygame.image.load("assets/little_brown.jpg").convert()
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            SCREEN.blit(image, DEFAULT_IMAGE_POSITION)
        if case == 3: # Very nice brown
            DEFAULT_IMAGE_POSITION = (435, 180)
            DEFAULT_IMAGE_SIZE = (400, 400)
            image = pygame.image.load("assets/very_nice_brown.jpg").convert()
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            SCREEN.blit(image, DEFAULT_IMAGE_POSITION)
        if case == 4: # Golden Brown
            DEFAULT_IMAGE_POSITION = (435, 180)
            DEFAULT_IMAGE_SIZE = (400, 400)
            image = pygame.image.load("assets/golden_brown.jpg").convert()
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            SCREEN.blit(image, DEFAULT_IMAGE_POSITION)
        if case == 5: # Burnt
            DEFAULT_IMAGE_POSITION = (435, 180)
            DEFAULT_IMAGE_SIZE = (400, 400)
            image = pygame.image.load("assets/art_burnt.jpg").convert()
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            SCREEN.blit(image, DEFAULT_IMAGE_POSITION)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE_BUTTON.checkForInput(CONT_MOUSE_POS):
                    play()
                if STOP_BUTTON.checkForInput(CONT_MOUSE_POS):
                    results()

        pygame.display.update()

def results(): # Results Screen
    global currentStreak
    status,case = header.checkIfBurnt(header.limit, header.marshToast)
    finalStatus = header.stopToasting(case, header.marshToast)

    # plays a success jingle if marshmallow is not burnt, else plays a fail jingle
    if case != 5:
        RESULTS_TEXT2 = get_font(16).render(finalStatus[1], True, "White")
        RESULTS_RECT2 = RESULTS_TEXT2.get_rect(center=(640, 150))
        SCREEN.blit(RESULTS_TEXT2, RESULTS_RECT2)
        channel3.play(pygame.mixer.Sound('assets/results.mp3'))
    else:
        channel4.play(pygame.mixer.Sound('assets/failresults.mp3'))
    while True:
        global checkStreak
        DEFAULT_IMAGE_POSITION = (0, 0)
        DEFAULT_IMAGE_SIZE = (1280, 720)
        image = pygame.image.load("assets/camping_background.jpg").convert()
        image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
        SCREEN.blit(image, DEFAULT_IMAGE_POSITION)

        RESULTS_MOUSE_POS = pygame.mouse.get_pos()
        # Shows correct marshmallow state
        if header.case == 1:
            DEFAULT_IMAGE_POSITION = (850, 180)
            DEFAULT_IMAGE_SIZE = (400, 400)
            image = pygame.image.load("assets/transparent_squishy_white.png").convert_alpha()
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            SCREEN.blit(image, DEFAULT_IMAGE_POSITION)
        if header.case == 2:
            DEFAULT_IMAGE_POSITION = (850, 180)
            DEFAULT_IMAGE_SIZE = (400, 400)
            image = pygame.image.load("assets/transparent_little_brown.png").convert_alpha()
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            SCREEN.blit(image, DEFAULT_IMAGE_POSITION)
        if header.case == 3:
            DEFAULT_IMAGE_POSITION = (850, 180)
            DEFAULT_IMAGE_SIZE = (400, 400)
            image = pygame.image.load("assets/transparent_very_nice_brown.png").convert_alpha()
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            SCREEN.blit(image, DEFAULT_IMAGE_POSITION)
        if header.case == 4:
            DEFAULT_IMAGE_POSITION = (850, 180)
            DEFAULT_IMAGE_SIZE = (400, 400)
            image = pygame.image.load("assets/transparent_golden_brown.png").convert_alpha()
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            SCREEN.blit(image, DEFAULT_IMAGE_POSITION)
        if header.case == 5:
            DEFAULT_IMAGE_POSITION = (850, 180)
            DEFAULT_IMAGE_SIZE = (400, 400)
            image = pygame.image.load("assets/transparent_burnt.png").convert_alpha()
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            SCREEN.blit(image, DEFAULT_IMAGE_POSITION)
        
        # Increases Streak if it was golden brown
        if header.checkStreak == False:
            currentStreak = header.incrStreak(case)
            header.checkStreak = True

        # Results Text
        RESULTS_TEXT = get_font(17).render(finalStatus[0], True, "White")
        RESULTS_RECT = RESULTS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(RESULTS_TEXT, RESULTS_RECT)

        # Creator Text
        CREATOR_TEXT = get_font(15).render("HackNJIT 2022", True, "#b68f40")
        CREATOR_RECT = CREATOR_TEXT.get_rect(center=(640, 670))
        CREATOR_TEXT2 = get_font(15).render("Adrianna Rust, Andrew Dickman, Dustin La, and Hrishikesh Sakunala", True, "#b68f40")
        CREATOR_RECT2 = CREATOR_TEXT2.get_rect(center=(640, 690))
        SCREEN.blit(CREATOR_TEXT, CREATOR_RECT)
        SCREEN.blit(CREATOR_TEXT2, CREATOR_RECT2)

        # Highscore Text
        highscore = "Highscore: " + str(header.getHighScore())
        HIGHSCORE_TEXT = get_font(20).render(highscore, True, "White")
        HIGHSCORE_RECT = HIGHSCORE_TEXT.get_rect(center=(640, 500))
        SCREEN.blit(HIGHSCORE_TEXT,HIGHSCORE_RECT)

        # Streak Text
        streak = "Your streak is: " + str(currentStreak)
        header.scoreArray.append(currentStreak)
        STREAK_TEXT = get_font(20).render(streak, True, "White")
        STREAK_RECT = STREAK_TEXT.get_rect(center=(640, 450))
        SCREEN.blit(STREAK_TEXT, STREAK_RECT)

        # Restart Button and Menu Button
        RESTART_BUTTON = Button(image=None, pos=(300, 600),
                             text_input="PLAY AGAIN", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        MENU_BUTTON = Button(image=None, pos=(960, 600),
                             text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        RESTART_BUTTON.changeColor(RESULTS_MOUSE_POS)
        RESTART_BUTTON.update(SCREEN)

        MENU_BUTTON.changeColor(RESULTS_MOUSE_POS)
        MENU_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(RESULTS_MOUSE_POS):
                    main_menu()
                if RESTART_BUTTON.checkForInput(RESULTS_MOUSE_POS):
                    header.reset()
                    play()

        pygame.display.update()

def main_menu(): # Main Menu
    while True:
        SCREEN.blit(BG, (0, 0))

        # text on page
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(30).render("Welcome to Marshmallow Toast Simulator!", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 80))

        menu_text = get_font(20).render("Press play to grab a marshmallow!", True, "White")
        SCREEN.blit(menu_text, (330, 130))

        menu_instructions = get_font(20).render("Your goal is to get your marshmallow",True, "White")
        SCREEN.blit(menu_instructions,(290,200))
        menu_instructions2 = get_font(20).render("to a scrumptious golden brown color.",True,"White")
        SCREEN.blit(menu_instructions2,(295,230))

        # Play Button and Quit Button
        PLAY_BUTTON = Button(image=None, pos=(320, 600),
                             text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(960, 600),
                             text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        # Creator Text
        CREATOR_TEXT = get_font(15).render("HackNJIT 2022", True, "#b68f40")
        CREATOR_RECT = CREATOR_TEXT.get_rect(center=(640, 670))
        CREATOR_TEXT2 = get_font(15).render("Adrianna Rust, Andrew Dickman, Dustin La, and Hrishikesh Sakunala", True, "#b68f40")
        CREATOR_RECT2 = CREATOR_TEXT2.get_rect(center=(640, 690))

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(CREATOR_TEXT, CREATOR_RECT)
        SCREEN.blit(CREATOR_TEXT2, CREATOR_RECT2)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Plays Background Music
mixer.init()
mixer.music.load('assets/background.mp3')
channel1 = pygame.mixer.Channel(0)
channel1.play(pygame.mixer.Sound('assets/background.mp3'),-1)
channel1.set_volume(0.5)
mixer.music.load('assets/firecrackle.mp3')
channel2 = pygame.mixer.Channel(1)
channel2.play(pygame.mixer.Sound('assets/firecrackle.mp3'),-1)
channel2.set_volume(0.3)

channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)

main_menu()