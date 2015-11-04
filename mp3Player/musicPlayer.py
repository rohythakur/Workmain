__author__ = 'eeamesX'
import pygame

import os, sys
import time



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


display_width = 500
display_height = 400

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Audio Player')


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

done = False
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
                stopPlay()

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
    pygame.mixer.music.stop()

def stopPlay():
    pygame.mixer.music.pause()

    pygame.mixer.music.unpause()


def stopmusic():

    pygame.mixer.music.stop()



def playloop():
    print 'starting'
    fps = 60




    while not musicExit:

        events = pygame.event.get()

        pygame.mixer.music.load('test2.wav')#load music

        pygame.mixer.music.play(-1)
        gameDisplay.fill(white)






        button("play", 200,200,100,50, green, light_green, action="play")
        button("back", 50,200,100,50, yellow, light_yellow, action="back")
        button("forward", 350,200,100,50, yellow, light_yellow, action="forward")

        button("quit", 400,350,100,50, red, light_red, action ="quit")
        gameDisplay.blit(backImg, (50,200))
        #gameDisplay.blit(playImg, (50,200))
        gameDisplay.blit(stopImg, (200,150))
        gameDisplay.blit(forImg, (350,200))
        clock.tick(fps)
        pygame.display.flip()
        if pygame.mixer.music.get_busy():

            for event in events:

                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.Q:
                        sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                     #print "mouse at (%d, %d)" % event.pos
                    pass


    pygame.quit()
    quit()


start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
playloop()
pygame.quit()