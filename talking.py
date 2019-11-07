# -*- coding: cp1252 -*-
import pygame, random, sys, time
import talking
from pygame.locals import*

sys.dont_write_bytecode = True

WINDOWWIDTH = 1200
WINDOWHEIGHT=600


#things i can change through convo
shieldmax=10
shields=shieldmax #10
hull=10 #10
roundtimer=3 #30
rapid_fire_constant=10 #10 
PLAYERMOVERATE=7 #7
ADDNEWBADDIERATE=15#lower is more guys spawning # 15
BULLETTHRESHOLD=80 #higher = slower #80

girlslevel=['Dismal', 'Improving', 'Hopeful', 'Complete']
girl1_level=girlslevel[0]
girl2_level=girlslevel[0]
girl3_level=girlslevel[0]

relationshippoints=1
#relationship points needs to go to 0

#dismal, improving, hopeful, beliving

TEXTCOLOR= (255,255,255)
BACKGROUNDCOLOR= (0,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
LIGHTBLUE=(0,255,222)
LGREEN=(145,255,145)
RED=(255,0,0)
PURP=(207,76,255)


pygame.init()
mainClock=pygame.time.Clock()
windowSurface=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
#48, 30, 20
font=pygame.font.SysFont("Arial", 40)
smallfont=pygame.font.SysFont("Arial", 20)
medfont=pygame.font.SysFont("Arial", 26)

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            if event.type==KEYDOWN:
                if event.type==K_ESCAPE:
                    terminate()
                return

def drawText (text, font, surface, x, y):
    textobj=font.render(text, 1, TEXTCOLOR)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj, textrect)

def drawTextmine (text, font, surface, x, y, inputcolortext):
    textobj=font.render(text, 1, inputcolortext)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj, textrect)

guy1rectleft=pygame.Rect(0, 0, 100, 150)
guy1rectright=pygame.Rect((WINDOWWIDTH-200), (WINDOWHEIGHT-200), 100, 150)
guy1imageint=pygame.image.load('guy1.png')
guy1image=pygame.transform.scale(guy1imageint, (200,200))

girl1rectleft=pygame.Rect(0, 0, 100, 150)
girl1rectright=pygame.Rect((WINDOWWIDTH-200), (WINDOWHEIGHT-200), 100, 150)
girl1imageint=pygame.image.load('girl1.png')
girl1image=pygame.transform.scale(girl1imageint, (200,200))

girl2rectleft=pygame.Rect(0, 0, 100, 150)
girl2rectright=pygame.Rect((WINDOWWIDTH-200), (WINDOWHEIGHT-200), 100, 150)
girl2imageint=pygame.image.load('girl2.png')
girl2image=pygame.transform.scale(girl2imageint, (200,200))

girl3rectleft=pygame.Rect(0, 0, 100, 150)
girl3rectright=pygame.Rect((WINDOWWIDTH-200), (WINDOWHEIGHT-200), 100, 150)
girl3imageint=pygame.image.load('girl3.png')
girl3image=pygame.transform.scale(girl3imageint, (200,200))

guy2rectleft=pygame.Rect(0, 0, 100, 150)
guy2imageint=pygame.image.load('guy2.png')
guy2image=pygame.transform.scale(guy2imageint, (200,200))

