import math
import sys, pygame, pygame.mixer
from pygame.locals import *
pygame.init()

sound = pygame.mixer.Sound(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Sounds\start1.wav')
sound.play()

#setting the screen size
size = width, heigh = 1500, 900
screen = pygame.display.set_mode(size)
#background image
background = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\background.jpg')
screen.blit(background, (100,90))
pygame.display.flip()
#Instructions
instructionspng = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\Instructions.png')
instructionspng = pygame.transform.scale(instructionspng,(450,775))
screen.blit(instructionspng, (1030.5,235.5))
#Title
titlepng = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\Title.png')
screen.blit(titlepng, (1, 770))
pygame.display.flip()

#poolballs
whiteball = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\whiteball.png')
ball1 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball1.png')
ball2 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball2.png')
ball3 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball3.png')
ball4 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball4.png')
ball5 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball5.png')
ball6 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball6.png')
ball7 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball7.png')
ball8 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball8.png')
ball9 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball9.png')
ball10 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball10.png')
ball11 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball11.png')
ball12 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball12.png')
ball13 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball13.png')
ball14 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball14.png')
ball15 = pygame.image.load(r'C:\Users\avramp\Documents\BU\Spring 2020\AI\PoolTableHelp\Resources\Images\ball15.png')
whiteball = pygame.transform.scale(whiteball,(25,25))
ball1 = pygame.transform.scale(ball1,(25,25))
ball2 = pygame.transform.scale(ball2,(25,25))
ball3 = pygame.transform.scale(ball3,(25,25))
ball4 = pygame.transform.scale(ball4,(25,25))
ball5 = pygame.transform.scale(ball5,(25,25))
ball6 = pygame.transform.scale(ball6,(25,25))
ball7 = pygame.transform.scale(ball7,(25,25))
ball8 = pygame.transform.scale(ball8,(25,25))
ball9 = pygame.transform.scale(ball9,(25,25))
ball10 = pygame.transform.scale(ball10,(25,25))
ball11 = pygame.transform.scale(ball11,(25,25))
ball12 = pygame.transform.scale(ball12,(25,25))
ball13 = pygame.transform.scale(ball13,(25,25))
ball14 = pygame.transform.scale(ball14,(25,25))
ball15 = pygame.transform.scale(ball15,(25,25))

#TextField / Return Field
textWIDTH = 567
textHEIGHT = 115
#RGB Values
white = (255, 255, 255)
gray = (128, 128, 128)
darkgray = (169, 169, 169)
lightgray = (211, 211, 211)

font = pygame.font.SysFont("Times New Roman, Arial", 12)
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont("Times New Roman, Arial", 12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((653.5),(594))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
def message_display2(text):
    largeText = pygame.font.SysFont("Times New Roman, Arial", 12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((653.5),(618))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
def message_display3(text):
    largeText = pygame.font.SysFont("Times New Roman, Arial", 12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((653.5),(630))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
def message_display4(text):
    largeText = pygame.font.SysFont("Times New Roman, Arial", 12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((653.5),(642))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
def message_display5(text):
    largeText = pygame.font.SysFont("Times New Roman, Arial", 12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((653.5),(654))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
def message_display6(text):
    largeText = pygame.font.SysFont("Times New Roman, Arial", 12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((653.5),(666))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
def message_display7(text):
    largeText = pygame.font.SysFont("Times New Roman, Arial", 12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((653.5),(678))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
def message_display9(text):
    largeText = pygame.font.SysFont("Times New Roman, Arial", 12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((653.5),(690))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
def message_display8(text):
    largeText = pygame.font.SysFont("Times New Roman, Arial", 12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((653.5),(702))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()


#Classes work
class button():
    def __init__(self, color, x,y,width,height, text='', action=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    
    def isClicked():
        click = pygame.mouse.get_pressed()
        if click[0] == 1 and action !=None:
            if action == "oneBallMove":
                mx,my = pygame.mouse.get_pos()
                #screen.fill(pygame.Color("black"))
                #screen.blit(background, (100,90))
                #screen.blit(whiteball, (mx-12.5,my-12.5))
                #pygame.display.flip()
                screen.blit(ball1, (mx-12.5,my-12.5))
                b1 = Poolball("oneBall", ball1, mx-12.5, my-12.5)
                pygame.display.flip()
                print(b1.name)
                print(b1.xcoordinate)
                print(b1.ycoordinate)                
                
        

def redrawWindow():
    oneButton.draw(screen)
    
class pockets:
    def __init__(self, pocketName, xcoordinate, ycoordinate):
        self.pocketName = pocketName
        self.xcoordinate = xcoordinate
        self.ycoordinate = ycoordinate
        
topLeft = pockets("topLeft", 131.5, 112.5)
topCenter = pockets("topCenter", 547.5, 112.5)
topRight = pockets("topRight", 968, 112.5)
bottomLeft = pockets("bottomLeft", 131.5, 528.5)
bottomCenter = pockets("bottomCenter", 547.5, 528.5)
bottomRight = pockets("bottomRight", 968, 528.5)


class ballsBeenPocketed:
    def __init__(self, name, pocket, difficulty):
        self.name = name
        self.pocket = pocket
        self.difficulty = difficulty


class Poolball:
    
    def __init__(self, name, image, xcoordinate, ycoordinate):
        self.name = name
        self.image = image
        self.xcoordinate = xcoordinate
        self.ycoordinate = ycoordinate

b0 = Poolball("whiteBall", whiteball, 1050,100)        
b1 = Poolball("oneBall", ball1, 1075, 100)
b2 = Poolball("twoBall", ball2, 1100,100)
b3 = Poolball("threeBall", ball3, 1125,100)
b4 = Poolball("fourBall", ball4, 1150,100)
b5 = Poolball("fiveBall", ball5, 1175,100)
b6 = Poolball("sixBall", ball6, 1200,100)
b7 = Poolball("sevenBall", ball7, 1050,125)
b8 = Poolball("eightBall", ball8, 1075,125)
b9 = Poolball("nineBall", ball9, 1100,125)
b10 = Poolball("tenBall", ball10, 1125,125)
b11 = Poolball("elevenBall", ball11, 1150,125)
b12 = Poolball("twelveBall", ball12, 1175,125)
b13 = Poolball("thirteenBall", ball13, 1200,125)
b14 = Poolball("fourteenBall", ball14, 1050,150)
b15 = Poolball("fifteenBall", ball15, 1075,150)


screen.blit(whiteball, (1050,100))
screen.blit(ball1, (1075,100))
screen.blit(ball2, (1100,100))
screen.blit(ball3, (1125,100))
screen.blit(ball4, (1150,100))
screen.blit(ball5, (1175,100))
screen.blit(ball6, (1200,100))
screen.blit(ball7, (1050,125))
screen.blit(ball8, (1075,125))
screen.blit(ball9, (1100,125))
screen.blit(ball10, (1125,125))
screen.blit(ball11, (1150,125))
screen.blit(ball12, (1175,125))
screen.blit(ball13, (1200,125))
screen.blit(ball14, (1050,150))
screen.blit(ball15, (1075,150))
pygame.display.flip()

#definitions
def solidsSearch():
    print ("")
    print("***********")
    print("Solids Search Test")
    print("***********")
    print("")
    print("")    
    startx = b0.xcoordinate 
    starty = b0.ycoordinate
    ballsOnTableWrk = ballsOnTable.copy()
    moveOnToNextBall = None
    checkWithPockets = None
    ballPathOpen = []
    for index, x in enumerate(solids):
        if 131.5<x.xcoordinate<968 and 112.5<x.ycoordinate<528.5:
            print(x.name + "[][][][][][][][][][][][][]")
            curx = x.xcoordinate
            cury = x.ycoordinate
            for index, obj in enumerate(ballsOnTableWrk):
                if obj == None:
                    continue
                else:
                    if obj.xcoordinate == curx:
                        ballsOnTableWrk[index] = None
                        print("Balls on table list")
                        print(ballsOnTableWrk)
                        continue              
                    else:
                        print (obj.name)
                        if 131.5<obj.xcoordinate<968 and 112.5<obj.ycoordinate<528.5:
                            p1 = Point(startx, starty) 
                            q1 = Point(curx, cury) 
                            p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                            q2 = Point(obj.xcoordinate, obj.ycoordinate+12.5) 
                            
                            intersect = []
                            doesIntersect = None
                            
                            distance1 = math.sqrt( (curx - startx)**2 + (cury - starty)**2 )
                            
                            if doIntersect(p1, q1, p2, q2): 
                                intersect.append("yes")
                            else: 
                                intersect.append("no")
                            
                            p1 = Point(startx, starty) 
                            q1 = Point(curx, cury) 
                            p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                            q2 = Point(obj.xcoordinate+12.5, obj.ycoordinate) 
                            
                            if doIntersect(p1, q1, p2, q2): 
                                intersect.append("yes")
                            else: 
                                intersect.append("no")
                            
                            p1 = Point(startx, starty) 
                            q1 = Point(curx, cury) 
                            p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                            q2 = Point(obj.xcoordinate-12.5, obj.ycoordinate) 
                            
                            if doIntersect(p1, q1, p2, q2): 
                                intersect.append("yes")
                            else: 
                                intersect.append("no")
                                
                            p1 = Point(startx, starty) 
                            q1 = Point(curx, cury) 
                            p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                            q2 = Point(obj.xcoordinate, obj.ycoordinate-12.5) 
                            
                            if doIntersect(p1, q1, p2, q2): 
                                intersect.append("yes")
                            else: 
                                intersect.append("no") 
                                
                            if "yes" in intersect:
                                doesIntersect = True    
                            else:
                                doesIntersect = False
                            
                            intersect.clear
        
                            if doesIntersect == True:
                                #ballsOnTableWrk[index] = None
                                print(obj.name + " is intersecting the path")
                                ballPathOpen.append("no")
                                #moveOnToNextBall = True
                                #print(ballsOnTableWrk)
                                continue
                            else:
                                print(obj.name + " is not intersecting the path")
                                ballPathOpen.append("yes")
                                print("**********************************************************************************")
                        else:
                            ballsOnTable[index] = None
                            distance1 = 0
                            print(ballsOnTable)
                            continue
            if "no" in ballPathOpen:
                print("this ball cannot be pocketed")
                #solids.append(Poolball(x.name, x.image, x.xcoordinate, x.ycoordinate))
                ballPathOpen.clear()
                continue
            else:
                #try and pocket the ball?
                ballPathOpen.clear()
                print("time to try and pocket the ball")
                print(x.name)
                checkx = x.xcoordinate
                checky = x.ycoordinate
                blockedAtAll = []
                for y in pocketsList:
                    curpocketx = y.xcoordinate
                    curpockety = y.ycoordinate 
                    print("Pocket=" + y.pocketName)
                    print(ballsOnTable)
                    for index, obj in enumerate(ballsOnTable):                        
                        if obj == None: 
                            continue                      
                        else:
                            if obj.xcoordinate == checkx:
                                ballsOnTable[index] = None
                                #print("Balls on table list")
                                #print(ballsOnTable)
                                continue                           
                            else:
                                print (obj.name)
                                if 131.5<obj.xcoordinate<968 and 112.5<obj.ycoordinate<528.5:
                                    p1 = Point(checkx, checky) 
                                    q1 = Point(curpocketx, curpockety) 
                                    p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                                    q2 = Point(obj.xcoordinate, obj.ycoordinate+12.5) 
                                    
                                    distance2 = math.sqrt( (curpocketx - checkx)**2 + (curpockety - checky)**2 )
                                    #blockedAtAll = []
                                    intersect = []
                                    doesIntersect = None
                                    
                                    if doIntersect(p1, q1, p2, q2): 
                                        intersect.append("yes")
                                    else: 
                                        intersect.append("no")
                                    
                                    p1 = Point(checkx, checky) 
                                    q1 = Point(curpocketx, curpockety) 
                                    p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                                    q2 = Point(obj.xcoordinate+12.5, obj.ycoordinate) 
                                    
                                    if doIntersect(p1, q1, p2, q2): 
                                        intersect.append("yes")
                                    else: 
                                        intersect.append("no")
                                    
                                    p1 = Point(checkx, checky) 
                                    q1 = Point(curpocketx, curpockety) 
                                    p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                                    q2 = Point(obj.xcoordinate-12.5, obj.ycoordinate) 
                                    
                                    if doIntersect(p1, q1, p2, q2): 
                                        intersect.append("yes")
                                    else: 
                                        intersect.append("no")
                                        
                                    p1 = Point(checkx, checky) 
                                    q1 = Point(curpocketx, curpockety) 
                                    p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                                    q2 = Point(obj.xcoordinate, obj.ycoordinate-12.5) 
                                    
                                    if doIntersect(p1, q1, p2, q2): 
                                        intersect.append("yes")
                                    else: 
                                        intersect.append("no") 
                                        
                                        
                                    if "yes" in intersect:
                                        doesIntersect = True
                                    else:
                                        doesIntersect = False
                                    
                                    intersect.clear
                
                                    if doesIntersect == True:
                                        #ballsOnTable[index] = None
                                        #print("skip this")
                                        #print(ballsOnTable)
                                        blockedAtAll.append("no")
                                        distance1 = 999999999
                                        distance2 = 999999999
                                        print("pocket blocked")
                                        continue
                                    else:
                                        #print("Pocket Ball!")
                                        #ballsOnTable[index] = None
                                        #print(ballsOnTable)
                                        blockedAtAll.append("yes")
                                        print("pocket not blocked")
                                        #ballsInPocket.append(ballsBeenPocketed(x.name, y.pocketName, 1))
                                else:
                                    ballsOnTable[index] = None
                                    distance2 = 0
                                    #print(ballsOnTable)
                                    continue 
                    ballsInPocket.append(ballsBeenPocketed(x.name, y.pocketName, (distance1 + distance2))) 
                    distance1 = 0
                    distance2 = 0
                if "yes" in blockedAtAll:
                    startx = checkx
                    starty = checky
                    print(blockedAtAll)
                    blockedAtAll = []
                    print("ball pocketed")
                else:
                    print(blockedAtAll)
                    print("ball not pocketed!")
                    blockedAtAll = []
                print("**********************************************************************************")   
           
        else:
            break
    for obj in ballsInPocket:
        print(obj.name, obj.pocket, obj.difficulty)
    
    #check if first solid ball is in the coordinate range of the table
    #if yes:
        #check if there is another ball in the way
            #if yes:
                #skip ball and keep in array
            #if no:
                #get coordinate of ball and check pockets coordinates
                #check if there is a ball between ball coordinate and pocket
                #if yes:
                    #skip pocket, go to next pocket
                #if no:
                    #hit ball into pocket, check next pocket, add up the hypotenuse values for the total travel distance (difficulty rating)
                #if no more pockets:
                    #remove ball from array, move on to next ball, if all pockets are skipped (maybe make a skip counter so if counter == 6 aka all pockets
                    #were skipped then leave ball and go to next one (since it currently cannot be made)
                #if a shot is made
                    #you want to add the total difficulty rating and ball that was made into a new array. so at the end you have the order of each ball and the total diff
        #At the end of this entire loop. You will have checked to see wether a SINGLE BALL can be made into each of the 6 pockets... if it can, then you will have
        #made it in that pocket and calculated the difficulty to make that shot. If the ball cannot be made at all, then it will remain in the queue to get hit later. 

def stripesSearch():
    print ("")
    print("***********")
    print("Stripes Search Test")
    print("***********")
    print("")
    print("")    
    startx = b0.xcoordinate 
    starty = b0.ycoordinate
    ballsOnTableWrk = ballsOnTable.copy()
    moveOnToNextBall = None
    checkWithPockets = None
    ballPathOpen = []
    for index, x in enumerate(stripes):
        if 131.5<x.xcoordinate<968 and 112.5<x.ycoordinate<528.5:
            print(x.name + "[][][][][][][][][][][][][]")
            curx = x.xcoordinate
            cury = x.ycoordinate
            for index, obj in enumerate(ballsOnTableWrk):
                if obj == None:
                    continue
                else:
                    if obj.xcoordinate == curx:
                        ballsOnTableWrk[index] = None
                        print("Balls on table list")
                        print(ballsOnTableWrk)
                        continue              
                    else:
                        print (obj.name)
                        if 131.5<obj.xcoordinate<968 and 112.5<obj.ycoordinate<528.5:
                            p1 = Point(startx, starty) 
                            q1 = Point(curx, cury) 
                            p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                            q2 = Point(obj.xcoordinate, obj.ycoordinate+12.5) 
                            
                            intersect = []
                            doesIntersect = None
                            
                            distance1 = math.sqrt( (curx - startx)**2 + (cury - starty)**2 )
                            
                            if doIntersect(p1, q1, p2, q2): 
                                intersect.append("yes")
                            else: 
                                intersect.append("no")
                            
                            p1 = Point(startx, starty) 
                            q1 = Point(curx, cury) 
                            p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                            q2 = Point(obj.xcoordinate+12.5, obj.ycoordinate) 
                            
                            if doIntersect(p1, q1, p2, q2): 
                                intersect.append("yes")
                            else: 
                                intersect.append("no")
                            
                            p1 = Point(startx, starty) 
                            q1 = Point(curx, cury) 
                            p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                            q2 = Point(obj.xcoordinate-12.5, obj.ycoordinate) 
                            
                            if doIntersect(p1, q1, p2, q2): 
                                intersect.append("yes")
                            else: 
                                intersect.append("no")
                                
                            p1 = Point(startx, starty) 
                            q1 = Point(curx, cury) 
                            p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                            q2 = Point(obj.xcoordinate, obj.ycoordinate-12.5) 
                            
                            if doIntersect(p1, q1, p2, q2): 
                                intersect.append("yes")
                            else: 
                                intersect.append("no") 
                                
                            if "yes" in intersect:
                                doesIntersect = True    
                            else:
                                doesIntersect = False
                            
                            intersect.clear
        
                            if doesIntersect == True:
                                #ballsOnTableWrk[index] = None
                                print(obj.name + " is intersecting the path")
                                ballPathOpen.append("no")
                                #moveOnToNextBall = True
                                #print(ballsOnTableWrk)
                                continue
                            else:
                                print(obj.name + " is not intersecting the path")
                                ballPathOpen.append("yes")
                                print("**********************************************************************************")
                        else:
                            ballsOnTable[index] = None
                            distance1 = 0
                            print(ballsOnTable)
                            continue
            if "no" in ballPathOpen:
                print("this ball cannot be pocketed")
                #solids.append(Poolball(x.name, x.image, x.xcoordinate, x.ycoordinate))
                ballPathOpen.clear()
                continue
            else:
                #try and pocket the ball?
                ballPathOpen.clear()
                print("time to try and pocket the ball")
                print(x.name)
                checkx = x.xcoordinate
                checky = x.ycoordinate
                blockedAtAll = []
                for y in pocketsList:
                    curpocketx = y.xcoordinate
                    curpockety = y.ycoordinate 
                    print("Pocket=" + y.pocketName)
                    print(ballsOnTable)
                    for index, obj in enumerate(ballsOnTable):                        
                        if obj == None: 
                            continue                      
                        else:
                            if obj.xcoordinate == checkx:
                                ballsOnTable[index] = None
                                #print("Balls on table list")
                                #print(ballsOnTable)
                                continue                           
                            else:
                                print (obj.name)
                                if 131.5<obj.xcoordinate<968 and 112.5<obj.ycoordinate<528.5:
                                    p1 = Point(checkx, checky) 
                                    q1 = Point(curpocketx, curpockety) 
                                    p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                                    q2 = Point(obj.xcoordinate, obj.ycoordinate+12.5) 
                                    
                                    distance2 = math.sqrt( (curpocketx - checkx)**2 + (curpockety - checky)**2 )
                                    #blockedAtAll = []
                                    intersect = []
                                    doesIntersect = None
                                    
                                    if doIntersect(p1, q1, p2, q2): 
                                        intersect.append("yes")
                                    else: 
                                        intersect.append("no")
                                    
                                    p1 = Point(checkx, checky) 
                                    q1 = Point(curpocketx, curpockety) 
                                    p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                                    q2 = Point(obj.xcoordinate+12.5, obj.ycoordinate) 
                                    
                                    if doIntersect(p1, q1, p2, q2): 
                                        intersect.append("yes")
                                    else: 
                                        intersect.append("no")
                                    
                                    p1 = Point(checkx, checky) 
                                    q1 = Point(curpocketx, curpockety) 
                                    p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                                    q2 = Point(obj.xcoordinate-12.5, obj.ycoordinate) 
                                    
                                    if doIntersect(p1, q1, p2, q2): 
                                        intersect.append("yes")
                                    else: 
                                        intersect.append("no")
                                        
                                    p1 = Point(checkx, checky) 
                                    q1 = Point(curpocketx, curpockety) 
                                    p2 = Point(obj.xcoordinate, obj.ycoordinate) 
                                    q2 = Point(obj.xcoordinate, obj.ycoordinate-12.5) 
                                    
                                    if doIntersect(p1, q1, p2, q2): 
                                        intersect.append("yes")
                                    else: 
                                        intersect.append("no") 
                                        
                                        
                                    if "yes" in intersect:
                                        doesIntersect = True
                                    else:
                                        doesIntersect = False
                                    
                                    intersect.clear
                
                                    if doesIntersect == True:
                                        #ballsOnTable[index] = None
                                        #print("skip this")
                                        #print(ballsOnTable)
                                        blockedAtAll.append("no")
                                        distance1 = 999999999
                                        distance2 = 999999999
                                        print("pocket blocked")
                                        continue
                                    else:
                                        #print("Pocket Ball!")
                                        #ballsOnTable[index] = None
                                        #print(ballsOnTable)
                                        blockedAtAll.append("yes")
                                        print("pocket not blocked")
                                        #ballsInPocket.append(ballsBeenPocketed(x.name, y.pocketName, 1))
                                else:
                                    ballsOnTable[index] = None
                                    distance2 = 0
                                    #print(ballsOnTable)
                                    continue 
                    ballsInPocket.append(ballsBeenPocketed(x.name, y.pocketName, (distance1 + distance2))) 
                    distance1 = 0
                    distance2 = 0
                if "yes" in blockedAtAll:
                    startx = checkx
                    starty = checky
                    print(blockedAtAll)
                    blockedAtAll = []
                    print("ball pocketed")
                else:
                    print(blockedAtAll)
                    print("ball not pocketed!")
                    blockedAtAll = []
                print("**********************************************************************************")   
           
        else:
            break
    for obj in ballsInPocket:
        print(obj.name, obj.pocket, obj.difficulty)
    
    #check if first solid ball is in the coordinate range of the table
    #if yes:
        #check if there is another ball in the way
            #if yes:
                #skip ball and keep in array
            #if no:
                #get coordinate of ball and check pockets coordinates
                #check if there is a ball between ball coordinate and pocket
                #if yes:
                    #skip pocket, go to next pocket
                #if no:
                    #hit ball into pocket, check next pocket, add up the hypotenuse values for the total travel distance (difficulty rating)
                #if no more pockets:
                    #remove ball from array, move on to next ball, if all pockets are skipped (maybe make a skip counter so if counter == 6 aka all pockets
                    #were skipped then leave ball and go to next one (since it currently cannot be made)
                #if a shot is made
                    #you want to add the total difficulty rating and ball that was made into a new array. so at the end you have the order of each ball and the total diff
        #At the end of this entire loop. You will have checked to see wether a SINGLE BALL can be made into each of the 6 pockets... if it can, then you will have
        #made it in that pocket and calculated the difficulty to make that shot. If the ball cannot be made at all, then it will remain in the queue to get hit later. 
solids = []
def solidBallList():
    #solids = []
    solids.append(Poolball("oneBall", ball1, b1.xcoordinate, b1.ycoordinate))
    solids.append(Poolball("twoBall", ball2, b2.xcoordinate, b2.ycoordinate))
    solids.append(Poolball("threeBall", ball3, b3.xcoordinate, b3.ycoordinate))
    solids.append(Poolball("fourBall", ball4, b4.xcoordinate, b4.ycoordinate))
    solids.append(Poolball("fiveBall", ball5, b5.xcoordinate, b5.ycoordinate))
    solids.append(Poolball("sixBall", ball6, b6.xcoordinate, b6.ycoordinate))
    solids.append(Poolball("sevenBall", ball7, b7.xcoordinate, b7.ycoordinate))
    
    #for obj in solids:
        #print(obj.name, obj.xcoordinate, obj.ycoordinate)
stripes = []
def stripeBallList():
    
    #stripes = []
    stripes.append(Poolball("nineBall", ball9, b9.xcoordinate, b9.ycoordinate))
    stripes.append(Poolball("tenBall", ball10, b10.xcoordinate, b10.ycoordinate))
    stripes.append(Poolball("elevenBall", ball11, b11.xcoordinate, b11.ycoordinate))
    stripes.append(Poolball("twelveBall", ball12, b12.xcoordinate, b12.ycoordinate))
    stripes.append(Poolball("thirteenBall", ball13, b13.xcoordinate, b13.ycoordinate))
    stripes.append(Poolball("fourteenBall", ball14, b14.xcoordinate, b14.ycoordinate))
    stripes.append(Poolball("fifteenBall", ball15, b15.xcoordinate, b15.ycoordinate))
    
    #for obj in stripes:
        #print(obj.name, obj.xcoordinate, obj.ycoordinate)
ballsOnTable = []       
def onTableBallList():
    #ballsOnTable = []
    ballsOnTable.append(Poolball("oneBall", ball1, b1.xcoordinate, b1.ycoordinate))
    ballsOnTable.append(Poolball("twoBall", ball2, b2.xcoordinate, b2.ycoordinate))
    ballsOnTable.append(Poolball("threeBall", ball3, b3.xcoordinate, b3.ycoordinate))
    ballsOnTable.append(Poolball("fourBall", ball4, b4.xcoordinate, b4.ycoordinate))
    ballsOnTable.append(Poolball("fiveBall", ball5, b5.xcoordinate, b5.ycoordinate))
    ballsOnTable.append(Poolball("sixBall", ball6, b6.xcoordinate, b6.ycoordinate))
    ballsOnTable.append(Poolball("sevenBall", ball7, b7.xcoordinate, b7.ycoordinate))
    ballsOnTable.append(Poolball("eightBall", ball8, b8.xcoordinate, b8.ycoordinate))
    ballsOnTable.append(Poolball("nineBall", ball9, b9.xcoordinate, b9.ycoordinate))
    ballsOnTable.append(Poolball("tenBall", ball10, b10.xcoordinate, b10.ycoordinate))
    ballsOnTable.append(Poolball("elevenBall", ball11, b11.xcoordinate, b11.ycoordinate))
    ballsOnTable.append(Poolball("twelveBall", ball12, b12.xcoordinate, b12.ycoordinate))
    ballsOnTable.append(Poolball("thirteenBall", ball13, b13.xcoordinate, b13.ycoordinate))
    ballsOnTable.append(Poolball("fourteenBall", ball14, b14.xcoordinate, b14.ycoordinate))
    ballsOnTable.append(Poolball("fifteenBall", ball15, b15.xcoordinate, b15.ycoordinate))    
ballsInPocket = []    
def pocketedBallList():
    fillerList = []
    
pocketsList = []
def pocketsGeneration():
    pocketsList.append(pockets("topLeft", 131.5, 112.5))
    pocketsList.append(pockets("topCenter", 547.5, 112.5))
    pocketsList.append(pockets("topRight", 968, 112.5))
    pocketsList.append(pockets("bottomLeft", 131.5, 528.5))
    pocketsList.append(pockets("bottomCenter", 547.5, 528.5))
    pocketsList.append(pockets("bottomRight", 968, 528.5))    


# A Python3 program to find if 2 given line segments intersect or not 
class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

# Given three colinear points p, q, r, the function checks if 
# point q lies on line segment 'pr' 
def onSegment(p, q, r): 
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
             (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))): 
        return True
    return False

def orientation(p, q, r): 
    # to find the orientation of an ordered triplet (p,q,r) 
    # function returns the following values: 
    # 0 : Colinear points 
    # 1 : Clockwise points 
    # 2 : Counterclockwise 


    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y)) 
    if (val > 0): 

        # Clockwise orientation 
        return 1
    elif (val < 0): 

        # Counterclockwise orientation 
        return 2
    else: 

        # Colinear orientation 
        return 0

# The main function that returns true if 
# the line segment 'p1q1' and 'p2q2' intersect. 
def doIntersect(p1,q1,p2,q2): 

    # Find the 4 orientations required for 
    # the general and special cases 
    o1 = orientation(p1, q1, p2) 
    o2 = orientation(p1, q1, q2) 
    o3 = orientation(p2, q2, p1) 
    o4 = orientation(p2, q2, q1) 

    # General case 
    if ((o1 != o2) and (o3 != o4)): 
        return True

    # Special Cases 

    # p1 , q1 and p2 are colinear and p2 lies on segment p1q1 
    if ((o1 == 0) and onSegment(p1, p2, q1)): 
        return True

    # p1 , q1 and q2 are colinear and q2 lies on segment p1q1 
    if ((o2 == 0) and onSegment(p1, q2, q1)): 
        return True

    # p2 , q2 and p1 are colinear and p1 lies on segment p2q2 
    if ((o3 == 0) and onSegment(p2, p1, q2)): 
        return True

    # p2 , q2 and q1 are colinear and q1 lies on segment p2q2 
    if ((o4 == 0) and onSegment(p2, q1, q2)): 
        return True

    # If none of the cases 
    return False

logicBuffer = []


def logicSolver():
    print("")
    print("")
    print("")
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "oneBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the one ball into the " + pocket)
        text1 = ("Pocket the one ball into the " + pocket)
        message_display(text1)
        temp = 0
        pocket = ""
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "twoBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the two ball into the " + pocket)
        text2 = ("Pocket the two ball into the " + pocket)
        message_display2(text2)
        temp = 0
        pocket = "" 
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "threeBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the three ball into the " + pocket)
        text3 = ("Pocket the three ball into the " + pocket)
        message_display3(text3)
        temp = 0
        pocket = ""
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "fourBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the four ball into the " + pocket)
        text4 = ("Pocket the four ball into the " + pocket)
        message_display4(text4)
        temp = 0
        pocket = ""
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "fiveBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the five ball into the " + pocket)
        text5 = ("Pocket the five ball into the " + pocket)
        message_display5(text5)
        temp = 0
        pocket = ""
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "sixBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the six ball into the " + pocket)
        text6 = ("Pocket the six ball into the " + pocket)
        message_display6(text6)
        temp = 0
        pocket = ""
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "sevenBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the seven ball into the " + pocket)
        text7 = ("Pocket the seven ball into the " + pocket)
        message_display7(text7)
        temp = 0
        pocket = ""
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "nineBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the nine ball into the " + pocket)
        text9 = ("Pocket the nine ball into the " + pocket)
        message_display9(text9)
        temp = 0
        pocket = ""
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "tenBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the ten ball into the " + pocket)
        temp = 0
        pocket = ""
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "elevenBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the eleven ball into the " + pocket)
        temp = 0
        pocket = ""
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "twelveBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the twelve ball into the " + pocket)
        temp = 0
        pocket = ""
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "thirteenBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the thirteen ball into the " + pocket)
        temp = 0
        pocket = ""
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "fourteenBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the fourteen ball into the " + pocket)
        temp = 0
        pocket = ""
    temp = 0
    pocket = ""
    for index, obj in enumerate(ballsInPocket):
        #temp = 0
        if obj.name == "fifteenBall":
            if temp == 0:
                cur = obj.difficulty
                temp = obj.difficulty
                pocket = obj.pocket
            if obj.difficulty < temp:
                temp = obj.difficulty
                pocket = obj.pocket
            else:
                continue
    if temp == 0:
        logicBuffer.append("")
    else:
        print("Pocket the fifteen ball into the " + pocket)
        temp = 0
        pocket = ""
    print("You are clear to pocket the eight and nine ball into any pocket")  
    text8 = ("You are clear to pocket the eight and nine ball into any pocket")  
    message_display8(text8)
                

