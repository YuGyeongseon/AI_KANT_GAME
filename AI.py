# AI_KANT_GAME
import pygame
import time
import sys


pygame.init()

white = (255, 255, 255)

gameNameImg = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-171845~2.png")
mainBackgroundImg = pygame.image.load("/storage/emulated/0/Download/NAVER MYBOX/다운로드 파일_20220717170103~2.png")
startImg= pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-172145~2.png")
quitImg =pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-172538~2.png")

act1BackgroundImg = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-173914.png")
act1Point1Img =pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-173914~4.png")
act1Point1ClickImg =pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-174123~4.png")
act1Point2Img =pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-173914~3.png")
act1Point2ClickImg =pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-174123~3.png")
act1Point3Img =pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-173914~5.png")
act1Point3ClickImg =pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-174123~5.png")

act2BackgroundImg = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-185633.png")
act2Point1Img = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-185633~2.png")
act2Point1ClickImg = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-185650~2.png")
act2Point2Img = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-185633~3.png")
act2Point2ClickImg = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-185650~3.png")

act3BackgroundImg = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-193707.png")
act3Point1Img = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-193707~2.png")
act3Point1ClickImg = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-193723~2.png")
act3Point2Img = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-193707~3.png")
act3Point2ClickImg = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-193723~3.png")

returnImg = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-180425~2.png")

end1Img = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-201546.png")

end2Img = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-202110.png")

wasteImg = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-180425.png")

errorImg = pygame.image.load("/storage/emulated/0/Pictures/Screenshots/Screenshot_20220717-184059.png")




display_width = 5000
display_height = 3000
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("AI_KANT_GAME")

clock = pygame.time.Clock()



class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(0.2)
                action()
        else:
            gameDisplay.blit(img_in,(x,y))

def quitgame():
    pygame.quit()
    sys.exit()


def mainPage():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        
        backgroundImg= gameDisplay.blit(mainBackgroundImg , (220,300))
        titleName= gameDisplay.blit(gameNameImg  , (500,40))
        startButton = Button(startImg,1400,400,500,200,startImg,1400,400,act1Page)
        quitButton = Button(quitImg,1420,700,500,200,quitImg,1420,700,quitgame)
        pygame.display.update()
        clock.tick(15)

def act1Page():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        
        backgroundImg= gameDisplay.blit(act1BackgroundImg , (0,0))
        point1Button = Button(act1Point1Img,560,570,700,100,act1Point1ClickImg,560,570,act2Page)
        point2Button = Button(act1Point2Img,270,700,2000,100,act1Point2ClickImg,270,700,wastePage)
        point3Button = Button(act1Point3Img,480,820,1000,100,act1Point3ClickImg,480,820,errorPage)
        pygame.display.update()
        clock.tick(15)

def errorPage():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
        gameDisplay.fill(white)
        
        backgroundImg= gameDisplay.blit(errorImg , (0,0))
        returnButton = Button(returnImg,1410,890,700,300,returnImg,1410,890,mainPage)
        pygame.display.update()
        clock.tick(15)
 
def wastePage():

   menu = True

   while menu:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

       gameDisplay.fill(white)
       backgroundImg= gameDisplay.blit(wasteImg , (0,0))
       returnButton = Button(returnImg,1410,890,700,300,returnImg,1410,890,mainPage)
       
       pygame.display.update()
       clock.tick(15)
        
def end1Page():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        backgroundImg= gameDisplay.blit(end1Img , (0,0))
        returnButton = Button(returnImg,1410,890,700,300,returnImg,1410,890,mainPage)
      
        pygame.display.update()
        clock.tick(15)
        
def act2Page():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        backgroundImg= gameDisplay.blit(act2BackgroundImg , (0,0))
        Act2point1Button = Button(act2Point1Img,320,550,700,100,act2Point1ClickImg,320,550,errorPage)
        Act2point2Button = Button(act2Point2Img,320,700,700,100,act2Point2ClickImg,340,700,act3Page)
        pygame.display.update()
        clock.tick(15)

def act3Page():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        backgroundImg= gameDisplay.blit(act3BackgroundImg , (0,0))
        Act3point1Button = Button(act3Point1Img,320,370,500,100,act3Point1ClickImg,320,370,end1Page)
        Act3point2Button = Button(act3Point2Img,320,540,630,100,act3Point2ClickImg,320,540,end2Page)
        
        pygame.display.update()
        clock.tick(15)

def end2Page():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        backgroundImg= gameDisplay.blit(end2Img , (0,0))
        returnButton = Button(returnImg,1410,890,700,300,returnImg,1410,890,mainPage)
        
        pygame.display.update()
        clock.tick(15)
mainPage()
