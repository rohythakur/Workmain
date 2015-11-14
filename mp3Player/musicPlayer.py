__author__ = 'eeamesX'
import pygame

import os, sys
import time
from datetime import datetime


pygame.mixer.pre_init(18000, -16, 2, 2048) # setup mixer to get sound right


pygame.init()

white = (255,255,255)
black = (0,0,0)


red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)



backImg = pygame.image.load('back.png')
backImg = pygame.transform.scale(backImg, (50,50))
forImg = pygame.image.load('forward.png')
forImg = pygame.transform.scale(forImg, (50,50))
stopImg = pygame.image.load('play.png')
stopImg = pygame.transform.scale(stopImg, (50,50))
exitImg = pygame.image.load('exit.png')
exitImg = pygame.transform.scale(stopImg, (50,50))
intelImg = pygame.image.load('exit.png')
intelImg = pygame.transform.scale(stopImg, (50,50))


display_width = 500
display_height = 400

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Audio Player')




musicExit = False


def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

def text_objects(text, color,size = "small"):

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()
    #print click
    #print "starting the button"
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        #print "made it here"
        if click[0] == True and action != None:
            #print "at this part"
            if action == "quit":
                print("clicked quit")
                pygame.quit()
                quit()

            if action == "forward":
                print("clicked forward")
                forwardButton()

            if action == "play":
                print("clicked play")
                Play()

            if action == "back":
                print("clicked back")
                backButton()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)




def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False



def forwardButton():
    pass

def backButton():
    pygame.mixer.music.rewind()




def Play():
    a = pygame.mixer.Sound("test.wav")
    print("length",a.get_length())
    soundfile = 'test.wav'
    pygame.mixer.init()
    pygame.mixer.music.load(soundfile)
    #pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1.0)
    time.sleep(1)
    pygame.mixer.music.play()



    return pygame.mixer.music.get_pos()



def stopmusic():

    pygame.mixer.music.stop()



def playloop():
    print 'starting'
    fps = 30
    start=datetime.now()
    # Set up clock
    clock = pygame.time.Clock()




    print datetime.now()-start
    while not musicExit:



        time.sleep(0.020)


        events = pygame.event.get()
        for event in events:

            if event.type == pygame.QUIT:
                sys.exit()



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.Q:
                    sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                 #print "mouse at (%d, %d)" % event.pos
                pass


        gameDisplay.fill(white)






        button("", 225,200,50,50, white, white, action="play")
        button("", 75,200,50,50, white, white, action="back")
        button("", 375,200,50,50, white, white, action="forward")

        button("", 450,350,50,50, white, white, action ="quit")
        gameDisplay.blit(backImg, (75,200))

        gameDisplay.blit(stopImg, (225,200))
        gameDisplay.blit(forImg, (375,200))
        gameDisplay.blit(intelImg, (375,200))
        gameDisplay.blit(exitImg, (450,350))
        clock.tick(fps)
        pygame.display.flip()





    pygame.quit()
    quit()





playloop()
pygame.quit()