mx,my = pygame.mouse.get_pos()

while 1: 
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:sys.exit()
        elif event.type == KEYDOWN and event.key == K_1:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball1, (mx-12.5,my-12.5))
            b1 = Poolball("oneBall", ball1, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b1.name)
            print(b1.xcoordinate)
            print(b1.ycoordinate)
        elif event.type == KEYDOWN and event.key == K_2:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball2, (mx-12.5,my-12.5))
            b2 = Poolball("twoBall", ball2, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b2.name)
            print(b2.xcoordinate)
            print(b2.ycoordinate)   
        elif event.type == KEYDOWN and event.key == K_3:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball3, (mx-12.5,my-12.5))
            b3 = Poolball("threeBall", ball3, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b3.name)
            print(b3.xcoordinate)
            print(b3.ycoordinate) 
        elif event.type == KEYDOWN and event.key == K_4:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball4, (mx-12.5,my-12.5))
            b4 = Poolball("fourBall", ball4, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b4.name)
            print(b4.xcoordinate)
            print(b4.ycoordinate)  
        elif event.type == KEYDOWN and event.key == K_5:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball5, (mx-12.5,my-12.5))
            b5 = Poolball("fiveBall", ball5, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b5.name)
            print(b5.xcoordinate)
            print(b5.ycoordinate)  
        elif event.type == KEYDOWN and event.key == K_6:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball6, (mx-12.5,my-12.5))
            b6 = Poolball("sixBall", ball6, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b6.name)
            print(b6.xcoordinate)
            print(b6.ycoordinate)
        elif event.type == KEYDOWN and event.key == K_7:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball7, (mx-12.5,my-12.5))
            b7 = Poolball("sevenBall", ball7, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b7.name)
            print(b7.xcoordinate)
            print(b7.ycoordinate)
        elif event.type == KEYDOWN and event.key == K_8:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball8, (mx-12.5,my-12.5))
            b8 = Poolball("eightBall", ball5, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b8.name)
            print(b8.xcoordinate)
            print(b8.ycoordinate)
        elif event.type == KEYDOWN and event.key == K_9:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball9, (mx-12.5,my-12.5))
            b9 = Poolball("nineBall", ball9, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b9.name)
            print(b9.xcoordinate)
            print(b9.ycoordinate)
        elif event.type == KEYDOWN and event.key == K_0:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(whiteball, (mx-12.5,my-12.5))
            b0 = Poolball("whiteBall", whiteball, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b0.name)
            print(b0.xcoordinate)
            print(b0.ycoordinate)
        elif event.type == KEYDOWN and event.key == K_q:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball10, (mx-12.5,my-12.5))
            b10 = Poolball("tenBall", ball10, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b10.name)
            print(b10.xcoordinate)
            print(b10.ycoordinate)
        elif event.type == KEYDOWN and event.key == K_w:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball11, (mx-12.5,my-12.5))
            b11 = Poolball("elevenBall", ball11, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b11.name)
            print(b11.xcoordinate)
            print(b11.ycoordinate)
        elif event.type == KEYDOWN and event.key == K_e:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball12, (mx-12.5,my-12.5))
            b12 = Poolball("twelveBall", ball12, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b12.name)
            print(b12.xcoordinate)
            print(b12.ycoordinate)  
        elif event.type == KEYDOWN and event.key == K_r:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball13, (mx-12.5,my-12.5))
            b13 = Poolball("thirteenBall", ball13, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b13.name)
            print(b13.xcoordinate)
            print(b13.ycoordinate) 
        elif event.type == KEYDOWN and event.key == K_t:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball14, (mx-12.5,my-12.5))
            b14 = Poolball("fourteenBall", ball14, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b14.name)
            print(b14.xcoordinate)
            print(b14.ycoordinate) 
        elif event.type == KEYDOWN and event.key == K_y:
            mx,my = pygame.mouse.get_pos()
            screen.blit(background, (100,90))
            screen.blit(ball15, (mx-12.5,my-12.5))
            b15 = Poolball("fifteenBall", ball15, mx-12.5, my-12.5)
            pygame.display.flip()
            print(b15.name)
            print(b15.xcoordinate)
            print(b15.ycoordinate) 
        elif event.type == KEYDOWN and event.key == K_a:
            screen.blit(background, (100,90))
            screen.blit(whiteball, (b0.xcoordinate,b0.ycoordinate))
            screen.blit(ball1, (b1.xcoordinate,b1.ycoordinate))
            screen.blit(ball2, (b2.xcoordinate,b2.ycoordinate))
            screen.blit(ball3, (b3.xcoordinate,b3.ycoordinate))
            screen.blit(ball4, (b4.xcoordinate,b4.ycoordinate))
            screen.blit(ball5, (b5.xcoordinate,b5.ycoordinate))
            screen.blit(ball6, (b6.xcoordinate,b6.ycoordinate))
            screen.blit(ball7, (b7.xcoordinate,b7.ycoordinate))
            screen.blit(ball8, (b8.xcoordinate,b8.ycoordinate))
            screen.blit(ball9, (b9.xcoordinate,b9.ycoordinate))
            screen.blit(ball10, (b10.xcoordinate,b10.ycoordinate))
            screen.blit(ball11, (b11.xcoordinate,b11.ycoordinate))
            screen.blit(ball12, (b12.xcoordinate,b12.ycoordinate))
            screen.blit(ball13, (b13.xcoordinate,b13.ycoordinate))
            screen.blit(ball14, (b14.xcoordinate,b14.ycoordinate))
            screen.blit(ball15, (b15.xcoordinate,b15.ycoordinate))
            pygame.display.flip() 
            
        elif event.type == KEYDOWN and event.key == K_c:
            mx,my = pygame.mouse.get_pos()
            b0 = Poolball("whiteBall", whiteball, 1050,100)        
            b1 = Poolball("oneBall", ball1, 1075, 100)
            b2 = Poolball("twoBall", ball2, 1100,100)
            b3 = Poolball("threeBall", ball3, 1125,100)
            b4 = Poolball("fourBall", ball4, 1150,100)
            b5 = Poolball("fiveBall", ball5, 1175,100)
            b6 = Poolball("sixBall", ball6, 1200,100)
            b7 = Poolball("sevenBall", ball7, 1050,125)
            b8 = Poolball("eightBall", ball8, 1075,125)
            b9 = Poolball("nineBall", ball9, 1100,125)
            b10 = Poolball("tenBall", ball10, 1125,125)
            b11 = Poolball("elevenBall", ball11, 1150,125)
            b12 = Poolball("twelveBall", ball12, 1175,125)
            b13 = Poolball("thirteenBall", ball13, 1200,125)
            b14 = Poolball("fourteenBall", ball14, 1050,150)
            b15 = Poolball("fifteenBall", ball15, 1075,150)            
            screen.blit(background, (100,90))
            pygame.display.flip()   
        elif event.type == KEYDOWN and event.key == K_z:
            #create solid ball list
            solidBallList()
            #create stripe ball list
            stripeBallList()
            #
            onTableBallList()
            #
            pocketsGeneration()
            #
            solidsSearch()
            #
            logicSolver()
            #
        elif event.type == KEYDOWN and event.key == K_x:
            #create solid ball list
            solidBallList()
            #create stripe ball list
            stripeBallList()
            #
            onTableBallList()
            #
            pocketsGeneration()
            #
            stripesSearch()   
            #
            logicSolver()
            

            
                    
