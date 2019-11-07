import pygame, random, sys, time
import talking #other python file with majority of story elements

from pygame.locals import*

#This is the main file for Gravline: Zero.  Many of these variables
#can be changed to modify game experience, leave for intended difficulty
#Some old comments might remain from initial programming.  

WINDOWWIDTH = 1200
WINDOWHEIGHT=600

#Variables  changed through convo
shieldmax=15
shields=shieldmax #15
hullmax=10 #(xcv if change, change below for stats)
hull=hullmax #10
introundtimer=33
roundtimer=introundtimer #30
rapid_fire_constant=10 #10 
PLAYERMOVERATE=7 #7 #if changes, change the menu screen
ADDNEWBADDIERATE=10#lower is more guys spawning # 15 10
BULLETTHRESHOLD=70 #higher = slower #80

beatlevel=0 #1 for yes, 0 for no 
megacrush=7
playerRect=pygame.Rect(0,0,30,10) #30

roundreduction=0

girlslevel=['Dismal', 'Improving', 'Hopeful', 'Complete']
girl1_level=girlslevel[0]
girl2_level=girlslevel[0]
girl3_level=girlslevel[0]

relationshippoints=0

roundstarthull=hull 

TEXTCOLOR= (255,255,255)
BACKGROUNDCOLOR= (0,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
LIGHTBLUE=(0,255,222)
LGREEN=(5,255,145)
RED=(255,0,0)
PURP=(207,76,255)
GREEN=(50,255,25)
AQUA=(68,255,152)

FPS= 40
BADDIEMINSIZE = 20
BADDIEMAXSIZE=50
BADDIEMINSPEED=0
BADDIEMAXSPEED=2


dis_count=9999 #this number only used for initial level trigger
turret_count=9999
boss_count=9999

ADDNEWSTARRATE=6
STARMINSIZE=2
STARMAXSIZE=10
STARMINSPEED=2
STARMAXSPEED=8

ADDNEWASTEROIDRATE=60
ASTEROIDMINSIZE=40
ASTEROIDMAXSIZE=140


bossbullet_add_rate=10#xcv
eb_add_rate=20
eb_size=10
eb_speed=5

ADDNEWBULLETRATE=40

BULLETMINSIZE=2
BULLETMAXSIZE=15
BULLETMINSPEED=2
BULLETMAXSPEED=8



pygame.init()
mainClock=pygame.time.Clock()
windowSurface=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('GravLine: Zero')
pygame.mouse.set_visible(False)




def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            if event.type==KEYDOWN:
                if event.type==K_ESCAPE:
                    terminate()
                return


def playerHasHitBaddie (playRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def playerHasHitAsteroid (playRect, asteroids):
    for b in asteroids:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def playerHITbullet (playRect, bullets):
    for b in bullets:
        if playerRect.colliderect(b['rect']):
            return True
    return False


#defines when a shot hits a badguy, trying to remove him
def shothit (shots, baddies):
    for s in shots:
        for b in baddies:
            if s['rect'].colliderect(b['rect']):
                try:
                    baddies.remove(b)
                #remove this for a none removing 'super shot'
                    shots.remove(s)
                   
                except:pass
    return False

def shothitasteroid (shots, asteroids):
    for s in shots:
        for b in asteroids:
            if s['rect'].colliderect(b['rect']):
                try:
                #remove this for a none removing 'super shot'
                    shots.remove(s)
                   
                except:pass
    return False



didsomethingexplode=0
xxlocation=0
xxcounter=0
def shothit_hp (shots, enemywithhp):
    global xxcounter
    global didsomethingexplode

    global xxlocation
    for s in shots[:]:


       
        for e in enemywithhp[:]:
            #maybe add a blow up loop in here
            
            localhp=e['hp']

            if s['rect'].colliderect(e['rect']):
                localhp=localhp-1
                e['hp']=localhp
                try:
                    
                    shots.remove(s)
                except:pass
                if e['hp']<=0:                 
                    xxcounter=1
                    xxlocation=e['rect']
                    randfield=random.randint(0,3)
                    currentsound=expsounds[randfield]
                    currentsound.play()                 
                     
                    #try:
                    enemywithhp.remove(e)                     
                    #shots.remove(s)
                    didsomethingexplode=1

    return False



def expanime():
    global xxcounter
    global didsomethingexplode

    global xxlocation    
    if didsomethingexplode==1:

        yxxx=xxlocation.top
        xxxx=xxlocation.left
        expimagexxx=exp_image_list[xxcounter]
        windowSurface.blit(expimagexxx,( (xxxx-50),(yxxx-50)))
        pygame.display.update()
        xxcounter=xxcounter+1

        if xxcounter> (len(exp_image_list)-1):
            xxcounter=0
            xxlocation=0
            didsomethingexplode=0 






font=pygame.font.SysFont("Arial", 36)
smallfont=pygame.font.SysFont("Arial", 20)
medfont=pygame.font.SysFont("Arial", 30)

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


def keyPressed(inputKey):
    
    keysPressed = pygame.key.get_pressed()

    if keysPressed[inputKey]:
        #key_currently_up=False
        return True
    else:
        return False
        
def keyPressedmenu():
    
    keysPressed = pygame.key.get_pressed()
    while keysPressed != K_1 or keysPressed != 2:
        print ('waiting for 1')
        keysPressed = pygame.key.get_pressed()
        print (keyPressed)
    if keysPressed ==K_1:
        print(1)
        return 1
    if keysPressed ==2:
        print(2)
        return 2

#font2=pygame.font.SysFont(
pygame.mixer.init()
warpSound=pygame.mixer.Sound('jumpsound3.wav')
hullhit=pygame.mixer.Sound('hullhit.wav')
dangersound=pygame.mixer.Sound('danger.wav')
ffieldSound1=pygame.mixer.Sound('force1.wav')
ffieldSound2=pygame.mixer.Sound('force2.wav')
ffieldSound3=pygame.mixer.Sound('force3.wav')
fieldsounds=[ffieldSound1,ffieldSound2,ffieldSound3]
expsound1=pygame.mixer.Sound('exp1.wav')
expsound2=pygame.mixer.Sound('exp2.wav')
expsound3=pygame.mixer.Sound('exp3.wav')
expsound4=pygame.mixer.Sound('exp4.wav')
expsounds=[expsound1,expsound2,expsound3, expsound4]

bgmusic=pygame.mixer.Sound('beginmusic.wav')

menumusic=pygame.mixer.Sound('menumusic.wav')

lv1music=pygame.mixer.Sound('morelevelmusic1.wav')
lv2music=pygame.mixer.Sound('morelevelmusic2.wav')
lv3music=pygame.mixer.Sound('morelevelmusic3.wav')
lv4music=pygame.mixer.Sound('morelevelmusic4.wav')
lv5music=pygame.mixer.Sound('morelevelmusic5.wav') #xcv no 5 music yet
musics=[lv1music, lv2music, lv3music, lv4music, lv5music]


gameOverSound=pygame.mixer.Sound('gameover.wav')


playerImage = pygame.image.load('trans.png')
pii=pygame.transform.scale(playerImage, (90,30))


piiY=pii.get_rect().centery
piiX=pii.get_rect().centerx
#print (piiY)
#piiX=pii.centerX
#playerRect=pygame.Rect(0,0,30,10)


playerImage2 = pygame.image.load('jet.png')
pii2=pygame.transform.scale(playerImage2, (90,30))
playerRect2=pygame.Rect(0,0,10,10)
#xcvb

blackimage = pygame.image.load('blackpic.png')
exp1nImage = pygame.image.load('exp1.png')
exp2nImage = pygame.image.load('exp2.png')
exp3nImage = pygame.image.load('exp3.png')
exp4nImage = pygame.image.load('exp4.png')


exp1Image = pygame.transform.scale(exp1nImage, (150,150))
exp2Image = pygame.transform.scale(exp2nImage, (150,150))
exp3Image = pygame.transform.scale(exp3nImage, (150,150))
exp4Image = pygame.transform.scale(exp4nImage, (150,150))
#exp_image_list=[blackimage, exp1Image, blackimage, exp2Image, blackimage, exp3Image, blackimage, exp4Image, blackimage]
exp_image_list=[exp1Image,exp1Image,exp1Image,exp1Image, exp1Image, exp1Image, blackimage, exp2Image,exp2Image,exp2Image,exp2Image, exp2Image,exp2Image, exp3Image,exp3Image,exp3Image,exp3Image, exp3Image,exp3Image, exp4Image,exp4Image,exp4Image,exp4Image,exp4Image,exp4Image]



bossImage = pygame.image.load('boss.png')
distImage = pygame.image.load('disrupt2.png')
turretImage = pygame.image.load('turret.png')
baddieImage = pygame.image.load('badguy.png')
starImage= pygame.image.load('star.jpg')

asteroidImage= pygame.image.load('asteroid.png')
asteroidImage2= pygame.image.load('asteroid2.png')
asteroidImage3= pygame.image.load('asteroid3.png')
astImagelist=[asteroidImage, asteroidImage2,asteroidImage3]

shotimageint=pygame.image.load('glaser.png')
shotimage=pygame.transform.scale(shotimageint, (50,50))
#doesnt do anything^^ size is rescaled in []
eshotimageint=pygame.image.load('rlaser.png')

bossbulletimageint=pygame.image.load('blaser.png')
bossbulletimage=pygame.transform.scale(bossbulletimageint, (20,20))

bulletimageint=pygame.image.load('laser.png')
bulletimage=pygame.transform.scale(bulletimageint, (20,20))

drawTextmine('Gravline: Zero', font, windowSurface, (WINDOWWIDTH/3), (WINDOWHEIGHT/3), BLUE)
drawText('Press key to start', smallfont, windowSurface, ((WINDOWWIDTH/3)+40), (WINDOWHEIGHT/3)+90)
drawTextmine('Controls:  Keypad to move', medfont, windowSurface, 100, 500, WHITE)
drawTextmine('Hold F to fire   B to use limited Bombs', medfont, windowSurface, 100, 550, WHITE)
#
#drawTextmine('this is test', font, windowSurface, (WINDOWWIDTH/3)-30, (WINDOWHEIGHT/3)+50, BLUE)

pygame.display.update()
waitForPlayerToPressKey()


truetime=0


#ic=input condition and time is the crude time
def talking_in_game(IC, time):
    global truetime
    global timeleft
    #global shottime
    rectsmall=pygame.Rect((WINDOWWIDTH-90), 0, 50, 50)
    guy1imageintgame=pygame.image.load('guy1.png')
    guy1imagegame=pygame.transform.scale(guy1imageintgame, (90,90))
    girl1imageintgame=pygame.image.load('girl1.png')
    girl1imagegame=pygame.transform.scale(girl1imageintgame, (90,90))
    girl2imageintgame=pygame.image.load('girl2.png')
    girl2imagegame=pygame.transform.scale(girl2imageintgame, (90,90))
    girl3imageintgame=pygame.image.load('girl3.png')
    girl3imagegame=pygame.transform.scale(girl3imageintgame, (90,90))
    
    if IC==0:
        return
#light shield
    if IC==1:
        drawTextmine(' "..." ', medfont, windowSurface, 750, 40, BLUE)
        windowSurface.blit(guy1imagegame, rectsmall)

    if IC==2:
        drawTextmine(' "Shields hit but holding" ', medfont, windowSurface, 750, 40, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)

    if IC==3:
        drawTextmine(' "Come on Dax, dodge!" ', medfont, windowSurface, 750, 40, RED)
        windowSurface.blit(girl2imagegame, rectsmall)

    if IC==4:
        drawTextmine(' "I can\'t keep shooting  ', medfont, windowSurface, 700, 20, PURP)
        drawTextmine(' if you keep getting hit!" ', medfont, windowSurface, 700, 60, PURP)
        windowSurface.blit(girl3imagegame, rectsmall)

    if IC==5:
        drawTextmine(' "Damn" ', medfont, windowSurface, 750, 40, BLUE)
        windowSurface.blit(guy1imagegame, rectsmall)           


#heavy shield
    if IC==6:
        drawTextmine(' "Shields fading fast..." ', medfont, windowSurface, 750, 40, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)

    if IC==7:
        drawTextmine(' "Another shield generator failed." ', medfont, windowSurface, 750, 40, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)

    if IC==8:
        drawTextmine(' "I barely even see the shield!!!" ', medfont, windowSurface, 750, 40, RED)
        windowSurface.blit(girl2imagegame, rectsmall)

    if IC==9:
        drawTextmine(' "At least my shot is clear."  ', medfont, windowSurface, 700, 20, PURP)
        windowSurface.blit(girl3imagegame, rectsmall)

    if IC==10:
        drawTextmine(' (Where did that one come from!?) ', medfont, windowSurface, 750, 40, BLUE)
        windowSurface.blit(guy1imagegame, rectsmall)
        
    if IC==11:
        drawTextmine(' "We have lost shields..." ', medfont, windowSurface, 750, 20, LGREEN)
        drawTextmine(' "Repeat, shields are now down" ', medfont, windowSurface, 750, 60, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall) 

#light hull damage
    if IC==12:
        drawTextmine(' "Gah..." ', medfont, windowSurface, 750, 40, BLUE)
        windowSurface.blit(guy1imagegame, rectsmall)

    if IC==13:
        drawTextmine(' "Multiple explosions reported" ', medfont, windowSurface, 750, 40, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)

    if IC==14:
        drawTextmine(' "Ahhh!" ', medfont, windowSurface, 750, 40, RED)
        windowSurface.blit(girl2imagegame, rectsmall)

    if IC==15:
        drawTextmine(' "Weapon\'s hit..."  ', medfont, windowSurface, 700, 20, PURP)
        drawTextmine(' "...got them back" ', medfont, windowSurface, 700, 60, PURP)
        windowSurface.blit(girl3imagegame, rectsmall)

    if IC==16:
        drawTextmine(' (Come on, I can do this) ', medfont, windowSurface, 750, 40, BLUE)
        windowSurface.blit(guy1imagegame, rectsmall)


#heavy damage
    if IC==17:
        drawTextmine(' "The ship is barely holding together." ', medfont, windowSurface, 750, 40, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)

    if IC==18:
        drawTextmine(' "I don\'t want to die!!!" ', medfont, windowSurface, 750, 40, RED)
        windowSurface.blit(girl2imagegame, rectsmall)

    if IC==19:
        drawTextmine(' "What a patheic commander" ', medfont, windowSurface, 750, 20, PURP)
        drawTextmine(' "I should have killed you" ', medfont, windowSurface, 750, 60, PURP)        
        windowSurface.blit(girl3imagegame, rectsmall)

    if IC==20:
        drawTextmine(' "Guess now would be the time to say..."  ', medfont, windowSurface, 700, 20, LGREEN)
        drawTextmine(' "...Nevermind, I\'ll take it to my grave" ', medfont, windowSurface, 700, 60, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)

    if IC==21:
        drawTextmine(' "This is it." ', medfont, windowSurface, 750, 40, BLUE)
        windowSurface.blit(guy1imagegame, rectsmall)

    if IC==22:
        drawTextmine(' "Core systems failing." ', medfont, windowSurface, 750, 20, LGREEN)
        drawTextmine(' "Ship destruction emminent." ', medfont, windowSurface, 750, 60, LGREEN)        
        windowSurface.blit(girl1imagegame, rectsmall)        
        
    if IC ==23 and time <=2:
        
        drawTextmine(' "Engage Grav-Jump." ', medfont, windowSurface, 750, 40, BLUE)
        windowSurface.blit(guy1imagegame, rectsmall)

    if IC==23 and time >2 and time <3:
        drawTextmine(' "Copy that!" ', medfont, windowSurface, 750, 40, RED)
        windowSurface.blit(girl2imagegame, rectsmall)

    if IC==23 and time >3 and time <4:
        drawTextmine(' "Lets get out of here!" ', medfont, windowSurface, 750, 40, PURP)  
        windowSurface.blit(girl3imagegame, rectsmall)  

    if IC==23 and time >4 and time <6:
      
        drawTextmine(' "Charging Grav-Engines!!!" ', medfont, windowSurface, 750, 40, RED)
        windowSurface.blit(girl2imagegame, rectsmall)

    if IC==23 and time >6 and time <7:
      
        drawTextmine(' "To think the Burn are attacking..."', medfont, windowSurface, 700, 20, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)

    if IC==23 and time >7 and time <8:
      
        drawTextmine(' "They killed our whole fleet..."', medfont, windowSurface, 700, 20, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)        

    if IC==24 and time >26 and time <28:
        drawTextmine(' "We might make it..."', medfont, windowSurface, 700, 20, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)

    if IC==24 and time >28:
        drawTextmine(' "Grav Engines almost charged!!!"', medfont, windowSurface, 750, 40, RED)
        windowSurface.blit(girl2imagegame, rectsmall)

#level2
        #truetime is for when the counter isnt going down
    if IC ==25 and truetime <=1:
        
        drawTextmine(' "Get us out of here Galil"', medfont, windowSurface, 750, 40, BLUE)
        windowSurface.blit(guy1imagegame, rectsmall)

    if IC ==25 and truetime >1 and truetime<3:
        drawTextmine(' "The engines aren\'t charging!"', medfont, windowSurface, 750, 40, RED)
        windowSurface.blit(girl2imagegame, rectsmall)

    if IC ==25 and truetime >3 and truetime<6:
        drawTextmine(' "Those machines...Grav-Disruptors!"', medfont, windowSurface, 700, 20, PURP)
        drawTextmine('"Kill them so we can charge the engines!"', medfont, windowSurface, 700, 60, PURP) 
        windowSurface.blit(girl3imagegame, rectsmall)
        #then it switches to the actual level count
    if IC==26 and time>0 and time<2:

        drawTextmine(' "Grav-disruption gone!"', medfont, windowSurface, 700, 20, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)
    if IC==26 and time>2 and time<5:        
        drawTextmine('"Engines charging again!"', medfont, windowSurface, 750, 20, RED)
        drawTextmine('"Keep us alive until then Dax!"', medfont, windowSurface, 750, 60, RED)        
        windowSurface.blit(girl2imagegame, rectsmall)
    if IC==26 and time>5 and time<6: 
        drawTextmine(' "No problem."', medfont, windowSurface, 750, 40, BLUE)
        windowSurface.blit(guy1imagegame, rectsmall)
        
#this is assinged below when level clock gets low
    if IC==27:
        drawTextmine(' "We almost made it!', medfont, windowSurface, 750, 20, RED)
        drawTextmine(' "We almost made it!!!', medfont, windowSurface, 750, 60, RED)        
        windowSurface.blit(girl2imagegame, rectsmall)

        
#27 concludes r2

    if IC==28 and truetime <2:
        drawTextmine(' "More Grav-Disruptors!"', medfont, windowSurface, 700, 20, LGREEN)
        drawTextmine(' "Niko!"', medfont, windowSurface, 700, 60, LGREEN)        
        windowSurface.blit(girl1imagegame, rectsmall)        


    if IC==28 and truetime >2 and truetime <4:
        drawTextmine(' "On it!  Don\'t worry your', medfont, windowSurface, 700, 20, PURP)
        drawTextmine('"pretty little face Lavine!"', medfont, windowSurface, 700, 60, PURP) 
        windowSurface.blit(girl3imagegame, rectsmall)

    if IC==28 and truetime >4 and truetime <5:
        drawTextmine(' "Something else...', medfont, windowSurface, 700, 20, LGREEN)
        drawTextmine(' "Asteroids!"', medfont, windowSurface, 700, 60, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall) 
    if IC==28 and truetime >5 and truetime <8:
        drawTextmine(' "Our laser will be useless"', medfont, windowSurface, 750, 40, BLUE)
        windowSurface.blit(guy1imagegame, rectsmall)          

    if IC==29 and time>0 and time<2:

        drawTextmine(' "Disruptors gone, Galil!', medfont, windowSurface, 700, 20, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)

    if IC==29 and time>2 and time<4:
        drawTextmine(' "I\'m hitting it!"', medfont, windowSurface, 750, 20, RED)   
        windowSurface.blit(girl2imagegame, rectsmall)

    if IC==30 and timeleft<4 and timeleft>2:
        drawTextmine(' "We are almost there!"', medfont, windowSurface, 750, 20, RED)   
        windowSurface.blit(girl2imagegame, rectsmall)
    if IC==30 and timeleft<2 and timeleft>0:           
        drawTextmine(' "We are going to make it..."', medfont, windowSurface, 700, 20, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)

        
#finished lv 3 asteroids

        
    if IC==31 and truetime <2:
        drawTextmine(' "I am picking up strong', medfont, windowSurface, 700, 20, LGREEN)
        drawTextmine(' energy readings!"', medfont, windowSurface, 700, 60, LGREEN)        
        windowSurface.blit(girl1imagegame, rectsmall)        


    if IC==31 and truetime >2 and truetime <4:
        drawTextmine(' "No way...', medfont, windowSurface, 750, 20, BLUE)
        drawTextmine(' Burn defense turrets!"', medfont, windowSurface, 750, 60, BLUE)        
        windowSurface.blit(guy1imagegame, rectsmall)

    if IC==31 and truetime >4 and truetime <6:
        drawTextmine('"Damn it! How much am I ', medfont, windowSurface, 700, 20, PURP)
        drawTextmine(' expected to kill!?"', medfont, windowSurface, 700, 60, PURP) 
        windowSurface.blit(girl3imagegame, rectsmall)        
    if IC==31 and truetime >6 and truetime <8:
        drawTextmine(' "Hurry and take the ', medfont, windowSurface, 750, 20, RED)
        drawTextmine(' disruptors down!"', medfont, windowSurface, 750, 50, RED)         
        windowSurface.blit(girl2imagegame, rectsmall)        
         

    if IC==32 and time>0 and time<2:
        drawTextmine(' "Got them!  Engines charging!', medfont, windowSurface, 750, 20, RED)   
        windowSurface.blit(girl2imagegame, rectsmall)     

    if IC==32 and time>2 and time<4:
        drawTextmine(' "Come on Dax, get us out of here"', medfont, windowSurface, 700, 20, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)

    if IC==33 and timeleft<4 and timeleft>2:
        drawTextmine(' "Come on Radiant', medfont, windowSurface, 750, 20, BLUE)
        drawTextmine(' hold together a little longer."', medfont, windowSurface, 750, 60, BLUE)        
        windowSurface.blit(guy1imagegame, rectsmall)
    if IC==33 and timeleft<2 and timeleft>0:           
        drawTextmine('"Just a few more...!"', medfont, windowSurface, 750, 60, BLUE)        
        windowSurface.blit(guy1imagegame, rectsmall)



#lv5
        
    if IC==34 and truetime <2:

        drawTextmine(' "Holy shit....', medfont, windowSurface, 750, 20, BLUE)
        drawTextmine(' A Burn Cruiser!!!"', medfont, windowSurface, 750, 60, BLUE)        
        windowSurface.blit(guy1imagegame, rectsmall)      


    if IC==34 and truetime >2 and truetime <4:
        drawTextmine('"Damn! ', medfont, windowSurface, 700, 20, PURP)
        drawTextmine('Can we beat something like that!?"', medfont, windowSurface, 700, 60, PURP) 
        windowSurface.blit(girl3imagegame, rectsmall) 

    if IC==34 and truetime >4 and truetime <6:
        drawTextmine(' "Dax!!!', medfont, windowSurface, 750, 20, RED)
        drawTextmine(' Do Something!!"', medfont, windowSurface, 750, 50, RED)         
        windowSurface.blit(girl2imagegame, rectsmall)          
       
    if IC==34 and truetime >6 and truetime <8:
        drawTextmine(' "I\'m doing everything I can!', medfont, windowSurface, 750, 20, BLUE)
        drawTextmine(' Let\'s do this Radiant!"', medfont, windowSurface, 750, 60, BLUE)        
        windowSurface.blit(guy1imagegame, rectsmall)        
         

    if IC==35 and time>0 and time<2:
        drawTextmine(' "Ok we are clear, we can do this!', medfont, windowSurface, 750, 20, RED)   
        windowSurface.blit(girl2imagegame, rectsmall)     

    if IC==35 and time>2 and time<4:
        drawTextmine(' "Come on Dax, get us out of here"', medfont, windowSurface, 700, 20, LGREEN)
        windowSurface.blit(girl1imagegame, rectsmall)

    if IC==36 and timeleft<4 and timeleft>2:
        drawTextmine(' "Radaint, don\'t fail us now...', medfont, windowSurface, 750, 20, BLUE)
        drawTextmine(' Just a little further...."', medfont, windowSurface, 750, 60, BLUE)        
        windowSurface.blit(guy1imagegame, rectsmall)
    if IC==36 and timeleft<2 and timeleft>0:           
        drawTextmine('"Come on!!!"', medfont, windowSurface, 750, 60, BLUE)        
        windowSurface.blit(guy1imagegame, rectsmall)       

def main():
    #while True:
    global beatlevel
    global timeleft
    timefinish=True
    died=False
    madeittoend=False
    IC=0

    currentmusic=musics[beatlevel]
#    currentmusic.play()
    currentmusic.play(-1,0)
        #make a list and jsut march down the list
    
    while True:        
        global topScore
        beatlevel
        global shields
        global hull
        global relationshippoints
        global dis_count
        global turret_count
        global boss_count
        global megacrush
        global truetime
        #global timeleft
        roundstarthull=hull
        megacrushkey_currently_up=True
        delay_shot=False
        #PLAYERMOVERATE=8

        global xxcounter
        global didsomethingexplode

        global xxlocation

        disruptor=[]
        turrets=[]
        shots=[]
        baddies=[]
        stars=[]
        bullets=[]
        eshots=[]
        asteroids=[]
        boss=[]
        bshots=[]
        score=0
        playerRect.topleft=(200, 200)
        #-30 and -10
        playerRect2.topleft=(170, 190)
        
        moveLeft=moveRight=moveUp=moveDown=False
        baddieAddCounter=0
        starAddCounter=0
        bulletAddCounter=0
        asteroidAddCounter=0        
        bossbulletAddCounter=0        
        shot=False
        scoremod=0
        f_button=0
        b_button=0
        dangermusic=False
        shottime=0
        tshottime=0
        bossshottime=0
        talktime=0
        truetime=0
        crudetime=0

        movingup=True
       
        while timefinish==True and died==False:


            if len(disruptor)==0:
                
                score=(score+1) #xcv possibly based on anything 
            crudetime=score/100.
            #what is interseting is that crude time becomes .001 here
            timeleft3=round(crudetime,2)
            timeleft2=roundtimer #assinged up top
            #timeleft2=3
            timeleft=timeleft2-timeleft3
            timeleft=round(timeleft,2)
            #print(timeleft)
           
            talktime=talktime+1
            truetime=(talktime/100)
            
            shottime= (shottime+1)
            tshottime=(tshottime+1)
            bossshottime=(bossshottime+1)            
            #print (shottime)
            #shotrepeat

            if timeleft<=0:
                timefinish=False
                madeittoend=True

            if hull<5:
                dangermusic=True
            if hull <1:
                dangermusic=False
            if dangermusic==True:
                dangersound.play()
            if dangermusic==False:
                dangersound.stop()

            while shottime> rapid_fire_constant:
                #print (shottime)
                shottime = 0
                #print(shottime)
                #print ('cleared shot')
                delay_shot=True
            #if shottime < 1:
                #delay_shot=False



            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                    #refrenced here and lower
                if event.type == KEYDOWN:
                    keyPressed(K_LEFT)
                    keyPressed(K_RIGHT)
                    keyPressed(K_UP)
                    keyPressed(K_DOWN)
                    keyPressed(ord('f'))


                        #nice, set a extra flag, and have it reverse after the effect (ie down below)
                    keyPressed(K_SPACE)
                    
                    if keyPressed(ord('b')) and megacrushkey_currently_up==True:
                        print(megacrushkey_currently_up)
                        b_button=1
                        megacrushkey_currently_up=False

                        
                if event.type==KEYUP:                    
                    if event.key==(ord('b')):
                        megacrushkey_currently_up=True
                        print(megacrushkey_currently_up)
                    #this is necessary to have otherwise, EVERY movement shoots as well
                        
                if event.type==KEYUP:                    
                    if event.key==K_ESCAPE:
                        terminate()                
                #if event.type==MOUSEMOTION:
                    #playerRect.move_ip(event.pos[0]- playerRect.centerx, event.pos[1]-playerRect.centery)

                        
            baddieAddCounter +=1
            starAddCounter +=1
            asteroidAddCounter +=1            
            
            bulletaddrate=len(baddies)#*ADDNEWBULLETRATE
            bulletAddCounter+=bulletaddrate




            if starAddCounter==ADDNEWSTARRATE:

                starAddCounter=0
                starSize= random.randint(STARMINSIZE,STARMAXSIZE)
                newStar={'rect':pygame.Rect(WINDOWWIDTH-starSize, random.randint(100,WINDOWHEIGHT), starSize, starSize),                                    
                           'speed': random.randint(STARMINSPEED, STARMAXSPEED),
                           'surface':pygame.transform.scale(starImage,(starSize, starSize)),}
                stars.append(newStar)


            if asteroidAddCounter==ADDNEWASTEROIDRATE and beatlevel>1:

                asteroidAddCounter=0
                astSpeed=random.randint(3,4)
                astSpeedY=random.randint(-1,2)
                localastran=random.randint(0,2)
                ranAstImage=astImagelist[localastran]


                
                asteroidSize= random.randint(ASTEROIDMINSIZE,ASTEROIDMAXSIZE)
                newAsteroid={'rect':pygame.Rect(WINDOWWIDTH-asteroidSize, random.randint(100,WINDOWHEIGHT), asteroidSize, asteroidSize),                                    
                           'speedx': astSpeed, 'speedy': astSpeedY, 'hp': 5,
                           'surface':pygame.transform.scale(ranAstImage,(asteroidSize, asteroidSize)),}
                asteroids.append(newAsteroid)

                
                #where they are added
            if baddieAddCounter==ADDNEWBADDIERATE:
                baddieAddCounter=0
                baddieSize= random.randint(BADDIEMINSIZE,BADDIEMAXSIZE)
                newBaddie={'rect':pygame.Rect(WINDOWWIDTH, random.randint(100,WINDOWHEIGHT), (baddieSize-5), (baddieSize-5)),                                    
                           'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                           'surface':pygame.transform.scale(baddieImage,(baddieSize, baddieSize)),}
                baddies.append(newBaddie)


            #distruptor add
            if beatlevel>0 and dis_count==9999: 
                dis_count=beatlevel             
                while dis_count>=0:
                    newDist={'rect':pygame.Rect((random.randint(700,(WINDOWWIDTH-100)), random.randint(100,(WINDOWHEIGHT-100)), 75, 75)),                                    
                               'hp': 5,
                               'surface':pygame.transform.scale(distImage,(75, 75)),}
                    dis_count=dis_count-1
                    disruptor.append(newDist)




            #boss
            if beatlevel>3 and boss_count==9999:
                boss_count=0

                newboss={'rect':pygame.Rect(900, 300, 150, 150),                                    
                           'hp': 30,
                           'surface':pygame.transform.scale(bossImage,(200, 200)),}
                boss.append(newboss)



            if beatlevel>2 and turret_count==9999: 
                turret_count=beatlevel             
                while turret_count>=0:
                    newTurret={'rect':pygame.Rect((random.randint(700,(WINDOWWIDTH-100)), random.randint(100,(WINDOWHEIGHT-100)), 75, 75)),                                    
                               'hp': 7,
                               'surface':pygame.transform.scale(turretImage,(50, 50)),}
                    turret_count=turret_count-1
                    turrets.append(newTurret)                    
                    



                #laser shots
            if keyPressed(ord('f')) and delay_shot==True:
                #print ('getting here')
                shotsize=20
                shotspeed=10
                newShot={'rect':pygame.Rect(playerRect.right, playerRect.top, 20,20),              
                         'speed':shotspeed,
                         'surface':pygame.transform.scale(shotimageint, (20,20)),}
                shots.append(newShot)
                f_button=0
                delay_shot=False
                #print (delay_shot)
                #print(len(shots))



            if bulletAddCounter >= BULLETTHRESHOLD:
               # print ('getting here')
                bulletAddCounter=0
                #bulletSize= random.randint(BULLETMINSIZE,BULLETMAXSIZE)
                bulletSpeed=random.randint(1,8)
                bulletSpeedY=random.randint(-3,3)                
                for b in baddies:
                    totalbad=len(baddies)
                    randombad=random.randint(0,totalbad-1)
                    #ok, so this is giving me a number related to someone in there
                    #Now need to assing shot location
                badguyIMusing= baddies[randombad]
                #print(badguyIMusing)
                test1=badguyIMusing['rect']
                #print(test1)
                test2=test1.left
                #print(test2)
                test3=test1.top
                #print('this is left')
                Bdirectionx=playerRect.centerx
                Bdirectiony=playerRect.centery
                #randombadslocationy= baddies['rect'].centery
                #keeping this around to show what i thought, and how it works

                #direction needs to be towards fighter        
                newBullet={'rect':pygame.Rect(test2, test3, 20, 20),                                    
                           'speed': bulletSpeed,
                           'speedY': bulletSpeedY,
                           'surface':pygame.transform.scale(bulletimageint,(20, 20)),}
                bullets.append(newBullet)

                    #randomly choose between these in length
                #print(len(bullets))
                #print('this is bullet length')



            if tshottime >= eb_add_rate and len(turrets)>0:
                tshottime=0              
                for t in turrets:
                    #this was pretty hard, but note how to drag something out of dict
                    #to use for other things
                    localturret=t
                    localrect=localturret['rect']
                    
                    randomy=random.randint(-3,3)                   
                    neweshot={'rect':pygame.Rect(localrect.left, localrect.top, 20, 20),
                               'speed': 6,
                               'speedY': randomy,
                               'surface':pygame.transform.scale(eshotimageint,(20, 20)),}
                    eshots.append(neweshot)

#xcvb boss
            if bossshottime >= bossbullet_add_rate:
                bossshottime=0              
                for b in boss:
                    #this was pretty hard, but note how to drag something out of dict
                    #to use for other things
                    localrect=b['rect']                 
                    newbshot={'rect':pygame.Rect(localrect.left, localrect.centery, 30, 30),
                               'speed': 6,
                               'surface':pygame.transform.scale(bossbulletimageint,(30, 30)),}
                    bshots.append(newbshot)

                
            if keyPressed(K_LEFT) and playerRect.left >0:
                playerRect.move_ip(-1*PLAYERMOVERATE,0)
            if keyPressed(K_RIGHT) and playerRect.right <WINDOWWIDTH:
                playerRect.move_ip(+1*PLAYERMOVERATE,0)
            if keyPressed(K_UP) and playerRect.top >100:
                playerRect.move_ip(0, -1*PLAYERMOVERATE)
            if keyPressed(K_DOWN) and playerRect.bottom< WINDOWHEIGHT:
                playerRect.move_ip(0, +1*PLAYERMOVERATE)


#notable is the -50 part because the hitbox is biger for the real, than the fake one
            if keyPressed(K_LEFT) and playerRect2.left >-30:
                playerRect2.move_ip(-1*PLAYERMOVERATE,0)
            if keyPressed(K_RIGHT) and playerRect2.right <(WINDOWWIDTH-50):
                playerRect2.move_ip(+1*PLAYERMOVERATE,0)
            if keyPressed(K_UP) and playerRect2.top >90:
                playerRect2.move_ip(0, -1*PLAYERMOVERATE)
            if keyPressed(K_DOWN) and playerRect2.bottom< (WINDOWHEIGHT-10):
                playerRect2.move_ip(0, +1*PLAYERMOVERATE)                




            windowSurface.fill(BACKGROUNDCOLOR)


            drawTextmine('Hull: %s' %(hull), font, windowSurface, 10, 0, RED)
            drawTextmine('Shields: %s' % (shields), font,windowSurface, 10, 40, LIGHTBLUE)
            drawText('Megacrush: %s' %(megacrush), font, windowSurface, 300, 0)
            drawText('Time Till Jump: %s' %(timeleft), font, windowSurface, 300, 50)            

            #hey, hell yeah, his pic naturally dissappers

            if crudetime>=0 and crudetime<=8 and beatlevel==0:       
                IC=23
            if crudetime>=26 and crudetime<=30 and beatlevel==0:       
                IC=24
            #level2 stuff
            if truetime <8 and beatlevel==1:
                IC=25
            if crudetime>.1 and beatlevel==1 and crudetime<6:
                IC=26
            if timeleft <2 and beatlevel==1:
                crudetime=2
                IC=27
                talking_in_game(IC, crudetime)


            #level 3 (asteroid)
                
            if truetime <8 and beatlevel==2:
                IC=28
            if crudetime>.1 and beatlevel==2 and crudetime<4:
                IC=29
            if timeleft <4 and beatlevel==2:
                IC=30
                #talking_in_game(IC, crudetime)

                #lv4 turrets
            if truetime <8 and beatlevel==3:
                IC=31
            if crudetime>.1 and beatlevel==3 and crudetime<4:
                IC=32
            if timeleft <4 and beatlevel==3:
                IC=33

                #lv5 boss
            if truetime <8 and beatlevel==4:
                IC=34
            if crudetime>.1 and beatlevel==4 and crudetime<4:
                IC=35
            if timeleft <4 and beatlevel==4:
                IC=36
            
            if shields==0 and hull==roundstarthull:
                IC=11
            if hull==4:
                IC=22
            #if shields <1:
                #IC=12

            talking_in_game(IC, crudetime)
                #print(crudetime)
            
            

            windowSurface.blit(pii, playerRect)
            windowSurface.blit(pii2, playerRect2)
            #windowSurface.blit(pii2, playerRect)
#xcvb

#can be taken out, this is merely hit box
            #pygame.draw.rect(windowSurface, WHITE, playerRect)
            #pygame.draw.rect(windowSurface, WHITE, playerRect2)
            
            pygame.draw.lines(windowSurface, BLUE, False, [(0,90), (WINDOWWIDTH,90)], 5)
            pygame.draw.lines(windowSurface, BLUE, False, [(690,0), (690,90)], 5)

            for b in baddies:
                b['rect'].move_ip(-b['speed'], 0)                
                if b['rect'].right<0:
                    baddies.remove(b)
                windowSurface.blit(b['surface'],b['rect'])

            for b in boss:
                if movingup==True:
                    b['rect'].move_ip(0, -2)
                if b['rect'].top<=90:
                    movingup=False
                if movingup==False:
                    b['rect'].move_ip(0, 2)
                if b['rect'].bottom==600:
                   movingup=True                    
                windowSurface.blit(b['surface'],b['rect'])                


            for d in disruptor:
                windowSurface.blit(d['surface'],d['rect'])

            for t in turrets:
                windowSurface.blit(t['surface'],t['rect'])                   

            for s in stars:
                s['rect'].move_ip(-s['speed'],0)
                if s['rect'].right<0:
                    stars.remove(s)
                windowSurface.blit(s['surface'],s['rect'])

            for l in shots[:]:
                l['rect'].move_ip(+l['speed'],0)
                windowSurface.blit(l['surface'],l['rect'])
                try:
                    if l['rect'].left>WINDOWWIDTH:
                        shots.remove(l)
                except: pass
                #print(len(shots))

            #this adds a random wave effect to the shots
            #for l in shots:
                #tfdx=random.randint(-5,5)
                #l['rect'].move_ip(+l['speed'],tfdx)
                #windowSurface.blit(l['surface'],l['rect'])
                #try:
                    #if l['rect'].left>WINDOWWIDTH:
                        #shots.remove(s)
                #except:pass                

            for b in bullets:
                b['rect'].move_ip(-b['speed'],b['speedY'])
                windowSurface.blit(b['surface'],b['rect'])
                try:
                    if b['rect'].right<0:
                        bullets.remove(b)
                except:pass                      
                try:
                    if b['rect'].top<90:
                        bullets.remove(b)
                except:pass                            
                try:
                    if b['rect'].top>WINDOWHEIGHT:
                        bullets.remove(b)
                except:pass

            for e in eshots:
                e['rect'].move_ip(-e['speed'],e['speedY'])
                windowSurface.blit(e['surface'],e['rect'])
                try:
                    if e['rect'].right<0:
                        eshots.remove(e)
                except:pass                      
                try:
                    if e['rect'].top<90:
                        eshots.remove(e)
                except:pass                            
                try:
                    if e['rect'].top>WINDOWHEIGHT:
                        eshots.remove(e)
                except:pass                


            for b in bshots:
                b['rect'].move_ip(-b['speed'],0)
                windowSurface.blit(b['surface'],b['rect'])
                try:
                    if e['rect'].right<0:
                        eshots.remove(e)
                except:pass                      

                

            for b in asteroids:
                b['rect'].move_ip(-b['speedx'],b['speedy'])
                windowSurface.blit(b['surface'],b['rect'])
                try:
                    if b['rect'].right<0:
                        asteroids.remove(b)
                except:pass                      
                try:
                    if b['rect'].top<90:
                        asteroids.remove(b)
                except:pass                            
                try:
                    if b['rect'].top>WINDOWHEIGHT:
                        asteroids.remove(s)
                except:pass                  
                        
            pygame.display.update()              
                

            if keyPressed(ord('b')) and b_button==1 and megacrush>0:

                #Posistion, size, location
                for x in range(0,50):
                    localrect=pygame.Rect((WINDOWWIDTH/2),(WINDOWHEIGHT/2), 10,10)
                    localrect.move_ip(-(10*x),-(10*x))
                    MCImage = pygame.image.load('laser.jpg')
                    MCii=pygame.transform.scale(MCImage, ((20*x),(20*x)))
                    #MCImage.move_ip(-(5*x),-(5*x))
                    #print(growingrect)
                    windowSurface.blit(MCii, localrect)

                    pygame.display.update()                    
                #for b in baddies[:]:
                    #baddies.remove(b)
                #b_button=0
                #megacrushleft-=1
                #xcvb mega can remove these
                for b in baddies[:]:
                    baddies.remove(b)
                for l in bullets[:]:
                    bullets.remove(l)
                for e in eshots[:]:
                    eshots.remove(e)                    
                b_button=0
                megacrush=megacrush-1


            if playerHasHitBaddie(playerRect, baddies):
                if shields==0:
                    hull-=1
                    hullhit.play()
                    if hull >5:    
                        randscream=random.randint(12,16)
                    if hull <6:
                        randscream=random.randint(17,21)            
                if shields>0:
                    shields-=1
                    randfield=random.randint(0,2)
                    currentsound=fieldsounds[randfield]
                    currentsound.play()
                    if shields >5:    
                        randscream=random.randint(1,5)
                    if shields <6:
                        randscream=random.randint(6,10)
                for b in baddies[:]:
                    if b['rect'].colliderect(playerRect):
                        baddies.remove(b)
                
                IC=randscream
    #for a mega crush after taking hit, use below
                #for b in baddies[:]:
                    #baddies.remove(b)

            if playerHITbullet(playerRect, bullets):
                if shields==0:
                    hull-=1
                    hullhit.play()
                    if hull >5:    
                        randscream=random.randint(12,16)
                    if hull <6:
                        randscream=random.randint(17,21)                  
                if shields>0:
                    shields-=1
                    randfield=random.randint(0,2)
                    currentsound=fieldsounds[randfield]
                    currentsound.play()
                    if shields >5:    
                        randscream=random.randint(1,5)
                    if shields <6:
                        randscream=random.randint(6,10)

                for b in bullets[:]:
                    if b['rect'].colliderect(playerRect):
                        bullets.remove(b)                    
                IC=randscream

            if playerHITbullet(playerRect, eshots):
                if shields==0:
                    hull-=1
                    hullhit.play()
                    if hull >5:    
                        randscream=random.randint(12,16)
                    if hull <6:
                        randscream=random.randint(17,21)                  
                if shields>0:
                    shields-=1
                    randfield=random.randint(0,2)
                    currentsound=fieldsounds[randfield]
                    currentsound.play()
                    if shields >5:    
                        randscream=random.randint(1,5)
                    if shields <6:
                        randscream=random.randint(6,10)

                for e in eshots[:]:
                    if e['rect'].colliderect(playerRect):
                        eshots.remove(e)                    
                IC=randscream                  

            if playerHITbullet(playerRect, bshots):
                if shields==0:
                    hull-=1
                    hullhit.play()
                    if hull >5:    
                        randscream=random.randint(12,16)
                    if hull <6:
                        randscream=random.randint(17,21)                  
                if shields>0:
                    shields-=1
                    randfield=random.randint(0,2)
                    currentsound=fieldsounds[randfield]
                    currentsound.play()
                    if shields >5:    
                        randscream=random.randint(1,5)
                    if shields <6:
                        randscream=random.randint(6,10)

                for b in bshots[:]:
                    if b['rect'].colliderect(playerRect):
                        bshots.remove(b)                    
                IC=randscream   

            if playerHasHitAsteroid(playerRect, asteroids):
                if shields==0:
                    hull-=1
                    hullhit.play()
                    if hull >5:    
                        randscream=random.randint(12,16)
                    if hull <6:
                        randscream=random.randint(17,21)                  
                if shields>0:
                    shields-=1
                    randfield=random.randint(0,2)
                    currentsound=fieldsounds[randfield]
                    currentsound.play()
                    if shields >5:    
                        randscream=random.randint(1,5)
                    if shields <6:
                        randscream=random.randint(6,10)

                for b in asteroids[:]:
                    if b['rect'].colliderect(playerRect):
                        asteroids.remove(b)                    
                IC=randscream







####                                ###



            shothit(shots,baddies)
            shothit_hp(shots, asteroids)
            #shothitasteroid(shots,asteroids)
            shothit_hp(shots,disruptor)
            expanime()
            shothit_hp(shots, turrets)
            shothit_hp(shots,boss)





####                        ###







                      


              
            if hull<=0:
                died=True
                dangersound.stop()
                windowSurface.fill(BACKGROUNDCOLOR)
                #drawTextmine('Hull: %s' %(hull), font, windowSurface, 10, 0, RED)
                drawTextmine('Hull: DESTORYED', font, windowSurface, 10, 0, RED)
                #pygame.display.update()                
                #break
            pygame.display.update()


            #man, wtf is with timers
            #global Timeleft
            #print(mainClock)
            #pygame.time.set_timer(Timeleft,1000)
            #if Timeleft:
                #Timeleft=Timeleft-1
                #print(Timeleft)
                #print('time elft')
                
            mainClock.tick(FPS)
            


        if madeittoend==True:
            print('did i make it to end?')
            currentmusic.stop()
            dangersound.stop()
            #windowSurface.fill(BACKGROUNDCOLOR)
            pygame.display.update()
            warpSound.play()
            drawTextmine('Jump engaged!', font, windowSurface, (WINDOWWIDTH/3), (WINDOWHEIGHT/3), BLUE)
            pygame.display.update()
            time.sleep(1)
            for x in range(0,120):
                localrect2=pygame.Rect((WINDOWWIDTH/2),(WINDOWHEIGHT/2), 10,10)
                localrect2.move_ip(-(10*x),-(10*x))
                jumpimage = pygame.image.load('jump2.png')
                jumpii=pygame.transform.scale(jumpimage, ((20*x),(20*x)))
                #MCImage.move_ip(-(5*x),-(5*x))
                #print(growingrect)
                windowSurface.blit(jumpii, localrect2)

                pygame.display.update()
            windowSurface.fill(BACKGROUNDCOLOR)                
            drawText('Jump successful!', font, windowSurface, (WINDOWWIDTH/3), (WINDOWHEIGHT/3))
            pygame.display.update()
            time.sleep(2)

            beatlevel=beatlevel+1
            print(beatlevel)
            print('this is bl at end of level')
            relationshippoints+=1
            dis_count=9999
            turret_count=9999
            
            drawTextmine('GravLines remaining: %s'  %(5-beatlevel), font, windowSurface, 400, 400, RED)
            pygame.display.update()
            waitForPlayerToPressKey()

            
        if died==True:
            currentmusic.stop()
            gameOverSound.play()
            drawText('game over', font, windowSurface, (WINDOWWIDTH/3), (WINDOWHEIGHT/3))
            drawText('press button to go to main menu', font, windowSurface, (WINDOWWIDTH/3)-80, (WINDOWHEIGHT/3)+50)
            pygame.display.update()
            waitForPlayerToPressKey()
            gameOverSound.stop()  
            beatlevel=0
        #waitForPlayerToPressKey()
        #if event.type == KEYDOWN:
            #if event.key==keyPressed(ord('y')):
                #break



        break                            






###




    ###



    ####




###


    ###

def crewrelationship():


    ##relaitonships
    
    print ('relation start')
    global shieldmax
    global girl1_level
    global girl2_level
    global girl3_level
    global relationshippoints
    global roundtimer
    global playerRect
    global rapid_fire_constant
    global PLAYERMOVERATE
    global roundreduction
    print (relationshippoints)
    print('rp')
    exitvar=0
    non_help_charge_reduction=1
    non_help_laser_reduction=.9
    non_help_shield_increase=3
    non_help_hitbox_reduction=playerRect.inflate(-1,-1)
    galilreduce=2


    rectsmalllavine=pygame.Rect(0, 400, 100, 100)
    smLAVint=pygame.image.load('girl1.png')
    smLAV=pygame.transform.scale(smLAVint, (100,100))
    
    rectsmallgalil=pygame.Rect(0, 400, 100, 100)    
    smGALint=pygame.image.load('girl2.png')
    smGAL=pygame.transform.scale(smGALint, (100,100))

    rectsmallniko=pygame.Rect(0, 500, 100, 100)       
    smNIKOint=pygame.image.load('girl3.png')
    smNIKO=pygame.transform.scale(smNIKOint, (100,100))
    
    happyrect=pygame.Rect(0,0,100,100)
#xcv

    
    windowSurface.fill(BACKGROUNDCOLOR)
    guy1rectleft=pygame.Rect(0, 0, 100, 150)
    guy1rectright=pygame.Rect((WINDOWWIDTH-200), (WINDOWHEIGHT-200), 100, 150)
    guy1imageint=pygame.image.load('guy1.png')
    guy1image=pygame.transform.scale(guy1imageint, (200,200))
    
    girl1rectleft=pygame.Rect(0, 0, 100, 150)
    girl1rectright=pygame.Rect((WINDOWWIDTH-200), (WINDOWHEIGHT-200), 100, 150)
    girl1imageint=pygame.image.load('girl1.png')
    girl1image=pygame.transform.scale(girl1imageint, (200,200))
    
    girl2rectleft=pygame.Rect(0, 200, 100, 150)
    girl2rectright=pygame.Rect((WINDOWWIDTH-200), (WINDOWHEIGHT-200), 100, 150)
    girl2imageint=pygame.image.load('girl2.png')
    girl2image=pygame.transform.scale(girl2imageint, (200,200))
    
    girl3rectleft=pygame.Rect(0, 400, 100, 150)
    girl3rectright=pygame.Rect((WINDOWWIDTH-200), (WINDOWHEIGHT-200), 100, 150)
    girl3imageint=pygame.image.load('girl3.png')
    girl3image=pygame.transform.scale(girl3imageint, (200,200))

    windowSurface.blit(guy1image, guy1rectright)
    windowSurface.blit(girl1image, girl1rectleft)
    windowSurface.blit(girl2image, girl2rectleft)
    windowSurface.blit(girl3image, girl3rectleft)    

    
    drawTextmine('Who should I go see?', medfont, windowSurface,750, (WINDOWHEIGHT-60), BLUE)
    drawTextmine(' 1: Go see Lavine and help with shields', font, windowSurface,210, 100, LGREEN)
    drawTextmine(' 2: Go see Galil and help with engines', font, windowSurface,210, 300, RED)
    drawTextmine(' 3: Go see Niko and help with weapons', font, windowSurface,210, 500, PURP)       

    
    pygame.display.update()
    #waitForPlayerToPressKey()
    
    while exitvar==0:
        print(relationshippoints)
        print('rp points^')
        windowSurface.fill(BACKGROUNDCOLOR)
        event=pygame.event.wait()
        print ('relation while')
        if event.type==KEYDOWN:
            if relationshippoints==0:
                windowSurface.fill(BACKGROUNDCOLOR)                
                windowSurface.blit(guy1image, guy1rectright)
                drawTextmine('There isn\'t enough time before we De-Jump.  If we', font, windowSurface,100, 500, BLUE)
                drawTextmine('survive this next one, I\'ll try talking to her then.', font, windowSurface,100, 535, BLUE)                

                pygame.display.update()
                waitForPlayerToPressKey()
                exitvar=1            
                #pay attention to this, rp mgiht have to be changed based on debug xcv
                
            if keyPressed(K_1) and relationshippoints>=1 and girl1_level==girlslevel[0]:
                print ('lavine1')
                exitvar=1
                relationshippoints-=1
                talking.talklavine1()
                #xcvbn
                
                shieldmax=shieldmax+15
                
                playerRect=non_help_hitbox_reduction

                roundtimer=roundtimer-non_help_charge_reduction
                #roundtimer=roundtimer-non_help_charge_reduction
                
                rapid_fire_constant=rapid_fire_constant-non_help_laser_reduction

                
                windowSurface.fill(BACKGROUNDCOLOR)
                drawTextmine('Thank you for your help, we did great.', font, windowSurface, 220, 50, LGREEN)       
                drawTextmine('Shield Generators Tuned to Higher Output', font, windowSurface, 70, 230, LIGHTBLUE)                
                drawTextmine('Shields:  %s' % (shieldmax), font,windowSurface, 70, 300, LIGHTBLUE)
                drawTextmine(' (+15)', font,windowSurface, 280, 300, GREEN)                              
                drawTextmine('Ugh...this engine...', medfont, windowSurface, 130, 420, RED)
                drawTextmine('(Small engine boost)', smallfont, windowSurface, 130, 450, GREEN)                
                drawTextmine('I did what I could with this patheic ship\'s weapons', medfont, windowSurface, 130, 520, PURP)
                drawTextmine('(Small weapon boost)', smallfont, windowSurface, 130, 550, GREEN)                   
                windowSurface.blit(girl1image, happyrect)                

                #windowSurface.blit(smLAV, rectsmalllavine)
                windowSurface.blit(smGAL, rectsmallgalil)
                windowSurface.blit(smNIKO, rectsmallniko)  
                           
                girl1_level=girlslevel[1]

                pygame.display.update()
                waitForPlayerToPressKey()

            if keyPressed(K_1) and relationshippoints>=1 and girl1_level==girlslevel[1]:
                print ('lavine2')
                exitvar=1
                relationshippoints-=1
                talking.talklavine2()
                #xcv^
                windowSurface.fill(BACKGROUNDCOLOR)
                
                shieldmax=shieldmax+15
                
                playerRect=non_help_hitbox_reduction

                roundtimer=roundtimer-non_help_charge_reduction
                
                rapid_fire_constant=rapid_fire_constant-non_help_laser_reduction
                
                windowSurface.fill(BACKGROUNDCOLOR)
                drawTextmine('Si...Dax, thank you for helping...', font, windowSurface, 220, 50, LGREEN)       
                drawTextmine('Shields capacitors optimized', font, windowSurface, 70, 230, LIGHTBLUE)                
                drawTextmine('Shields:  %s' % (shieldmax), font,windowSurface, 70, 300, LIGHTBLUE)
                drawTextmine(' (+15)', font,windowSurface, 280, 300, GREEN)                              
                drawTextmine('I am getting a bit out of this engine!', medfont, windowSurface, 130, 420, RED)
                drawTextmine('(Small engine boost)', smallfont, windowSurface, 130, 450, GREEN)                
                drawTextmine('If I was only on a better ship with real weapons...', medfont, windowSurface, 130, 520, PURP)
                drawTextmine('(Small weapon boost)', smallfont, windowSurface, 130, 550, GREEN)                   
                windowSurface.blit(girl1image, happyrect) 
                windowSurface.blit(smGAL, rectsmallgalil)
                windowSurface.blit(smNIKO, rectsmallniko)  

                
                girl1_level=girlslevel[2]
                pygame.display.update()
                waitForPlayerToPressKey()

            if keyPressed(K_1) and relationshippoints>=1 and girl1_level==girlslevel[2]:
                print ('lavine3')
                exitvar=1
                relationshippoints-=1
                talking.talklavine3()
                #xcv^                
                windowSurface.fill(BACKGROUNDCOLOR)
                
                shieldmax=shieldmax+20
                playerRect=non_help_hitbox_reduction

                roundtimer=roundtimer-non_help_charge_reduction
                rapid_fire_constant=rapid_fire_constant-non_help_laser_reduction
                
                windowSurface.fill(BACKGROUNDCOLOR)
                drawTextmine('Dax, if we live through this I want to be with you.', font, windowSurface, 220, 50, LGREEN)       
                drawTextmine('Shields overdriven', font, windowSurface, 70, 230, LIGHTBLUE)                
                drawTextmine('Shields:  %s' % (shieldmax), font,windowSurface, 70, 300, LIGHTBLUE)
                drawTextmine(' (+20)', font,windowSurface, 280, 300, GREEN)                              
                drawTextmine('Little by little!', medfont, windowSurface, 130, 420, RED)
                drawTextmine('(Small engine boost)', smallfont, windowSurface, 130, 450, GREEN)                
                drawTextmine('Good thing I am smart.', medfont, windowSurface, 130, 520, PURP)
                drawTextmine('(Small weapon boost)', smallfont, windowSurface, 130, 550, GREEN)                   
                windowSurface.blit(girl1image, happyrect) 
                windowSurface.blit(smGAL, rectsmallgalil)
                windowSurface.blit(smNIKO, rectsmallniko)  

                
                girl1_level=girlslevel[3]
                pygame.display.update()
                waitForPlayerToPressKey()

                 

            if keyPressed(K_2) and relationshippoints>=1 and girl2_level==girlslevel[0]:
                print ('galil1')
                exitvar=1
                relationshippoints-=1
                talking.talkgalil1()
                #xcv^
                windowSurface.fill(BACKGROUNDCOLOR)

                              
                girl2_level=girlslevel[1]
                
                playerRect=playerRect.inflate(-4,-1)

                roundtimer=roundtimer-galilreduce
                PLAYERMOVERATE=PLAYERMOVERATE+1 

                shieldmax=shieldmax+non_help_shield_increase
             
                rapid_fire_constant=rapid_fire_constant-non_help_laser_reduction
                
                windowSurface.fill(BACKGROUNDCOLOR)
                drawTextmine('Thanks Dax!!!', font, windowSurface, 220, 50, RED)       
                drawTextmine('Engines converted to combat mode', font, windowSurface, 70, 230, LIGHTBLUE)                
                drawTextmine('Engines:', font,windowSurface, 70, 300, LIGHTBLUE)
                drawTextmine(' (Multiple Bonuses)', font,windowSurface, 280, 300, GREEN)                              
                drawTextmine('Sir, I got an increase in the shields.', medfont, windowSurface, 130, 420, LGREEN)
                drawTextmine('(Small shield boost)', smallfont, windowSurface, 130, 450, GREEN)                
                drawTextmine('Our lasers are better, just don\'t look at what I did.', medfont, windowSurface, 130, 520, PURP)
                drawTextmine('(Small weapon boost)', smallfont, windowSurface, 130, 550, GREEN)                   
                windowSurface.blit(girl2image, happyrect)                
                windowSurface.blit(smLAV, rectsmalllavine)
                #windowSurface.blit(smGAL, rectsmallgalil)
                windowSurface.blit(smNIKO, rectsmallniko)  
                pygame.display.update()
                waitForPlayerToPressKey()



              
                pygame.display.update()
                waitForPlayerToPressKey()

                

            if keyPressed(K_2) and relationshippoints>=1 and girl2_level==girlslevel[1]:
                print ('galil2')
                exitvar=1
                relationshippoints-=1
                talking.talkgalil2()
                #xcv^
                windowSurface.fill(BACKGROUNDCOLOR)

                              
                girl2_level=girlslevel[2]
                
                playerRect=playerRect.inflate(-4,-1)

                roundtimer=roundtimer-galilreduce
                PLAYERMOVERATE=PLAYERMOVERATE+1 

                shieldmax=shieldmax+non_help_shield_increase
             
                rapid_fire_constant=rapid_fire_constant-non_help_laser_reduction
                
                windowSurface.fill(BACKGROUNDCOLOR)
                drawTextmine('Awesome Dax, no one will be able to touch us now!', font, windowSurface, 220, 50, RED)
                
                drawTextmine('Engines Power Routing Optimized', font, windowSurface, 70, 230, LIGHTBLUE)                
                drawTextmine('Engines:', font,windowSurface, 70, 300, LIGHTBLUE)
                drawTextmine(' (Multiple Bonuses)', font,windowSurface, 280, 300, GREEN)                              
                drawTextmine('Reporting a shield increase, Sir.', medfont, windowSurface, 130, 420, LGREEN)
                drawTextmine('(Small shield boost)', smallfont, windowSurface, 130, 450, GREEN)                
                drawTextmine('Heh, damn am I good.', medfont, windowSurface, 130, 520, PURP)
                drawTextmine('(Small weapon boost)', smallfont, windowSurface, 130, 550, GREEN)                   
                windowSurface.blit(girl2image, happyrect)                

                windowSurface.blit(smLAV, rectsmalllavine)
                #windowSurface.blit(smGAL, rectsmallgalil)
                windowSurface.blit(smNIKO, rectsmallniko)              
                pygame.display.update()
                waitForPlayerToPressKey()



            if keyPressed(K_2) and relationshippoints>=1 and girl2_level==girlslevel[2]:
                print ('galil3')
                exitvar=1
                relationshippoints-=1
                talking.talkgalil3()
                #xcv^
                windowSurface.fill(BACKGROUNDCOLOR)

                              
                girl2_level=girlslevel[3]
                
                playerRect=playerRect.inflate(-4,-2)

                roundtimer=roundtimer-galilreduce
                PLAYERMOVERATE=PLAYERMOVERATE+1 

                shieldmax=shieldmax+non_help_shield_increase
             
                rapid_fire_constant=rapid_fire_constant-non_help_laser_reduction
                
                windowSurface.fill(BACKGROUNDCOLOR)
                drawTextmine('Dax I want to stay with you forever!  ', font, windowSurface, 220, 50, RED)
                drawTextmine('Nothing will come between us!', font, windowSurface, 220, 90, RED)                    
                drawTextmine('Combat Engine Mode Achieved', font, windowSurface, 70, 230, LIGHTBLUE)                
                drawTextmine('Engines:', font,windowSurface, 70, 300, LIGHTBLUE)
                drawTextmine(' (Multiple Bonuses)', font,windowSurface, 280, 300, GREEN)                              
                drawTextmine('Got a bit more out of the shields Sir.', medfont, windowSurface, 130, 420, LGREEN)
                drawTextmine('(Small shield boost)', smallfont, windowSurface, 130, 450, GREEN)                
                drawTextmine('There is a lot more where that came from!', medfont, windowSurface, 130, 520, PURP)
                drawTextmine('(Small weapon boost)', smallfont, windowSurface, 130, 550, GREEN)                   
                windowSurface.blit(girl2image, happyrect)                

                windowSurface.blit(smLAV, rectsmalllavine)
                #windowSurface.blit(smGAL, rectsmallgalil)
                windowSurface.blit(smNIKO, rectsmallniko)              
                pygame.display.update()
                waitForPlayerToPressKey()

                

            if keyPressed(K_3) and relationshippoints>=1 and girl3_level==girlslevel[0]:
                print ('niko')
                exitvar=1
                relationshippoints-=1
                talking.talkniko1()



                shieldmax=shieldmax+non_help_shield_increase
                
                playerRect=non_help_hitbox_reduction

                roundtimer=roundtimer-non_help_charge_reduction
                
                rapid_fire_constant=rapid_fire_constant-1.7
                
                windowSurface.fill(BACKGROUNDCOLOR)
                drawTextmine('You helped...a bit.', font, windowSurface, 220, 50, PURP)       
                drawTextmine('Weapon systems routed sucessfully', font, windowSurface, 70, 230, LIGHTBLUE)                
                drawTextmine('Weapon cooldown:  %s' % (rapid_fire_constant), font,windowSurface, 70, 300, LIGHTBLUE)
                drawTextmine(' (-1.7)', font,windowSurface, 480, 300, GREEN)

                drawTextmine('I eeked a bit out of the shields Sir.', medfont, windowSurface, 130, 420, LGREEN)
                drawTextmine('(Small shield boost)', smallfont, windowSurface, 130, 450, GREEN)
                
                drawTextmine('This engine is so archaic...', medfont, windowSurface, 130, 520, RED)
                drawTextmine('(Small engine boost)', smallfont, windowSurface, 130, 550, GREEN)                
                 
                windowSurface.blit(girl3image, happyrect)                
                windowSurface.blit(smLAV, rectsmalllavine)
                windowSurface.blit(smGAL, rectsmallniko)
  
           
                girl3_level=girlslevel[1]         
                pygame.display.update()
                waitForPlayerToPressKey()                


            if keyPressed(K_3) and relationshippoints>=1 and girl3_level==girlslevel[1]:
                print ('niko2')
                exitvar=1
                relationshippoints-=1
                talking.talkniko2()



                shieldmax=shieldmax+non_help_shield_increase
                
                playerRect=non_help_hitbox_reduction

                roundtimer=roundtimer-non_help_charge_reduction
                
                rapid_fire_constant=rapid_fire_constant-1.7  
                
                windowSurface.fill(BACKGROUNDCOLOR)
                drawTextmine('Dax...Thanks.', font, windowSurface, 220, 50, PURP)       
                drawTextmine('Laser batteries hypercooled', font, windowSurface, 70, 230, LIGHTBLUE)                
                drawTextmine('Weapon cooldown:  %s' % (rapid_fire_constant), font,windowSurface, 70, 300, LIGHTBLUE)
                drawTextmine(' (-1.7)', font,windowSurface, 480, 300, GREEN)

                drawTextmine('Sir, I am detecting a small shield improvement.', medfont, windowSurface, 130, 420, LGREEN)
                drawTextmine('(Small shield boost)', smallfont, windowSurface, 130, 450, GREEN)
                
                drawTextmine('I got something Dax!', medfont, windowSurface, 130, 520, RED)
                drawTextmine('(Small engine boost)', smallfont, windowSurface, 130, 550, GREEN)                
                 
                windowSurface.blit(girl3image, happyrect)                
                windowSurface.blit(smLAV, rectsmalllavine)
                windowSurface.blit(smGAL, rectsmallniko)
  
           
                girl3_level=girlslevel[2]         
                pygame.display.update()
                waitForPlayerToPressKey()  




            if keyPressed(K_3) and relationshippoints>=1 and girl3_level==girlslevel[2]:
                print ('niko3')
                exitvar=1
                relationshippoints-=1
                talking.talkniko3()



                shieldmax=shieldmax+non_help_shield_increase
                
                playerRect=non_help_hitbox_reduction

                roundtimer=roundtimer-non_help_charge_reduction
                
                rapid_fire_constant=rapid_fire_constant-1.7  
                
                windowSurface.fill(BACKGROUNDCOLOR)
                drawTextmine('I am glad I could be open with you.', font, windowSurface, 220, 50, PURP)       
                drawTextmine('Weapon Systems overdrive', font, windowSurface, 70, 230, LIGHTBLUE)                
                drawTextmine('Weapon cooldown:  %s' % (rapid_fire_constant), font,windowSurface, 70, 300, LIGHTBLUE)
                drawTextmine(' (-1.7)', font,windowSurface, 480, 300, GREEN)

                drawTextmine('Sir I was able to fix the shields further.', medfont, windowSurface, 130, 420, LGREEN)
                drawTextmine('(Small shield boost)', smallfont, windowSurface, 130, 450, GREEN)
                
                drawTextmine('Dax, I improved the engines!', medfont, windowSurface, 130, 520, RED)
                drawTextmine('(Small engine boost)', smallfont, windowSurface, 130, 550, GREEN)                
                 
                windowSurface.blit(girl3image, happyrect)                
                windowSurface.blit(smLAV, rectsmalllavine)
                windowSurface.blit(smGAL, rectsmallniko)
  
           
                girl3_level=girlslevel[3]         
                pygame.display.update()
                waitForPlayerToPressKey()  


                
            if keyPressed(K_ESCAPE):
                exitvar=1
                return
    print ('exited this')

def shipstats():
    global playerRect
    #player rect stuff
    z=playerRect.left
    y=playerRect.right
    t=abs(z-y)
    f=playerRect.top
    g=playerRect.bottom
    h=abs(f-g)
    hitbox=t*h
    #player rect stuff^
    hbreduction=abs(hitbox-300)
    laserreduction=abs(10-rapid_fire_constant)
    
    shieldincrease=shieldmax-15
    hullremain=hull-10
    movebonus=PLAYERMOVERATE-7
    windowSurface.fill(BACKGROUNDCOLOR)

    
    stat1rect=pygame.Rect(500, 0, 200, 200)
    stat1int=pygame.image.load('storyship1.png')
    statimage=pygame.transform.scale(stat1int, (700,250))    
    windowSurface.blit(statimage, stat1rect)

    guy1rectright=pygame.Rect((WINDOWWIDTH-200), (WINDOWHEIGHT-200), 100, 150)
    guy1imageint=pygame.image.load('guy1.png')
    guy1image=pygame.transform.scale(guy1imageint, (200,200))
    windowSurface.blit(guy1image, guy1rectright)
    drawTextmine('...', font, windowSurface, 900, 500, BLUE)
    
    pygame.display.update()
    drawTextmine('Radiant\'s Stats:', font, windowSurface, 10, 0, BLUE)    
    drawTextmine('Hull Remaining: %s' %(hull), font, windowSurface, 10, 50, WHITE)
    drawTextmine('(- %s)' % (hullremain), medfont,windowSurface, 350, 60, RED)
    
    drawTextmine('(Lavine)', smallfont,windowSurface, 50, 150, LGREEN)    
    drawTextmine('Max Shields: %s' % (shieldmax), font,windowSurface, 10, 160, LIGHTBLUE)
    drawTextmine('(+ %s)' % (shieldincrease), medfont,windowSurface, 350, 170, GREEN)

    drawTextmine('(Galil)', smallfont,windowSurface, 50, 290, RED)      
    drawTextmine('Bonus charge time on engines: %s' %(abs(introundtimer-roundtimer)), font, windowSurface, 10, 300, LIGHTBLUE)
    drawTextmine('(+ %s)' % (abs(introundtimer-roundtimer)), medfont,windowSurface, 600, 310, GREEN)     
    drawTextmine('Move rate: %s' %(PLAYERMOVERATE), font, windowSurface, 10, 355, LIGHTBLUE)
    drawTextmine('(+ %s)' % (movebonus), medfont,windowSurface, 600, 365, GREEN)
    drawTextmine('Hitbox: %s' %(hitbox), font, windowSurface, 10, 415, LIGHTBLUE)
    drawTextmine('(-  %s)' % (hbreduction), medfont,windowSurface, 600, 425, GREEN)

    drawTextmine('(Niko)', smallfont,windowSurface, 50, 520, PURP)     
    drawTextmine('Laser Cooldown: %s' %(rapid_fire_constant), font, windowSurface, 10, 530, LIGHTBLUE)
    drawTextmine('(- %s)' % (laserreduction), medfont,windowSurface, 350, 540, GREEN)     



    
    pygame.display.update()    
    waitForPlayerToPressKey()  
    
    
    ###
def hypermainloop():
    hypercontinue=True #wheter game is over
    choicemade=0
    continuex=0
    continuepostconvo=0
    global beatlevel
    global hull
    global shields
    global ADDNEWBADDIERATE
    global BULLETTHRESHOLD
    global shieldmax
    global beatlevel
    global girl1_level
    global girl2_level
    global girl3_level
    global relationshippoints
    global roundtimer
    global megacrush
    global rapid_fire_constant
    global roundreduction

    guy1rectleft=pygame.Rect(0, 0, 100, 150)
    guy1imageint=pygame.image.load('guy1.png')
    guy1image=pygame.transform.scale(guy1imageint, (200,200))
    
    girl1rectleft=pygame.Rect(0, 400, 100, 150)
    girl1imageint=pygame.image.load('girl1.png')
    girl1image=pygame.transform.scale(girl1imageint, (200,200))

    girl2rectleft=pygame.Rect(400, 400, 100, 150)
    girl2imageint=pygame.image.load('girl2.png')
    girl2image=pygame.transform.scale(girl2imageint, (200,200))

    girl3rectleft=pygame.Rect(800, 400, 100, 150)
    girl3imageint=pygame.image.load('girl3.png')
    girl3image=pygame.transform.scale(girl3imageint, (200,200))
    
    while hypercontinue==True:

            
        for event in pygame.event.get():
            print (beatlevel)
            print ('beatlevel')
            shields=shieldmax

            if beatlevel==0:
               
                talking.talking1()
            print (rapid_fire_constant)
            print (roundreduction)
            
            main()
            
            
            if beatlevel==1:
               
                talking.talkingpost1()
                
            if beatlevel==2:
               
                talking.talkingpost2()
                
            if beatlevel==3:
               
                talking.talkingpost3()
                
            if beatlevel==4:
               
                talking.talkingpost4()                       
            print(beatlevel)
            if beatlevel==5:
               
                talking.talkingpost5()
                if girl1_level==girlslevel[3]:
                    print ('lav end')
                    talking.talklavineend()
                if girl2_level==girlslevel[3]:
                    print ('gal end')
                    talking.talkgalilend()
                if girl3_level==girlslevel[3]:
                    print ('niko end')
                    talking.talknikoend()


                
            menumusic.play()            
           
            windowSurface.fill(BACKGROUNDCOLOR)

            continuex=0
            
            #this is game over loop
            while beatlevel==0:
                windowSurface.fill(BACKGROUNDCOLOR)
                drawText('Press "y" to try again', font, windowSurface, (WINDOWWIDTH/3)-80, (WINDOWHEIGHT/3)+50)
                pygame.display.update()
                event=pygame.event.wait()
                if event.type==KEYDOWN:
                    if keyPressed(ord('y')):
                        megacrush=5
                        shields=10
                        hull=10
                        relationshippoints=0
                        girl1_level=girlslevel[0]
                        girl2_level=girlslevel[0]
                        girl3_level=girlslevel[0]
                        menumusic.stop()
                        roundtimer=30
                        rapid_fire_constant=10
                        PLAYERMOVERATE=7
                        playerRect=pygame.Rect(0,0,30,10)
                        main()
                    if keyPressed(K_ESCAPE):
                        terminate()

                
            windowSurface.fill(BACKGROUNDCOLOR)           
            pygame.display.update()

            if beatlevel==5:
                continuex=1
                print ('end bonus story')
                #xcv end sotry here and if statement
            while continuex==0:
                event=pygame.event.wait()
                windowSurface.fill(BACKGROUNDCOLOR)


                drawTextmine('1: Go talk to and help someone on the crew', medfont, windowSurface, 220, 50, WHITE)
                drawTextmine('2: Check ship stats', medfont, windowSurface, 220, 100, LIGHTBLUE)                
                drawTextmine('3: Finished, and ready to continue escape', medfont, windowSurface, 220, 150, BLUE)


                drawTextmine('-Lavine', smallfont, windowSurface, 210, 580, LGREEN)
                drawTextmine('%s' %(girl1_level), font, windowSurface, 230, 475, LGREEN)
                
                drawTextmine('-Galil', smallfont, windowSurface, 610, 580, RED)
                drawTextmine('%s' %(girl2_level), font, windowSurface, 630, 475, RED)
                


                drawTextmine('-Niko', smallfont, windowSurface, 1010, 580, PURP)
                drawTextmine('%s' %(girl3_level), font, windowSurface, 1030, 475, PURP)
                
                drawTextmine('Crew\'s Morale:', font, windowSurface, 450, 360, LIGHTBLUE)            
                pygame.draw.lines(windowSurface, BLUE, False, [(0,395), (WINDOWWIDTH,395)], 5)
                windowSurface.blit(guy1image, guy1rectleft)                
                windowSurface.blit(girl1image, girl1rectleft)
                windowSurface.blit(girl2image, girl2rectleft)
                windowSurface.blit(girl3image, girl3rectleft)
                pygame.display.update()

                
                if event.type==KEYDOWN:
                    if keyPressed(K_ESCAPE):
                        terminate()                    
                    if keyPressed(K_1):
                        print('convo')
                        crewrelationship()
                    if keyPressed(K_2):
                        print('ship')
                        shipstats()                        
                    if keyPressed(K_3):
                        continuex=1
                        print ('changed x')
                        menumusic.stop()
                        if relationshippoints>0:
                            relationshippoints=0
                        
            if beatlevel==1:
                ADDNEWBADDIERATE=ADDNEWBADDIERATE-1
                BULLETTHRESHOLD=BULLETTHRESHOLD-10
                #roundtimer=roundtimer+2
            if beatlevel==2:
                ADDNEWBADDIERATE=ADDNEWBADDIERATE-1
                BULLETTHRESHOLD=BULLETTHRESHOLD-10
                #roundtimer=roundtimer+2                
            if beatlevel==3:
                ADDNEWBADDIERATE=ADDNEWBADDIERATE-1
                BULLETTHRESHOLD=BULLETTHRESHOLD-10
                #roundtimer=roundtimer+2                
            if beatlevel==4:
                ADDNEWBADDIERATE=ADDNEWBADDIERATE-2
                BULLETTHRESHOLD=BULLETTHRESHOLD-10
                roundtimer=roundtimer+3                

#ADDNEWBADDIERATE=15#lower is more guys spawning # 15
#BULLETTHRESHOLD=80 #higher = slower #80
            
        if beatlevel==5:
            hypercontinue=False                        
            print('this is end of game')
            #terminate()
    print('got out here')
    #if beatlevel >1:
        #print('made it to next level')
    terminate()


    
hypermainloop()


                                      