def talking1():

    texttopleft=210
    texttoptop=50
    texttopsecond=90
    textbotleft=300
    pygame.mixer.music.load('tesmu.wav')
    pygame.mixer.music.play(-1,0.0)

    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()

    
    #left and right appropriately
    guy1rectleft=pygame.Rect(0, 0, 100, 150)
    guy1rectright=pygame.Rect((WINDOWWIDTH-200), (WINDOWHEIGHT-200), 100, 150)
    guy1imageint=pygame.image.load('guy1.png')
    guy1image=pygame.transform.scale(guy1imageint, (200,200))

    girl1rectleft=pygame.Rect(0, 0, 100, 150)
    girl1rectright=pygame.Rect((WINDOWWIDTH-200), (WINDOWHEIGHT-200), 100, 150)
    girl1imageint=pygame.image.load('girl1.png')
    girl1image=pygame.transform.scale(girl1imageint, (200,200))

    girl2rectleft=pygame.Rect(0, 0, 100, 150)
    girl2rectright=pygame.Rect((WINDOWWIDTH-200), (WINDOWHEIGHT-200), 100, 150)
    girl2imageint=pygame.image.load('girl2.png')
    girl2image=pygame.transform.scale(girl2imageint, (200,200))

    girl3rectleft=pygame.Rect(0, 0, 100, 150)
    girl3rectright=pygame.Rect((WINDOWWIDTH-200), (WINDOWHEIGHT-200), 100, 150)
    girl3imageint=pygame.image.load('girl3.png')
    girl3image=pygame.transform.scale(girl3imageint, (200,200))

    storyboard1rect=pygame.Rect(0, 0, WINDOWWIDTH, (WINDOWHEIGHT-250))
    storyboard1int=pygame.image.load('storyship1.png')
    storyship1image=pygame.transform.scale(storyboard1int, ((WINDOWWIDTH-300),300))    
    windowSurface.blit(storyship1image, storyboard1rect)
    drawTextmine('-- The Solarian Federation Deep Space ', smallfont, windowSurface, (WINDOWWIDTH-300), 50, LIGHTBLUE)
    drawTextmine('Reconnaissance Ship \'Radiant\'', smallfont, windowSurface, (WINDOWWIDTH-300), 80, LIGHTBLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()

    drawTextmine('-- A small Solarian Fleet patrols the dangerous territory of the treacherous alien race called the \'Burn\'.', medfont, windowSurface, 10, 320, WHITE)
    drawTextmine('While not officially at war, tensions have been increasingly strained, in \'Border Actions\'', medfont, windowSurface, 10, 370, WHITE)
    drawTextmine('and \'Accidents\' alone there have been over 125,000 Solarians deaths, and many think it is  ', medfont, windowSurface, 10, 420, WHITE)
    drawTextmine('only a matter of time before the embers of war are sparked into an inferno...', medfont, windowSurface, 10, 470, WHITE)
    pygame.display.update()
    waitForPlayerToPressKey()




###




    ###

    #we'll never make it
    #well, we have to try dont we?
    #we are just a recon ship!? what can we do!?
    #weapon officer came up with the mega crush, but they only have a few

###    
    #
    windowSurface.fill(BACKGROUNDCOLOR)    
    pygame.display.update()
    drawTextmine('Care to repeat that?', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey() 
     
  

    #add 40 to height
    #drawTextmine('Care to repeat that?', font, windowSurface, 210, 50, BLUE)
    drawTextmine('Sir, the message I recieved was that', font, windowSurface, textbotleft, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('our fleet has come under Burn attack.', font, windowSurface, textbotleft, (WINDOWHEIGHT-60), LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()


    
    windowSurface.fill(BACKGROUNDCOLOR)

    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('What do you mean we are under attack?', font, windowSurface, 210, 50, BLUE)
    drawTextmine('Where is Flagship S1K?', font, windowSurface, 210, 90, BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()

    drawTextmine('Destroyed... we are the only ship left.', font, windowSurface, textbotleft, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)

    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('But...But, I had friends on those ships!', font, windowSurface, 210, 50, RED)
    drawTextmine('Jaiko was on S1K!!!  S1K just can\'t be gone!', font, windowSurface, 210, 90, RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()

###guy on bot
    drawTextmine('...', font, windowSurface, 500, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    #time.sleep(2)
    waitForPlayerToPressKey()
    drawTextmine('We will be in visual scanner range soon to confirm.', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)

    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()

###2nd scene
    storyboard2rect=pygame.Rect(0, 0, WINDOWWIDTH, (WINDOWHEIGHT-250))
    storyboard2int=pygame.image.load('story2.png')
    storyship2image=pygame.transform.scale(storyboard2int, ((WINDOWWIDTH),300))    
    windowSurface.blit(storyship2image, storyboard2rect)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('.', font, windowSurface, textbotleft, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine(' .', font, windowSurface, textbotleft, (WINDOWHEIGHT-100), BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('  .', font, windowSurface, textbotleft, (WINDOWHEIGHT-100), BLUE)
    pygame.display.update()
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('   Damn', font, windowSurface, textbotleft, (WINDOWHEIGHT-100), BLUE)

    pygame.display.update()
    waitForPlayerToPressKey()


###3rd and 3rd girl
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('JAIKO!!!', font, windowSurface, 500, (WINDOWHEIGHT-100), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)

    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('NO!!!', font, windowSurface, 500, (WINDOWHEIGHT-60), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Galil, please...', font, windowSurface, 210, 50, PURP)
    drawTextmine('Your screaming does not help, we are all confused right now.', font, windowSurface, 210, 90, PURP)    
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('They are all dead...If the Burn move this', font, windowSurface, 180, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('decisively everywhere, even Terra might fall.', font, windowSurface, 180, (WINDOWHEIGHT-60), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()


    drawTextmine('Not going to happen.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()

    #nxt scene
    #
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    drawTextmine('Why not?  They are taking advantage of the', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('fact that if they kill every ship, they can ', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    drawTextmine('attack faster than any message sent earlier.', font, windowSurface, 150, (WINDOWHEIGHT-60), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

##
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Grav-Jumps are way faster than any message.', font, windowSurface, 210, 50, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Even if we got a message out, they could beat it to Terra!', font, windowSurface, 210, 90, RED)
    pygame.display.update()
    waitForPlayerToPressKey()


    drawTextmine('We are not sending a message.', font, windowSurface, textbotleft, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('...We...aren\'t?', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('We are bringing the message.', font, windowSurface, textbotleft, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('It is the only way we could beat the Burn to Terra.', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('You are crazy!  We are five Gravline\'s away from Terra!!!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('All five are though Burn controlled locations!', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)    
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('We are one recon ship, barely even suited for battle.', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('We are one recon ship, barely even suited for battle.', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    drawTextmine('No offense Dax, but this was a joke assignment.', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('We all ended up here because we were not good', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    drawTextmine('enough for any other position.', font, windowSurface, 150, (WINDOWHEIGHT-60), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('...', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('It is hopeless!  We are we going to do!?', font, windowSurface, 140, (WINDOWHEIGHT-100), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)    
    pygame.display.update()
    drawTextmine('It is hopeless!  We are we going to do!?', font, windowSurface, 140, (WINDOWHEIGHT-100), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)    
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE) 
    drawTextmine('You are going to engage the Grav-Jump,', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Niko, is going to get on the weapons,', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('And Lavine, is going to funnel all remaining shields. ', font, windowSurface, 210, 130, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)    
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)  
    drawTextmine('And you!?!?', font, windowSurface, 540, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)    
    pygame.display.update()
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE) 
    drawTextmine('Me?  I\'m going to get us out of here alive.', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    pygame.mixer.music.stop()












#after 1
def talkingpost1():

    texttopleft=210
    texttoptop=50
    texttopsecond=90
    textbotleft=300
    pygame.mixer.music.load('storymusic1.wav')
    pygame.mixer.music.play(-1,0.0)

    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()
    drawTextmine('We did it! We did it!!!', font, windowSurface, 210, 50, RED)   
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('Heh, I have to say, I am impressed you ', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('got us out of there.', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('Heh, I have to say, I am impressed you ', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('got us out of there.', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    
    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('I had faith in you Sir.', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)

    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('I had faith in you Sir.', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    drawTextmine('Maybe you had faith in him, but we are the  ', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('only ship alive mainly because we were not there ', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    drawTextmine('during the surprise attack.', font, windowSurface, 150, (WINDOWHEIGHT-60), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    
    windowSurface.fill(BACKGROUNDCOLOR)

    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    drawTextmine('Maybe you had faith in him, but we are the  ', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('only ship alive mainly because we were not there ', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    drawTextmine('during the surprise attack.', font, windowSurface, 150, (WINDOWHEIGHT-60), PURP)
    

    drawTextmine('We were fortunate in that regard.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('We were fortunate in that regard.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)

    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    drawTextmine('What is not fortunate is how far we are', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('from Terra.', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)

    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    drawTextmine('What is not fortunate is how far we are', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('from Terra', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()

    drawTextmine('We are one Gravline closer!', font, windowSurface, 210, 50, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('We are one Gravline closer!', font, windowSurface, 210, 50, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)

    drawTextmine('One more closer to zero.', font, windowSurface, 500, (WINDOWHEIGHT-100), BLUE)   
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()

    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('One more closer to zero.', font, windowSurface, 500, (WINDOWHEIGHT-100), BLUE)   
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    
    drawTextmine('This is a peripheral colony, each Jump is going ', font, windowSurface, 210, 50, PURP)
    drawTextmine('to be far worse, as the fleets converge on Terra. ', font, windowSurface, 210, 90, PURP)    
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('This is a peripheral colony, each Jump is going ', font, windowSurface, 210, 50, PURP)
    drawTextmine('to be far worse, as the fleets converge on Terra. ', font, windowSurface, 210, 90, PURP)    
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)

    drawTextmine('I can not believe the Burn are attacking.', font, windowSurface, textbotleft, (WINDOWHEIGHT-100), LGREEN)   
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('I can not believe the Burn are attacking.', font, windowSurface, textbotleft, (WINDOWHEIGHT-100), LGREEN)   
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('We knew it was only a matter of time.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('We knew it was only a matter of time.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)

    drawTextmine('Good, I just need to get on a better ship ', font, windowSurface, 250, (WINDOWHEIGHT-140), PURP)
    drawTextmine('so I can kill them all. ', font, windowSurface, 250, (WINDOWHEIGHT-100), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Good, I just need to get on a better ship ', font, windowSurface, 250, (WINDOWHEIGHT-140), PURP)
    drawTextmine('so I can kill them all. ', font, windowSurface, 250, (WINDOWHEIGHT-100), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    drawTextmine('Jaiko...I can\'t believe he is gone...', font, windowSurface, 210, 50, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Jaiko...I can’t believe he is gone...', font, windowSurface, 210, 50, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    drawTextmine('Do you feel bad we were not there, Galil?', font, windowSurface, textbotleft, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Do you feel bad we were not there, Galil?', font, windowSurface, textbotleft, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('If we were there we might have been able…', font, windowSurface, 210, 50, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('If we were there we might have been able…', font, windowSurface, 210, 50, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    drawTextmine('If we were there, we would be dead!', font, windowSurface, 400, (WINDOWHEIGHT-100), BLUE)    
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('If we were there, we would be dead!', font, windowSurface, 400, (WINDOWHEIGHT-100), BLUE)    
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    drawTextmine('...', font, windowSurface, 210, 50, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('...', font, windowSurface, 500, (WINDOWHEIGHT-100), BLUE)    
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    drawTextmine('...', font, windowSurface, 210, 50, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('We were lucky we were on the other side of the planet.', font, windowSurface, 100, (WINDOWHEIGHT-60), BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('...', font, windowSurface, 500, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('We were lucky we were on the other side of the planet.', font, windowSurface, 100, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    drawTextmine('I don\'t care if I am alive or dead, ', font, windowSurface, 210, 50, PURP)
    drawTextmine('I won\'t know the difference.', font, windowSurface, 210, 90, PURP)    
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Ha, few of them probably knew the moment ', font, windowSurface, 210, 50, PURP)
    drawTextmine('they died anyway!', font, windowSurface, 210, 90, PURP)    
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('Stop.', font, windowSurface, 700, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)

    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('Why!?  Does it bother you I am talking about death? ', font, windowSurface, 210, 50, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Galil\'s friend...', font, windowSurface, 700, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()

    
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('... ', font, windowSurface, 210, 50, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)    
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('(I can\'t believe he is gone...)', font, windowSurface, 210, 90, RED)

    pygame.display.update()
    waitForPlayerToPressKey()

    
    windowSurface.fill(BACKGROUNDCOLOR)

    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('Sweet little Lavine, always looking out for everyone', font, windowSurface, 210, 50, PURP)
    drawTextmine('else.  How trite.  Grow up!  Both of you!!!', font, windowSurface, 210, 90, PURP)    
    pygame.display.update()
    waitForPlayerToPressKey()
    
    drawTextmine('Do you want me to be mean?  I can. I know', font, windowSurface, 250, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('all about you, and why you ended up here.', font, windowSurface, 250, (WINDOWHEIGHT-60), LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)

    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    drawTextmine('Ohh, smart little Lavine.  You think you are so skilled,', font, windowSurface, 210, 50, PURP)
    drawTextmine('but you are on the same ship as I am!', font, windowSurface, 210, 90, PURP)    
    pygame.display.update()
    waitForPlayerToPressKey()
    
    drawTextmine('Stop it.  Both of you. It is clear some', font, windowSurface, 250, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('of you are not happy on this ship,', font, windowSurface, 250, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('I don\'t care.', font, windowSurface, 500, (WINDOWHEIGHT-100), BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectright)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    drawTextmine('You all have a job to do, and I expect it done.', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)

    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)    
    windowSurface.blit(guy1image, guy1rectright)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    drawTextmine('We are taking the shortest path back to Terra, but ', font, windowSurface, 50, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('it is likely the Burn are on the exact same gravlocks.', font, windowSurface, 50, (WINDOWHEIGHT-60), BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    drawTextmine('(He is so stupid.  Why are we even risking this?  To think', font, windowSurface, 210, 50, PURP)
    drawTextmine('I got stuck with a commander like him...)', font, windowSurface, 210, 90, PURP)    
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('(He was good getting us out of that attack, but to escape ', font, windowSurface, 210, 50, RED)
    drawTextmine('through armies of Burn? Can we really do it?)', font, windowSurface, 210, 90, RED)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('(Dax…I understand your motivation, ', font, windowSurface, textbotleft, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('but we don\'t stand a chance...)', font, windowSurface, textbotleft, (WINDOWHEIGHT-60), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('It is likely when we come out of Jump', font, windowSurface, 210, 50, BLUE)
    drawTextmine('the area might already be overran.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('I need each of you to squeeze anything you ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('can out of this ship.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Because I can tell this is going to be', font, windowSurface, 210, 50, BLUE)
    drawTextmine('one hell of a ride.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    pygame.mixer.music.stop()






#post level 2
def talkingpost2():


    
    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()
    pygame.mixer.music.load('postlevel2.wav')
    pygame.mixer.music.play(-1,0.0)
    
    drawTextmine('I can’t believe they had grav disruptors ', font, windowSurface, 210, 50, RED)
    drawTextmine('in place already!', font, windowSurface, 210, 90, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('If there is any doubt of the intent of this ', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('attack I think it was just dispelled.', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()

    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('How did we not see this coming?', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('You must be blind, everyone saw it coming.', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()

    drawTextmine('I don\'t think anyone saw the intensity.', font, windowSurface, 210, 50, BLUE)
    drawTextmine('This is an all-out attack.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('They are risking everything on this.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()



    drawTextmine('Isn\'t the Solarian fleet stronger than ', font, windowSurface, 200, (WINDOWHEIGHT-100), RED)
    drawTextmine('the Burn\'s though?', font, windowSurface, 200, (WINDOWHEIGHT-60), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)

    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Way stronger, we would never lose to Burn swine.', font, windowSurface, 210, 50, PURP)
    drawTextmine('I don\'t know why Dax is on this suicide mission.', font, windowSurface, 210, 90, PURP)    
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    drawTextmine('The Aelisha will step in if things get bad.', font, windowSurface, 200, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('They have always protected us.', font, windowSurface, 200, (WINDOWHEIGHT-60), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Both are missing the point.  You guys are not ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('considering fleet losses to this surprise attack.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Even after that though, our fleet will still be stronger.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('So…didn’t you just prove my point?', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)


    drawTextmine('I am not done.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine(' "..."     (Idiot...)', font, windowSurface, 350, (WINDOWHEIGHT-140), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('The real problem is twofold, they are clearly ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('blitzing for Terra.  ', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()
    drawTextmine('If we lose our home planet not only is a major source  ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('of our our fleet and power gone, but with it', font, windowSurface, 210, 90, BLUE)
    drawTextmine('morale and logistical strategy.', font, windowSurface, 210, 130, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('Terra won\'t fall!!', font, windowSurface, 210, 50, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Terra can\'t fall!!!', font, windowSurface, 210, 90, RED)

    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('It could.', font, windowSurface, 350, (WINDOWHEIGHT-140), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('But our scattered fleets would still be stronger.', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('With the new Dragoon-Class ships, the Burn stand no', font, windowSurface, 130, (WINDOWHEIGHT-140), PURP)
    drawTextmine('chance.  Our fleets are not locailzed anyway.', font, windowSurface, 130, (WINDOWHEIGHT-100), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('I heard the Blue Dragoon was recently hijacked and.', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('stolen.  Not confirmed officially, of course.', font, windowSurface, 210, 90, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Regardless, I know about the Dragoons, and Terra.', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    drawTextmine('The Burn are not getting in.  Thus we should abandon', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    drawTextmine('this crazy idea.', font, windowSurface, 100, (WINDOWHEIGHT-60), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('You are cowardly Niko.  ', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Listen to yourself. "Weapon" officer.', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)

    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    drawTextmine('Even if I believe our race could somehow prevail without', font, windowSurface, 210, 50, BLUE)
    drawTextmine('our home, and in a disorganized mess we would be left', font, windowSurface, 210, 90, BLUE)
    drawTextmine('in, I will not risk it just to save myself.', font, windowSurface, 210, 130, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Are you calling me a coward?', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    drawTextmine('That is exactly what I am calling you.', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Shouldn’t a captain know how his actions will affect', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('his crew?  What if I decide I won’t fire in battle?', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    
    windowSurface.fill(BACKGROUNDCOLOR)


    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    drawTextmine('As a captain, I know exactly how my crew will behave.  ', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)


    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    drawTextmine('So you can put this front on, but I know as soon as we ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('Dis-Jump, and the choice is between fire or die, ', font, windowSurface, 210, 90, BLUE)
    drawTextmine('what you will choose.', font, windowSurface, 210, 130, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()


    drawTextmine('Dax, we can’t possible make it through this alive.', font, windowSurface, 200, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('At least tell me you realize that.', font, windowSurface, 200, (WINDOWHEIGHT-60), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)

    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('(You do realize, but tell me this is just a front.)', font, windowSurface, 200, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('(Like he would admit it.  He will drag me to my grave)', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('(Is Dax going to let us die?)', font, windowSurface, 200, (WINDOWHEIGHT-100), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)



    drawTextmine('Dax...', font, windowSurface, 210, 50, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('Is that true…?  I don’t want to die, ', font, windowSurface, 210, 50, RED)
    drawTextmine('this was my first assingment…', font, windowSurface, 210, 90, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()



    
    drawTextmine('Of course it is.  He will not admit it.', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('Just think of all those that died in our ', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    drawTextmine('fleet when they first attacked.', font, windowSurface, 150, (WINDOWHEIGHT-60), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('We have made it through two, if we can do that, ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('whats stopping us from only three more?', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Great, a plan that relies on luck and hope.', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('And skill.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    pygame.display.update()
    waitForPlayerToPressKey()

    pygame.mixer.music.stop()





#post level 3
def talkingpost3():


    
    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()
    pygame.mixer.music.load('postlevel3.wav')
    pygame.mixer.music.play(-1,0.0)

    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('We made it...somehow.', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)

    
    pygame.display.update()
    waitForPlayerToPressKey()


    drawTextmine('We can\'t keep going, we are going to die!!!', font, windowSurface, 200, (WINDOWHEIGHT-100), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('In case you haven’t figured it out our ship is not getting ', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('repaired, and it is only going to get worse', font, windowSurface, 210, 90, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)


    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('I don’t even know if our warning would help, they ', font, windowSurface, 210, 50, RED)
    drawTextmine('they have so many ships converging already.  ', font, windowSurface, 210, 90, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)

    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('We might be too late as it is.', font, windowSurface, 210, 50, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    
    drawTextmine('That is true, I did not consider we might be at ', font, windowSurface, 200, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('the end of a series of attacks.', font, windowSurface, 200, (WINDOWHEIGHT-60), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)

    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('I say we abandon this.  ', font, windowSurface, 210, 50, PURP)
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Jump to somewhere safe and ride this out.', font, windowSurface, 210, 50, PURP)
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('That would be in defiance of my order.', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)    
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)

    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Well maybe that is what I am saying!  ', font, windowSurface, 210, 50, PURP)
    drawTextmine('We don’t even know if it would matter!', font, windowSurface, 210, 90, PURP)    
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('...', font, windowSurface, 200, (WINDOWHEIGHT-100), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('...', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)

    
    drawTextmine('Heh, so that’s how it is.  ', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)

    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('Cowards at heart.  We get a lease on ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('life and you all want to go running.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Dax we are on a suicide mission.  Rationally,  ', font, windowSurface, 200, (WINDOWHEIGHT-120), LGREEN)
    drawTextmine('there is no way to ensure there is a', font, windowSurface, 200, (WINDOWHEIGHT-80), LGREEN)
    drawTextmine('Terra left.', font, windowSurface, 200, (WINDOWHEIGHT-40), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('I believe in you, but we are trying to get ', font, windowSurface, 210, 50, RED)
    drawTextmine('through their fleets, the odds we ', font, windowSurface, 210, 90, RED)
    drawTextmine('make it are zero!', font, windowSurface, 210, 130, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)

    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('You know what else is a zero?', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)


    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('This captain.', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('I really don’t care if you like me.  ', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)

    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('We are doing this because we are loyal ', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('to the Solarian race.', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)

    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('If any of you fail to follow my orders ', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('I will personally execute you.', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)

    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)


    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('...', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)

    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('...', font, windowSurface, 200, (WINDOWHEIGHT-60), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)

    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('...', font, windowSurface, 210, 90, PURP)    
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)

    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('It is unfortunate it has come to this, that my crew', font, windowSurface, 100, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('is so seditious, but I am not changing my mind.', font, windowSurface, 100, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)

    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('I am sworn to protecting our race, and Terra ', font, windowSurface, 100, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('specifically at any cost.  ', font, windowSurface, 100, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)


    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('If I have to risk my life on a chance to save Terra from ', font, windowSurface, 100, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('a surprise attack I will do it every time.', font, windowSurface, 100, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)


    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine(' I would rather die then run.  ', font, windowSurface, 400, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Run knowing I had knowledge that might ', font, windowSurface, 100, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('have been able to save our race.', font, windowSurface, 100, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)


    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)


    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('(Dax…I am sorry I am not as brave as you.)', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)

    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('(How many would do what he is doing?  ', font, windowSurface, 200, (WINDOWHEIGHT-100), RED)
    drawTextmine('I admire the nobility, but I am terrified.)', font, windowSurface, 200, (WINDOWHEIGHT-60), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('(Ugh…this bastard.)', font, windowSurface, 210, 90, PURP)    
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('Dax?', font, windowSurface, 210, 90, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('What?', font, windowSurface, 550, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()

    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('I don\'t want to die.', font, windowSurface, 210, 90, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('...', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('Galil I am not going to let you die.  ', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('I will try my hardest to keep everyone here alive.', font, windowSurface, 210, 50, BLUE)
    drawTextmine('Whether you believe that or not.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Our chance of survival is low, but is it not zero.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('There is only one thing that is going to ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('be ‘zero’ around here.', font, windowSurface, 210, 90, BLUE)    
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('That is how many GravLines we are going to have ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('left to run when this is over.', font, windowSurface, 210, 90, BLUE)    
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()     
    

    pygame.mixer.music.stop()
    





#post 4
def talkingpost4():


    
    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()
    pygame.mixer.music.load('postlevel4.wav')
    pygame.mixer.music.play(-1,0.0)

    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('Heh, one more and that’s game.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey() 


    drawTextmine('We are going to make it!  ', font, windowSurface, 200, (WINDOWHEIGHT-100), RED)
    drawTextmine('We really might!', font, windowSurface, 200, (WINDOWHEIGHT-60), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()
    waitForPlayerToPressKey() 
    windowSurface.fill(BACKGROUNDCOLOR)

    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('The defenses we are running into are becoming insane.', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('As much as I hate to admit it, I actually ', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('think there is a chance we will ', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    drawTextmine('make it.', font, windowSurface, 150, (WINDOWHEIGHT-60), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)


    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('There is no telling what we are going to face on ', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('this final Jump.  We are going to have to pull ', font, windowSurface, 210, 90, LGREEN)
    drawTextmine('out all the stops.', font, windowSurface, 210, 130, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('But ALL I think we have is a chance.  That is it. ', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I still think this was and is a stupid idea.', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('But ALL I think we have is a chance.  That is it. ', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('I still think this was and is a stupid idea.', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    
    drawTextmine('Noted.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('Why do you think they attacked us?', font, windowSurface, 200, (WINDOWHEIGHT-100), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    windowSurface.fill(BACKGROUNDCOLOR)

    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('Despite our simmering hostilities, there is ', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('little reason for an all out war.', font, windowSurface, 210, 90, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('Notably we do not even colonize the same ', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('type of planets.', font, windowSurface, 210, 90, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('They are either after something, or running ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('from something.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Running?', font, windowSurface, 450, (WINDOWHEIGHT-100), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('I can\'t guess what the reason would be, ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('but those are the only things I can think.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('Do they hate us that bad Dax?', font, windowSurface, 200, (WINDOWHEIGHT-100), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('Well, they clearly dislike us.  However doing', font, windowSurface, 210, 50, BLUE)
    drawTextmine('anything in the name of hate is irrationale.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('But this is not about like or dislike.  They are not going ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('to risk parts of their fleets on emotion.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    drawTextmine('Burn are not know to possess emotion.', font, windowSurface, 200, (WINDOWHEIGHT-60), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('Would the Burn want us gone? Certainly, but ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('not at the risk they are incurring.  ', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Even if they start to decimate our race, the ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('Aelisha will step in and annihilate the Burn.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('So why?', font, windowSurface, 200, (WINDOWHEIGHT-60), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('And why are we on this mission than?', font, windowSurface, 210, 90, PURP)    
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I am not sure what they are after, but it   ', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('is very desperate.', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Niko, this is not about the Burn losing', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('it is about our home surviving.', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)

    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('We are doing this so we have a planet to return', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('to... to a home that still exists.', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)    
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('Terra...I hope it is still there.', font, windowSurface, 200, (WINDOWHEIGHT-100), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('What a waste this would all be.', font, windowSurface, 210, 90, PURP)    
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('We better get ready before our final Jump.', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    drawTextmine('You can do it Dax, I know you can.', font, windowSurface, 200, (WINDOWHEIGHT-100), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)    
    drawTextmine('“WE” can do this.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()


    
    pygame.mixer.music.stop()









def talkingpost5():


    
    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()
    pygame.mixer.music.load('morelevelmusic5.wav')
    pygame.mixer.music.play(-1,0.0)    




    storyboard1rect=pygame.Rect(0, 0, WINDOWWIDTH, (WINDOWHEIGHT-250))
    storyboard1int=pygame.image.load('endstory1.png')
    storyship1image=pygame.transform.scale(storyboard1int, ((WINDOWWIDTH),300))    
    windowSurface.blit(storyship1image, storyboard1rect)
    drawTextmine('-- Terra - Home of the Solarian Race', smallfont, windowSurface, 20, 310, LIGHTBLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()


    drawTextmine('Its Terra!  I see it!!', font, windowSurface, 200, (WINDOWHEIGHT-100), RED)
    drawTextmine('But...its so quiet...', font, windowSurface, 200, (WINDOWHEIGHT-60), RED)    
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    
    storyboard1rect=pygame.Rect(0, 0, WINDOWWIDTH, (WINDOWHEIGHT-250))
    storyboard1int=pygame.image.load('endstory1.png')
    storyship1image=pygame.transform.scale(storyboard1int, ((WINDOWWIDTH),300))    
    windowSurface.blit(storyship1image, storyboard1rect)
    drawTextmine('-- Terra - Home of the Solarian Race', smallfont, windowSurface, 20, 310, LIGHTBLUE)

    drawTextmine('Is Terra is still alive?', font, windowSurface, 200, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    storyboard1rect=pygame.Rect(0, 0, WINDOWWIDTH, (WINDOWHEIGHT-250))
    storyboard1int=pygame.image.load('endstory1.png')
    storyship1image=pygame.transform.scale(storyboard1int, ((WINDOWWIDTH),300))    
    windowSurface.blit(storyship1image, storyboard1rect)
    drawTextmine('-- Terra - Home of the Solarian Race', smallfont, windowSurface, 20, 310, LIGHTBLUE)
    
    drawTextmine('Damn, we made it.  I can\'t believe it', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('But where is everyone?', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)    
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    storyboard1rect=pygame.Rect(0, 0, WINDOWWIDTH, (WINDOWHEIGHT-250))
    storyboard1int=pygame.image.load('endstory1.png')
    storyship1image=pygame.transform.scale(storyboard1int, ((WINDOWWIDTH),300))    
    windowSurface.blit(storyship1image, storyboard1rect)
    drawTextmine('-- Terra - Home of the Solarian Race', smallfont, windowSurface, 20, 310, LIGHTBLUE)


    drawTextmine('Lavine, get on the comm now, transmit the ', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('following message on all known bands.', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    storyboard1rect=pygame.Rect(0, 0, WINDOWWIDTH, (WINDOWHEIGHT-250))
    storyboard1int=pygame.image.load('endstory1.png')
    storyship1image=pygame.transform.scale(storyboard1int, ((WINDOWWIDTH),300))    
    windowSurface.blit(storyship1image, storyboard1rect)
    drawTextmine('-- Terra - Home of the Solarian Race', smallfont, windowSurface, 20, 310, LIGHTBLUE)

    drawTextmine('Copy that Dax, all connections open.', font, windowSurface, 200, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('"Prepare to copy emergency traffic.” ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('Lavine, do you have all the data of our battles?', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)

    pygame.display.update()    
    waitForPlayerToPressKey()
    
    drawTextmine('Yes, it is loaded.', font, windowSurface, 200, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('Okay, start sending it.  ', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)

    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('“We are under Burn attack.  My name is Dax, Commander ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('of the Deep Space Reconnaissance Ship the Radiant"', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('"Repeat we are under Burn attack.”', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)

    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('It is shipping.', font, windowSurface, 200, (WINDOWHEIGHT-60), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)

    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Will they believe us?', font, windowSurface, 210, 50, RED)
    drawTextmine('Is anyone even left!?', font, windowSurface, 210, 90, RED)    
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()    
    waitForPlayerToPressKey()

    drawTextmine('They better, after everything we went through.  ', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('I will strangle someone if they don\'t.', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('I will not stop you.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('Damn it!  Why won\'t they respond?', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()    

    windowSurface.fill(BACKGROUNDCOLOR)  
    drawTextmine('“We are the lone survivor of an attack on our ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('fleet, we are barely ahead of the Burn attack."  ', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)

    pygame.display.update()    
    waitForPlayerToPressKey()    

    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('“You must prepare all ships and defenses ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('immediately.  This is not a drill.”  ', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)

    pygame.display.update()    
    waitForPlayerToPressKey() 
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Damn it!  Are they not listening?', font, windowSurface, 210, 50, BLUE)
    drawTextmine('Are we too late!?  After everything', font, windowSurface, 210, 90, BLUE)
    drawTextmine('we went through...', font, windowSurface, 210, 130, BLUE)        
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey() 
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('“Sky Commander Laya!  Sky Commander Laya!”', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey() 
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('“Sky Commander Laya has been…replaced”', font, windowSurface, 210, 50, WHITE)
    windowSurface.blit(guy2image, guy2rectleft)
    pygame.display.update()    
    waitForPlayerToPressKey()

    drawTextmine('“Replaced!? Where the hell is the Sky Commander!?"', font, windowSurface, 100, (WINDOWHEIGHT-130), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()    
    waitForPlayerToPressKey()    
    drawTextmine('“Get me Laya immediately!"', font, windowSurface, 100, (WINDOWHEIGHT-90), BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('“Our very survival is at stake!"', font, windowSurface, 100, (WINDOWHEIGHT-50), BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()    
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('“Where she has gone is none of your concern."', font, windowSurface, 210, 50, WHITE)
    windowSurface.blit(guy2image, guy2rectleft)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('What is going on?  Did Terra get taken over?', font, windowSurface, 200, (WINDOWHEIGHT-120), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()
    waitForPlayerToPressKey()    
    drawTextmine('Dax...are we too late?', font, windowSurface, 200, (WINDOWHEIGHT-90), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Are the Burn actually just other Solarians!?', font, windowSurface, 200, (WINDOWHEIGHT-60), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    drawTextmine('No way...we were fighting other Solarians?', font, windowSurface, 210, 60, PURP)    
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('We were fighting our own people!?', font, windowSurface, 210, 90, PURP)        
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('No, this is not right.  The Burn are not', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('anywhere near Solarian.  I am not sure who this is.', font, windowSurface, 210, 90, LGREEN)    
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)   
    windowSurface.blit(girl1image, girl1rectleft)
    pygame.display.update()    
    waitForPlayerToPressKey()

    drawTextmine('You mentioned that the Blue Dragoon was ', font, windowSurface, 200, (WINDOWHEIGHT-120), RED)
    drawTextmine('stolen, any chance it is that?', font, windowSurface, 200, (WINDOWHEIGHT-90), RED)    
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()
    waitForPlayerToPressKey()    
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('Maybe.  It might be because of the Blue Dragoon missing, ', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('can not think of anything else.', font, windowSurface, 210, 90, LGREEN)    
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)   
    windowSurface.blit(girl1image, girl1rectleft)
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    drawTextmine('Would she be removed for losing a Dragoon?', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()    
    waitForPlayerToPressKey()    
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('It is possible, depending on who this guy is.', font, windowSurface, 210, 50, LGREEN)
  
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)   
    windowSurface.blit(girl1image, girl1rectleft)
    pygame.display.update()    
    waitForPlayerToPressKey()

    drawTextmine('“Who the hell are you?”', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)

    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('“It is vital I talk to someone important."', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)    
    drawTextmine('“I am Sky Commander Dailance.”', font, windowSurface, 210, 50, WHITE)
    windowSurface.blit(guy2image, guy2rectleft)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('Dailance - Sky Commander of Terra', smallfont, windowSurface, 10, 210, WHITE)

    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('Lavine, can you confirm that?', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('I am checking the incoming data now...', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)   
    windowSurface.blit(girl1image, girl1rectleft)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectleft)    
    drawTextmine('Oh my god...it really is the Sky Commander!', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()


    drawTextmine('Damn, he is kinda cute...', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    
    drawTextmine('“Sir, are you receiving the data we are sending?”', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('“Confirmed.  Captain, you did hell of a job ', font, windowSurface, 210, 50, WHITE)
    drawTextmine('bringing us this information."  ', font, windowSurface, 210, 90, WHITE)
    windowSurface.blit(guy2image, guy2rectleft)
    drawTextmine('Dailance - Sky Commander of Terra', smallfont, windowSurface, 10, 210, WHITE)   
    
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('"We are activating all defenses as we speak."', font, windowSurface, 210, 50, WHITE)
    windowSurface.blit(guy2image, guy2rectleft)
    drawTextmine('Dailance - Sky Commander of Terra', smallfont, windowSurface, 10, 210, WHITE) 
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    drawTextmine('We did it!  We helped save Terra!', font, windowSurface, 200, (WINDOWHEIGHT-60), RED)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('Well, the attack still has not come yet.', font, windowSurface, 210, 90, PURP)    
    windowSurface.blit(girl3image, girl3rectleft)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 10, 210, PURP)
    pygame.display.update()    
    waitForPlayerToPressKey()

    drawTextmine('They are mobilizing, Terra will be able to ', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('hold with this warning.', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('"You have done well.  I am clearing an ', font, windowSurface, 210, 50, WHITE)
    drawTextmine('opening on Dock 127 for you.', font, windowSurface, 210, 90, WHITE)
    windowSurface.blit(guy2image, guy2rectleft)
    drawTextmine('Dailance - Sky Commander of Terra', smallfont, windowSurface, 10, 210, WHITE)    
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('Let us get that ship repaired.', font, windowSurface, 210, 130, WHITE)    
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('It looks like its been through war."', font, windowSurface, 210, 160, WHITE)    
    pygame.display.update()    
    waitForPlayerToPressKey()    
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('"Can I interest you in a quick break and then commanding', font, windowSurface, 210, 60, WHITE)
    drawTextmine('a lended ship for this battle?', font, windowSurface, 210, 90, WHITE)
    drawTextmine('I do not think your ship will be repaired fast enough."', font, windowSurface, 210, 120, WHITE)    
    windowSurface.blit(guy2image, guy2rectleft)
    drawTextmine('Dailance - Sky Commander of Terra', smallfont, windowSurface, 10, 210, WHITE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    drawTextmine('“No rest, and this ship is just fine Sir.”', font, windowSurface, 150, (WINDOWHEIGHT-100), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('"I will see you in the battle then.', font, windowSurface, 210, 50, WHITE)
    drawTextmine('Captain, I wish we had a thousand more like you."', font, windowSurface, 210, 90, WHITE)    
    windowSurface.blit(guy2image, guy2rectleft)
    drawTextmine('Dailance - Sky Commander of Terra', smallfont, windowSurface, 10, 210, WHITE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)

    drawTextmine('No complaints from you guys if we help?', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()  
    drawTextmine('None.  Lets give these Burn the ', font, windowSurface, 200, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('pounding they deserve.', font, windowSurface, 200, (WINDOWHEIGHT-60), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('We are done running!', font, windowSurface, 210, 90, RED)
    windowSurface.blit(girl2image, girl2rectleft)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 10, 210, RED)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('Good, I was not done killing them yet.', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()    
    waitForPlayerToPressKey()    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Then lets go, to protect Terra!', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()    
    waitForPlayerToPressKey()  
    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('Dax…are you going to report us when this is over?', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()  
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    drawTextmine('For what?', font, windowSurface, 150, (WINDOWHEIGHT-60), BLUE)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 950, 380, BLUE)
    windowSurface.blit(guy1image, guy1rectright)
    pygame.display.update()    
    waitForPlayerToPressKey()  
    drawTextmine('For going against you.', font, windowSurface, 210, 50, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Hmm...', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('Can\'t say I remember anything like that happening.  ', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectleft)
    drawTextmine('...Thanks', font, windowSurface, 210, 50, LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 10, 210, LGREEN)
    drawTextmine('Thanks.', font, windowSurface, 150, (WINDOWHEIGHT-60), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    pygame.display.update()    
    waitForPlayerToPressKey()   
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('We are done running.  Let’s show them what we can do.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()

    drawTextmine('For Flagship S1X and Jaiko!', font, windowSurface, 200, (WINDOWHEIGHT-60), RED)    
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Radiant Engine Control', smallfont, windowSurface, 950, 380, RED)

    pygame.display.update()    
    waitForPlayerToPressKey()    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('We are done running.  Let’s show them what we can do.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)    

    drawTextmine('For all those I didn\'t get to kill, and our ', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    drawTextmine('comrades who fell during the surprise attacks.', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Radiant\'s Weapon Officer', smallfont, windowSurface, 950, 380, PURP)
    
    pygame.display.update()    
    waitForPlayerToPressKey()    
    windowSurface.fill(BACKGROUNDCOLOR)
    
    drawTextmine('We are done running.  Let’s show them what we can do.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)    

    drawTextmine('For Terra, our home.', font, windowSurface, 200, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('Lavine - Radiant Communications', smallfont, windowSurface, 950, 380, LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()    
    waitForPlayerToPressKey()    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('For the Radiant.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Commander of the Radiant', smallfont, windowSurface, 10, 210, BLUE)      
    pygame.display.update()    
    waitForPlayerToPressKey()    
    windowSurface.fill(BACKGROUNDCOLOR)
    storyboard2rect=pygame.Rect(0, 0, WINDOWWIDTH, (WINDOWHEIGHT-250))
    storyboard2int=pygame.image.load('endstory2.png')
    storyship2image=pygame.transform.scale(storyboard2int, ((WINDOWWIDTH),300))    
    windowSurface.blit(storyship2image, storyboard2rect)
    drawTextmine('On that date, a Burn fleet appeared in the Terra system to the surprise of many, ', medfont, windowSurface, 20, 310, LIGHTBLUE)
    drawTextmine('but not to all.  Few people knew of Dax and his crew, the sacrifice they went ', medfont, windowSurface, 20, 340, LIGHTBLUE)
    drawTextmine('through to get critical information back to their home.  ', medfont, windowSurface, 20, 370, LIGHTBLUE) 
    pygame.display.update()    
    waitForPlayerToPressKey()   
    windowSurface.fill(BACKGROUNDCOLOR)
    
    storyboard2rect=pygame.Rect(0, 0, WINDOWWIDTH, (WINDOWHEIGHT-250))
    storyboard2int=pygame.image.load('endstory2.png')
    storyship2image=pygame.transform.scale(storyboard2int, ((WINDOWWIDTH),300))    
    windowSurface.blit(storyship2image, storyboard2rect)
    drawTextmine('But among the highest echelons that knew, many attribute the ', medfont, windowSurface, 20, 310, LIGHTBLUE)
    drawTextmine('the rout of the Burn directly to this heroic warning ', medfont, windowSurface, 20, 340, LIGHTBLUE)
    drawTextmine('one small ship named the Radiant carried across the stars.', medfont, windowSurface, 20, 370, LIGHTBLUE) 

    pygame.display.update()    
    waitForPlayerToPressKey()   
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('        The End.', font, windowSurface, 500, 300, WHITE)
    drawTextmine('Thank you for playing!', font, windowSurface, 500, 350, WHITE)    
    drawTextmine('Gravline: Zero - By Eric Szabelski', medfont, windowSurface, 400, 400, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()

    
    pygame.mixer.music.stop()




def talklavine1():


    
    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()
    
    drawTextmine('Lavine.', font, windowSurface, 210, 90, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    pygame.display.update()    
    waitForPlayerToPressKey()

    drawTextmine('Hello sir.  We only have a little time,', font, windowSurface, 300, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('why are you here?', font, windowSurface, 300, (WINDOWHEIGHT-60), LGREEN)
    windowSurface.blit(girl1image, girl1rectright)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('I came to help.', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()                
    drawTextmine('Sir, you don\'t need to.', font, windowSurface, 300, (WINDOWHEIGHT-100), LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('You do not need to be so formal with me, Lavine.', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()                
    drawTextmine('Sorry Si...Ok', font, windowSurface, 300, (WINDOWHEIGHT-100), LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('Here let me help you with that.', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Ok...', font, windowSurface, 300, (WINDOWHEIGHT-100), LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('Seeing the way you and Niko always fight', font, windowSurface, 210, 50, BLUE)
    drawTextmine('are you not happy on this ship?', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('...', font, windowSurface, 300, (WINDOWHEIGHT-100), LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('Do you think I am a bad leader?', font, windowSurface, 210, 50, BLUE) 
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('No.  ', font, windowSurface, 300, 480, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Nothing to do with you.  ', font, windowSurface, 300, 520, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Only my own fault.', font, windowSurface, 300, 560, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('...', font, windowSurface, 210, 30, BLUE) 
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('(Galil is young, and I am a Captain, but both Lavine ', font, windowSurface, 210, 70, BLUE)
    drawTextmine('and Niko both screwed up to end up on this ship)', font, windowSurface, 210, 110, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('It might be out of place but I wanted to say', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('something since I saw you on my crew.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Whats that?', font, windowSurface, 700, 520, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    
    drawTextmine('You probably don’t remember, but we went ', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('to the same academy.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)

    drawTextmine('I always felt really bad about this one prank, ', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('once I tell you, you’ll remember.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('The sauce?', font, windowSurface, 600, 520, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('Ha, so you remember.', font, windowSurface, 210, 30, BLUE) 
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('How could I forget?', font, windowSurface, 600, 520, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('Sorry about that.', font, windowSurface, 210, 30, BLUE) 
    pygame.display.update()
    waitForPlayerToPressKey()
    
    drawTextmine('Haha!  Don’t be, I was only splashed, ', font, windowSurface, 300, 520, LGREEN)
    drawTextmine('my friend got it worse.', font, windowSurface, 300, 560, LGREEN)    
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('I was trying so hard to not ', font, windowSurface, 500, 520, LGREEN)
    drawTextmine('laugh back then!', font, windowSurface, 500, 560, LGREEN)    
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Ha, glad you aren’t mad.', font, windowSurface, 210, 30, BLUE) 
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    
    drawTextmine('I am not, actually I am glad ', font, windowSurface, 500, 520, LGREEN)
    drawTextmine('you remembered me.', font, windowSurface, 500, 560, LGREEN) 
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I always felt bad about that.', font, windowSurface, 210, 30, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
        
    drawTextmine('As funny as it was.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    
    drawTextmine('Don\'t feel bad.  It was funny.', font, windowSurface, 400, 520, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('If I could see that other girl I would ', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('apologize to her.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('You can\'t', font, windowSurface, 600, 520, LGREEN)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Why?', font, windowSurface, 210, 30, BLUE) 
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)

    drawTextmine('She died in a ‘border action’ with the Burn ', font, windowSurface, 300, 520, LGREEN)
    drawTextmine('pretty soon after graduation.', font, windowSurface, 300, 560, LGREEN) 
    pygame.display.update()
    waitForPlayerToPressKey()
    
    drawTextmine('...', font, windowSurface, 210, 30, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()    
    drawTextmine('It is almost time to come out of Jump.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)                
    windowSurface.blit(girl1image, girl1rectright)
    
    drawTextmine('Thanks for the help and the talk.', font, windowSurface, 300, 560, LGREEN) 
    pygame.display.update()
    waitForPlayerToPressKey()

    drawTextmine('I’ll make sure it is not our last.', font, windowSurface, 210, 30, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()    

    
#


def talklavine2():


    
    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()
    
    drawTextmine('Hey Lavine, if we route some power from the comms ', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('through the shield converter it should increase ', font, windowSurface, 210, 70, BLUE)
    drawTextmine('the power output…', font, windowSurface, 210, 110, BLUE)     

    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)    
    pygame.display.update()    
    waitForPlayerToPressKey()

    drawTextmine('You seem pretty smart Sir.', font, windowSurface, 300, (WINDOWHEIGHT-100), LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)        
    drawTextmine('They do not make dumb Captains.  ', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('Again, just call me Dax.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('I guess I was just basing it off of myself and', font, windowSurface, 250, 480, LGREEN)
    drawTextmine('Niko, ending up on a ship on the fringe.', font, windowSurface, 250, 520, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)     
    drawTextmine('(Is she going to go into why they ', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('both were assigned here?)', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
 
    drawTextmine('I feel kind of bad for Galil, ending up ', font, windowSurface, 300, 480, LGREEN)
    drawTextmine('on a ship with a bunch of screw-ups.', font, windowSurface, 300, 520, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)
    
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)     
    drawTextmine('I think you are mistaken about ', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('why I am here.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()

    drawTextmine('What do you mean?', font, windowSurface, 300, 480, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('I can’t guess what happened to you or in ', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('Niko’s past, but there are no ', font, windowSurface, 210, 70, BLUE)
    drawTextmine('‘screw-up’ captains.', font, windowSurface, 210, 110, BLUE)     
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('If you do not cut it, you are gone.', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('Period.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('But sir, no offense, but ', font, windowSurface, 300, 480, LGREEN)
    drawTextmine('this assignment…', font, windowSurface, 300, 520, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('Was a bad one?  Of course.  ', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('But that is how it works, this is my ', font, windowSurface, 210, 70, BLUE)
    drawTextmine('first assignment, just like Galil’s.', font, windowSurface, 210, 110, BLUE)     
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('This is not a ‘bad’ assignment because ', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('I messed up.  This is a totally ', font, windowSurface, 210, 70, BLUE)
    drawTextmine('typical one.', font, windowSurface, 210, 110, BLUE)     
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('I had no idea...', font, windowSurface, 300, 480, LGREEN)

    windowSurface.fill(BACKGROUNDCOLOR)
    
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)    
    drawTextmine('Anyway, if we live through this, I will ensure that ', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('whatever you did is forgotten and you will ', font, windowSurface, 210, 70, BLUE)
    drawTextmine('get to a ‘better’ ship ', font, windowSurface, 210, 110, BLUE)     
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)    
    drawTextmine('Since it is what you want.', font, windowSurface, 210, 30, BLUE) 
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    drawTextmine('Si…Dax.  Thank you.  I only hope', font, windowSurface, 250, 480, LGREEN)
    drawTextmine('that we would be on the same ship.', font, windowSurface, 250, 520, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    
    drawTextmine('Well I could try to see if I could get you again.', font, windowSurface, 210, 30, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('I would like that.', font, windowSurface, 300, 480, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()    
    drawTextmine('We have to live first.', font, windowSurface, 210, 30, BLUE)     
    pygame.display.update()    
    waitForPlayerToPressKey()




def talklavine3():


    
    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('Dax, I am so sorry for what I have done.', font, windowSurface, 300, 480, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('(She used my name)', font, windowSurface, 210, 30, BLUE)   

    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('What are you apologizing for?  Anything you have said ', font, windowSurface, 210, 30, BLUE) 
    drawTextmine('recently I attribute to combat stress, and you have ', font, windowSurface, 210, 70, BLUE)
    drawTextmine('done nothing except a stellar job.', font, windowSurface, 210, 110, BLUE)     

    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)

    drawTextmine('I lied to you.', font, windowSurface, 300, 480, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('About?', font, windowSurface, 210, 30, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)

    drawTextmine('Why I am on this ship.', font, windowSurface, 300, 480, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('You messed up, I get it, don’t worry.', font, windowSurface, 210, 30, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)

    drawTextmine('But I got people killed.  ', font, windowSurface, 300, 480, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('Accidental?', font, windowSurface, 210, 30, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('...', font, windowSurface, 300, 480, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('No.  But that is what I said it was.', font, windowSurface, 300, 520, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    drawTextmine('(Damn…)', font, windowSurface, 210, 30, BLUE)    

    pygame.display.update()    
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('You know the girl you spilled the sauce on?  ', font, windowSurface, 200, 480, LGREEN)

    pygame.display.update()    
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('We always had a rivalry, and it started to turn to ', font, windowSurface, 100, 480, LGREEN)
    drawTextmine('hate.  We were on a assignment together,', font, windowSurface, 100, 520, LGREEN)
    drawTextmine('and her ship was in trouble…', font, windowSurface, 100, 560, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()    
    drawTextmine('(She is crying…  She always seems so ', font, windowSurface, 210, 30, BLUE)    
    drawTextmine('measured and controlled.)', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('I rerouted her communication, it left her ', font, windowSurface, 200, 480, LGREEN)
    drawTextmine('and her crew dead.', font, windowSurface, 200, 520, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)    
    drawTextmine('I was found out later, but covered it enough', font, windowSurface, 100, 480, LGREEN)
    drawTextmine('that it looked like an accident. Then I was ', font, windowSurface, 100, 520, LGREEN)
    drawTextmine('assigned to the fringe as a chance to redeem myself.', font, windowSurface, 100, 560, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey() 
    drawTextmine('Well you are doing a good job of that.', font, windowSurface, 210, 30, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)       
    drawTextmine('You don’t care?', font, windowSurface, 300, 480, LGREEN)

    pygame.display.update()    
    waitForPlayerToPressKey()    
    drawTextmine('Not really.  Captains always get crews composed of people ', font, windowSurface, 210, 30, BLUE)
    drawTextmine('like this.  The Federation is pretty big, a lot of people ', font, windowSurface, 210, 70, BLUE)
    drawTextmine('go astray.  This is a chance at forgiveness.', font, windowSurface, 210, 110, BLUE)     
    pygame.display.update()    
    waitForPlayerToPressKey() 
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    
    drawTextmine('You don’t care that I am so messed up?', font, windowSurface, 300, 480, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    drawTextmine('They prepared us for this. Captains’ first assignments are ', font, windowSurface, 210, 30, BLUE)  
    drawTextmine('always composed of people the Federation has viewed ', font, windowSurface, 210, 70, BLUE)
    drawTextmine('as useful enough for a second chance.', font, windowSurface, 210, 110, BLUE)     
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    
    drawTextmine('I feel like I was let off easy, no ', font, windowSurface, 300, 480, LGREEN)
    drawTextmine('record or anything.', font, windowSurface, 300, 520, LGREEN)
    
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('You remember in the one place that matters.', font, windowSurface, 210, 30, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('There is something else I wanted to say…', font, windowSurface, 100, 480, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('What is that?  You do not need to curb ', font, windowSurface, 210, 30, BLUE)
    drawTextmine('your words around me', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)    

    drawTextmine('The main thing I wanted to say…I really care about you.  ', font, windowSurface, 100, 480, LGREEN)
    drawTextmine('Ever since I saw you in the academy.  Then to get ', font, windowSurface, 100, 520, LGREEN)
    drawTextmine('assigned to your ship after messing up so badly…', font, windowSurface, 100, 560, LGREEN)

    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('Lavine, I care about you too.  You messed up. I get it.', font, windowSurface, 210, 30, BLUE)
    drawTextmine('A lot of people do.  Let it go, prove to the Federation ', font, windowSurface, 210, 70, BLUE)
    drawTextmine('you deserved this second chance.', font, windowSurface, 210, 110, BLUE)     
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright)    
    drawTextmine('Thank you Dax...', font, windowSurface, 300, 480, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('I can tell you have a gentle heart, ', font, windowSurface, 210, 30, BLUE)   
    drawTextmine('and that is what matters to me.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl1image, girl1rectright) 
    drawTextmine('I would never leave you Dax.  I will do anything for you.', font, windowSurface, 100, 480, LGREEN)
    drawTextmine('I want to stay with you forever. ', font, windowSurface, 100, 520, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('Well, lets get out of this first.', font, windowSurface, 210, 30, BLUE)   
    pygame.display.update()    
    waitForPlayerToPressKey()    



##




#









def talklavineend():


    pygame.mixer.music.load('endgamemusic.wav')
    pygame.mixer.music.play(-1,0.0)
    
    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()
    windowSurface.blit(girl1image, girl1rectright)
    drawTextmine('The Green Dragoon...what an amazing ship.', font, windowSurface, 200, (WINDOWHEIGHT-100), LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()
    windowSurface.blit(girl1image, girl1rectright)    
    drawTextmine('To think I am the Comm Officer on a ship ', font, windowSurface, 200, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('of this caliber… How things have changed.', font, windowSurface, 200, (WINDOWHEIGHT-60), LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('Lavine - Green Dragoon\'s Communication Officer', medfont, windowSurface, 700, 380, LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()    
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('We warned Terra, we helped in its', font, windowSurface, 210, 30, BLUE)   
    drawTextmine('defense, this is only natural.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectright)    
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('Lavine - Green Dragoon\'s Communication Officer', medfont, windowSurface, 700, 380, LGREEN)
    
    drawTextmine('And to think I get to serve', font, windowSurface, 200, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('with a hero~', font, windowSurface, 200, (WINDOWHEIGHT-60), LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    drawTextmine('Everyone on the Radiant helped.', font, windowSurface, 210, 30, BLUE)   
    pygame.display.update()    
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectright)    
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('Lavine - Green Dragoon\'s Communication Officer', medfont, windowSurface, 700, 380, LGREEN)

    drawTextmine('And that I get to spend my nights', font, windowSurface, 200, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('with that hero…', font, windowSurface, 200, (WINDOWHEIGHT-60), LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()

    drawTextmine('You are a sweet, attractive girl who does her job,', font, windowSurface, 210, 30, BLUE)   
    drawTextmine('that’s better than a lot.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectright)    
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('Lavine - Green Dragoon\'s Communication Officer', medfont, windowSurface, 700, 380, LGREEN)

    drawTextmine('Hehe, such a way with words.', font, windowSurface, 200, (WINDOWHEIGHT-60), LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('Actions speak louder than words.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()
 
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectright)    
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('Lavine - Green Dragoon\'s Communication Officer', medfont, windowSurface, 700, 380, LGREEN)
    drawTextmine('Oh believe me.  After last night', font, windowSurface, 200, (WINDOWHEIGHT-80), LGREEN)
    drawTextmine('I have no doubt of that.', font, windowSurface, 200, (WINDOWHEIGHT-40), LGREEN)    
    pygame.display.update()    
    waitForPlayerToPressKey()
    drawTextmine('Anyway, I am glad we made it through all that.', font, windowSurface, 210, 30, BLUE)   
    drawTextmine('Now I have a cute girl, and a great ship.', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()

    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectright)    
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('Lavine - Green Dragoon\'s Communication Officer', medfont, windowSurface, 700, 380, LGREEN)

    drawTextmine('Of course, now that we have a real ship is it time', font, windowSurface, 100, (WINDOWHEIGHT-100), LGREEN)
    drawTextmine('show the Burn what we can really do.', font, windowSurface, 100, (WINDOWHEIGHT-60), LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()    
    drawTextmine('Before we leave, I need you to report to my quarters', font, windowSurface, 210, 30, BLUE)   
    drawTextmine('Green Dragoon Communication Officer Lavine', font, windowSurface, 210, 70, BLUE)
    pygame.display.update()    
    waitForPlayerToPressKey()  
    pygame.mixer.music.stop()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl1image, girl1rectright)    
    windowSurface.blit(guy1image, guy1rectleft)
    drawTextmine('Yes sir~', font, windowSurface, 100, (WINDOWHEIGHT-60), LGREEN)
    pygame.display.update()    
    waitForPlayerToPressKey()    





    
##

def talkgalil1():


    
    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()

    drawTextmine('Galil?', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('             Galil?', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    drawTextmine('Dax, I’m down here.', font, windowSurface, 200, (WINDOWHEIGHT-100), RED)
    windowSurface.blit(girl2image, girl2rectright)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('I came to help out with the engines.', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I am trying a new way of charging the grav engines,', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('They might wear out faster, but should make us faster.', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('What will it improve? Jump charge time, or our speed?', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Both!!!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('Great, tell me what to do and I’ll help.', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Ok, first hold this while I go change…', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('“While I go change”', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Hehe, slip of the tongue!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('Galil are you upset to be on this ship ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('like the other two?', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('No way!  I understand why they both are,', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('but I don’t know their story.', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)    
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)     
    drawTextmine('This is my first assignment out of the academy', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('so I did not have high expectations.', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)    
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('… (She is young, so this is a pretty standard assignment', font, windowSurface, 210, 50, BLUE)
    drawTextmine('for her, unlike the other two, she did not screw up)', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)     
    drawTextmine('Sorry!  Didn\'t mean anything by that.', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('In all honesty I am impressed with you.', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)      
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)     
    drawTextmine('If I get to a bigger ship I can’t wait to', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('see the officers there!', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)      
    pygame.display.update()
    waitForPlayerToPressKey()    
    drawTextmine('(Does she even realize what she is implying?', font, windowSurface, 210, 50, BLUE)
    drawTextmine('Maybe just naïve.)', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('I am going to command a bigger ship one day.', font, windowSurface, 210, 50, BLUE)   
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I believe in you!  But I then again, don’t know much!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)    
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('(Man, I don’t think she realizes half of what she says.)', font, windowSurface, 210, 50, BLUE)   
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Well that should about do it!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)    
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('Finished changing?', font, windowSurface, 210, 50, BLUE)   
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Now I am going to go change for real!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)    
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('I am not coming.', font, windowSurface, 210, 50, BLUE)   
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Aww...', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)    
    pygame.display.update()
    waitForPlayerToPressKey()    
    

def talkgalil2():
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('Galil?', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Hey you knew where to look for me!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)   
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('I am a fast learner.', font, windowSurface, 210, 50, BLUE)   
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Yeah I am impressed with how much', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('you helped with the engines.', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)    
    pygame.display.update()
    waitForPlayerToPressKey()    
  
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('I know Niko and Lavine do not have that much', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('faith in you, but I do. ', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)    
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('I think you are great, I can’t believe I got ', font, windowSurface, 100, (WINDOWHEIGHT-130), RED)
    drawTextmine('assigned to a ship like this for my first!', font, windowSurface, 100, (WINDOWHEIGHT-90), RED)
    drawTextmine('I can\'t tell you are bad at all!', font, windowSurface, 100, (WINDOWHEIGHT-50), RED)      
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('(Ha, at least her honesty is refreshing.)', font, windowSurface, 210, 50, BLUE)   
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)     
    drawTextmine('Galil, this is my first official ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('assingment, like you.', font, windowSurface, 210, 90, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Like me!?  Your first!?  No way!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('You are always so cool, and calm...', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)    
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('You did not screw up like the others?!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)    
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)     
    drawTextmine('No.  Captains always get these, to see if', font, windowSurface, 210, 50, BLUE)
    drawTextmine('they can prove themselves with reformed crews ', font, windowSurface, 210, 90, BLUE)
    drawTextmine('before better posistions.', font, windowSurface, 210, 130, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Wow!  That is so cool! I hope after this ', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('is all over I can get onto a better ship.  ', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)
    pygame.display.update()
    waitForPlayerToPressKey()    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)   
    drawTextmine('They have some really great new grav engines', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('coming out…in the Dragoon class they use…', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)
    pygame.display.update()
    waitForPlayerToPressKey()      
    drawTextmine('(She is the youngest, but she definitely', font, windowSurface, 210, 50, BLUE)
    drawTextmine('knows her stuff when it comes to this.)', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)   
    drawTextmine('Anyway, if we make it through this,', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('can I be on your ship again?', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Captains are allowed to pick some of the crew,', font, windowSurface, 210, 50, BLUE)
    drawTextmine('if you would I would be glad to have you.', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)   
    drawTextmine('Yay!  I just got one thing to take care of ', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('again real fast before our next battle.', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)   
    drawTextmine('Let me guess, going to go change again?', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Yeah!  Want to come help?', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)   
    drawTextmine(' No, not right now.  Maybe if we get through this.', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I will hold you to it!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()



def talkgalil3():
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('We are at about the limits of how fast', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('this Grav Engine can charge.', font, windowSurface, 100, (WINDOWHEIGHT-60), RED) 
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('The fact you were able to improve it', font, windowSurface, 210, 50, BLUE)
    drawTextmine('at all is impressive.', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('No way, you helped way more than I thought', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('Captains ever could!', font, windowSurface, 100, (WINDOWHEIGHT-60), RED) 
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('You can’t wait until you get to a big ship', font, windowSurface, 210, 50, BLUE)
    drawTextmine('to see about those Captains right?', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('No!  I found the Captain I want to stick', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('with for my whole life.', font, windowSurface, 100, (WINDOWHEIGHT-60), RED) 
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Why?  You are young, this is', font, windowSurface, 210, 50, BLUE)
    drawTextmine('your first assignment.', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('This was yours as well!  You are awesome', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('Dax, brave, smart, good looking.', font, windowSurface, 100, (WINDOWHEIGHT-60), RED) 
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('Besides, I like you.', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()    
    drawTextmine('I like you too Galil, if we make it through this alive', font, windowSurface, 210, 50, BLUE)
    drawTextmine('it would be an honor to have you on my crew.', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()       

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('But I mean I really like you!  ', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('I was so lucky to have my first assignment', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('be with someone as great as you.', font, windowSurface, 100, (WINDOWHEIGHT-60), RED) 
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Good, I don’t get the messed up girl.', font, windowSurface, 210, 50, BLUE)   
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('Like Niko and Lavine?', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Yes.', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()    

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('No way, I am perfect.', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)

    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Do you know how to cook, how to be nice, how to', font, windowSurface, 210, 50, BLUE)
    drawTextmine('fix or clean clothes without the machines?', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('Uh…', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I have high standards for girls.  You have to be cute,', font, windowSurface, 210, 50, BLUE)
    drawTextmine('nice, know something more than just engines…', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()
 
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('I will learn!  ', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()    
    drawTextmine('I will learn all of them!!!', font, windowSurface, 100, (WINDOWHEIGHT-60), RED) 
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Ha, lets get out of this alive Galil.', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)    
    drawTextmine('I will do everything I can to make sure we survive!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()  


#





def talkgalilend():
    pygame.mixer.music.load('endgamemusic.wav')
    pygame.mixer.music.play(-1,0.0)    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)
    
    drawTextmine('I can\'t believe I am on a Dragoon!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('These new engines are awesome!!!', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Galil - Green Dragoon Engine Control', medfont, windowSurface, 820, 380, RED)    
    pygame.display.update()
    waitForPlayerToPressKey()
    
    drawTextmine('After what we went through?', font, windowSurface, 210, 50, BLUE)
    drawTextmine('We deserved something like this.', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Green Dragoon Engine Control', medfont, windowSurface, 820, 380, RED)    
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('To think I served with the legendary Dax!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Served? You were instrumental.', font, windowSurface, 210, 50, BLUE)
    drawTextmine('By the way, I like these clothes.', font, windowSurface, 210, 90, BLUE)      
    pygame.display.update()
    waitForPlayerToPressKey()

    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Green Dragoon Engine Control', medfont, windowSurface, 820, 380, RED)    
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('No problem!  It was easy to pick up.', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('Glad you like them!!!', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Remember when you were trying to lure me in', font, windowSurface, 210, 50, BLUE)
    drawTextmine('during the whole event with your ‘changing clothes’?', font, windowSurface, 210, 90, BLUE)      
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Green Dragoon Engine Control', medfont, windowSurface, 820, 380, RED)    
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('Hehe, yeah, seems kind of stupid now.', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I thought it was cute.', font, windowSurface, 210, 50, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Green Dragoon Engine Control', medfont, windowSurface, 820, 380, RED)    
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('Anyway, we got some time before we head', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('off to against the Burn.', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)    
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('And?', font, windowSurface, 210, 50, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Green Dragoon Engine Control', medfont, windowSurface, 820, 380, RED)    
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('Well I was thinking you could help change my', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
    drawTextmine('clothes, and I could help change yours.', font, windowSurface, 100, (WINDOWHEIGHT-60), RED)    
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Is this going to end the same way last night did?', font, windowSurface, 210, 50, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()     

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl2image, girl2rectright)
    drawTextmine('Galil - Green Dragoon Engine Control', medfont, windowSurface, 820, 380, RED)    
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('And better!!!', font, windowSurface, 100, (WINDOWHEIGHT-100), RED)
 
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Lets go.  Then the Burn are going to pay.', font, windowSurface, 210, 50, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()
    

##












    ###

def talkniko1():


    
    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()



    drawTextmine('Niko I came here to see if I can’t help you out', font, windowSurface, 210, 50, BLUE)
    drawTextmine('with our weapons.', font, windowSurface, 210, 90, BLUE)    
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)    
    pygame.display.update()
    waitForPlayerToPressKey()      
    drawTextmine('This meager load out consisting of just some lasers?', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Those would be the ones.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)    
    pygame.display.update()
    waitForPlayerToPressKey()      
    drawTextmine('Whatever.  ', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Anyway I think if I reroute some of the power I can ', font, windowSurface, 150, (WINDOWHEIGHT-100), PURP)
    drawTextmine('charge them faster.', font, windowSurface, 150, (WINDOWHEIGHT-60), PURP)    
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawTextmine('Do it, our firepower is about the only thing keeping us alive.', font, windowSurface, 210, 50, BLUE)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)    
    pygame.display.update()
    waitForPlayerToPressKey()      
    drawTextmine('I want you to know how pathetic this is.', font, windowSurface, 150, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('I am a highly skilled weapons officer, capable ', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    drawTextmine('of handling multiple platforms, bringing to ', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    drawTextmine('bear thousands of rounds…', font, windowSurface, 100, (WINDOWHEIGHT-60), PURP)    
    pygame.display.update()
    waitForPlayerToPressKey()    
    drawTextmine('So sorry you are stuck with me…', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('You better be.  ', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    drawTextmine('I deserve way better than this.', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()    
    drawTextmine('It was sarcasm.', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('Oh...', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('Well you think you are so cool then don’t you!  ', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    drawTextmine('You think you are so good, look at yourself Dax.', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('Commander on one little ship on a suicide mission. ', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()  
    drawTextmine('You are delusional.  ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('You do know how captains are trained and progress, right?', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('Or in all your childish loathing of everyone ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('did you forget that?', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('(I don’t know how, but I can’t let him know that)  ', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()    
    drawTextmine(' I know exactly how they are promoted!', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()      
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('Good, maybe you will keep that in mind next time.', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl3image, girl3rectright)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Hey, don’t go!  ', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()    
    drawTextmine(' Thanks for the help...  ', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(girl3image, girl3rectright)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('He is gone… I wonder if he heard me.  ', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()    
    drawTextmine('I truly meant it.', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)

    pygame.display.update()
    waitForPlayerToPressKey()  
#











#niko!

#

def talkniko2():


    
    windowSurface.fill(BACKGROUNDCOLOR)
    pygame.display.update()

    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)    
    drawTextmine('Dax…back to ‘help’ again?', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()   
    drawTextmine('Do you deny I helped last time?', font, windowSurface, 210, 50, BLUE)
    drawTextmine('with our weapons', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()



    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)    
    drawTextmine('As much as I would like to deny it, I will not.', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Do you hate me?', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)     
    drawTextmine('… Not exactly.', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Well that is a start.', font, windowSurface, 210, 50, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)     
    drawTextmine('I just…this was never supposed to happen to me.', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('(Her voice is close to cracking, I have ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('never seen her like this)', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()
    

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('I…damn it, I was among the best weapon ', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    drawTextmine('officers in my class.', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('I was trained to kill mercilessly, and I', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    drawTextmine('have done my job well even on a ship like this…', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('I lost track of how many I have helped kill', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    drawTextmine('from a distance, but I kill a single person', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    drawTextmine('in real life and my life is ruined…', font, windowSurface, 100, (WINDOWHEIGHT-60), PURP)    
    pygame.display.update()
    waitForPlayerToPressKey()    
    drawTextmine('(I suspected it might have been something', font, windowSurface, 210, 50, BLUE)
    drawTextmine('like that, given her hostility.)', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('(That is how the Solarian Federation works, someone can', font, windowSurface, 210, 50, BLUE)
    drawTextmine('mess up bad, and they are given a ‘second chance’)', font, windowSurface, 210, 90, BLUE)  
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('(But it is assignments to fringe', font, windowSurface, 210, 50, BLUE)
    drawTextmine('colonies or fleets.)', font, windowSurface, 210, 90, BLUE)  
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Does it bother you knowing I am a murderer?', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    drawTextmine('That you are commanding such a messed up crew?', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('Not at all.', font, windowSurface, 210, 50, BLUE)  
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Why?  How can it not?', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('You don\'t know how Captains are trained.  ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('Despite what you said.', font, windowSurface, 210, 90, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I don’t', font, windowSurface, 500, (WINDOWHEIGHT-140), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()


    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('We are given these ‘bad’ assignments as our first', font, windowSurface, 210, 50, BLUE)
    drawTextmine('ones, to prove what we can do, and', font, windowSurface, 210, 90, BLUE)
    drawTextmine('how we can handle people like you.', font, windowSurface, 210, 130, BLUE)       
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I hate to say it, but you are doing a good job.  ', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    drawTextmine('You are actually starting to grow on me.', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)    
    pygame.display.update()
    waitForPlayerToPressKey()
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright) 
    drawTextmine('You are growing on me a little as well.', font, windowSurface, 210, 50, BLUE)      
    pygame.display.update()
    waitForPlayerToPressKey()
    

def talkniko3():


    
    windowSurface.fill(BACKGROUNDCOLOR)


    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)    
    drawTextmine('This is about the limit we are going', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    drawTextmine('to get out of the lasers.', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)    
    pygame.display.update()
    waitForPlayerToPressKey()   
    drawTextmine('It has already done better than I expected.', font, windowSurface, 210, 50, BLUE)   
    pygame.display.update()
    waitForPlayerToPressKey()



    windowSurface.fill(BACKGROUNDCOLOR)


    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)    
    drawTextmine('I notice you have low expectations.', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)   
    pygame.display.update()
    waitForPlayerToPressKey()   
    drawTextmine('No, I actually have high expectations when I', font, windowSurface, 210, 50, BLUE)
    drawTextmine('think something can reach them.', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()    

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)    
    drawTextmine('...', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)   
    pygame.display.update()
    waitForPlayerToPressKey()  
    drawTextmine('What are your expectations of me?', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()     
    drawTextmine('High.', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()    

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)    
    drawTextmine('Still considering what you know of me?', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)   
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('No, before.  I could tell you were a girl I would like, despite', font, windowSurface, 210, 50, BLUE)
    drawTextmine('the illusion you put on for yourself and others.', font, windowSurface, 210, 90, BLUE) 
    pygame.display.update()
    waitForPlayerToPressKey()    

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)    
    drawTextmine('How can you tell?', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)   
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I am good at reading people.  ', font, windowSurface, 210, 50, BLUE)
    drawTextmine('Part of being a captain I suspose.', font, windowSurface, 210, 90, BLUE)    
    pygame.display.update()
    waitForPlayerToPressKey()      

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Besides, Weapon Officers are always aggressive, so no', font, windowSurface, 210, 50, BLUE)    
    drawTextmine('surprise there, considering the way you were made.', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()  
       
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('But you had this harsh exterior you crafted for yourself', font, windowSurface, 210, 50, BLUE)     
    drawTextmine('and it was a vulnerable girl that was within.', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()  
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)    
    drawTextmine('There is no use denying it.', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP) 
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I like the true Niko.  I like tough girls,', font, windowSurface, 210, 50, BLUE)       
    drawTextmine('but it needs to be measured.', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()  

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('There has to be a nice girl somewhere in there.', font, windowSurface, 210, 50, BLUE)      
    drawTextmine('Otherwise it is no different than a guy.', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()  

    drawTextmine('Hehe, all my life I always had to act so tough', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)   
    drawTextmine('it was the only way to protect myself.', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('I am glad to see there is actually a girl in', font, windowSurface, 210, 50, BLUE)       
    drawTextmine('that hot body.  But don’t go soft on me.', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()      
    drawTextmine('When this is all over, I am', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)   
    drawTextmine('going to beat you down…', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('…And then make some food and take care of you.', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)   

    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Good, I want to see that.  But the former will never happen.', font, windowSurface, 210, 90, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey() 





def talknikoend():
    pygame.mixer.music.load('endgamemusic.wav')
    pygame.mixer.music.play(-1,0.0)    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    
    drawTextmine('Now this is firepower I am talking about!', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)   
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Niko - Green Dragoon Weapon Officer', medfont, windowSurface, 820, 380, PURP)    
    pygame.display.update()
    waitForPlayerToPressKey()
    
    drawTextmine('Don’t get to carried away.  Yet.', font, windowSurface, 210, 50, BLUE)  
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Green Dragoon Weapon Officer', medfont, windowSurface, 820, 380, PURP)
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('Wow, fancy new clothes to go with the new command.', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)   
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('My risk paid off.', font, windowSurface, 210, 50, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Green Dragoon Weapon Officer', medfont, windowSurface, 820, 380, PURP)
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('I really have to hand it to you.  I was sorry', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)
    drawTextmine('for being such a bitch near the end there.', font, windowSurface, 100, (WINDOWHEIGHT-100), PURP)       
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Don’t worry.  It will stay between us.', font, windowSurface, 210, 50, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()    


    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Green Dragoon Weapon Officer', medfont, windowSurface, 820, 380, PURP)
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('You know what else I want between us?', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)      
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('What?', font, windowSurface, 210, 50, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Green Dragoon Weapon Officer', medfont, windowSurface, 820, 380, PURP)
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('Nothing.  Not even clothes.', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)      
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Ready again?  Last night wasn’t enough?', font, windowSurface, 210, 50, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()     



    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Green Dragoon Weapon Officer', medfont, windowSurface, 820, 380, PURP)
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('You brought out the bad girl in me.', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)      
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I thought I brought the nice girl out.', font, windowSurface, 210, 50, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()

    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Green Dragoon Weapon Officer', medfont, windowSurface, 820, 380, PURP)
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('You brought both!', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)      
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('I think I can spare you some time before we leave.', font, windowSurface, 210, 50, BLUE)     
    pygame.display.update()
    waitForPlayerToPressKey()

    
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(guy1image, guy1rectleft)
    windowSurface.blit(girl3image, girl3rectright)
    drawTextmine('Niko - Green Dragoon Weapon Officer', medfont, windowSurface, 820, 380, PURP)
    drawTextmine('Dax - Green Dragoon Commander', medfont, windowSurface, 10, 210, BLUE)
    drawTextmine('How nice of you.', font, windowSurface, 100, (WINDOWHEIGHT-140), PURP)      
    pygame.display.update()
    waitForPlayerToPressKey()
    drawTextmine('Lets go.  I want to see what your hands can do to me, before', font, windowSurface, 210, 50, BLUE)
    drawTextmine('I see the fleets of Burn annihilated by them.', font, windowSurface, 210, 90, BLUE)       
    pygame.display.update()
    waitForPlayerToPressKey() 


