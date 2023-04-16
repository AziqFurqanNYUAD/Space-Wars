import os
import random
import time
path = os.getcwd()+ '/'
add_library("minim")
NUM_ROWS = 20
NUM_COLS = 20
global turbo
turbo = False
Game=True
Select=True

#import library for music 
player = Minim(this)

#Setsup the background
class Background():
    def __init__(self,x1,y1,x2,y2,w,h):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.w=w
        self.h=h
        self.image1 = loadImage(path + "/images/" +str("bg_space.jpg"))
        self.image2 = loadImage(path + "/images/" +str("bg_space_invert.jpg"))
    
    #we loop between 2 images one original and one inverted to loop the background
    def back_loop(self):
        if self.y1>=0 or self.y1>=-1000: 
            self.y1+=25
            image(self.image1, 0, self.y1, 1000, 1000)
        if self.y2>=-1000:
            self.y2+=25
            image(self.image2, 0, self.y2, 1000, 1000) 
        if self.y1==0:
            self.y2=-1000 
        if self.y2==0:
            self.y1=-1000
            
#this is the main spaceship that the user controls
class SpaceShip():
    def __init__(self,x,y,w,h):
        global Game
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.buttons={LEFT:False,RIGHT:False}
    
    # places the spaceship on the screen
    def instance(self,target, powerup):
        self.spaceship=loadImage(path + "/images/" + "trek.png")
        noFill()
        noStroke()
        rect(self.x,self.y,self.w,self.h)
        image(self.spaceship,self.x,self.y,self.w,self.h)
        
        self.ring=loadImage(path + "/images/" + "ring.png")
        if powerup.turbo==True :
            image(self.ring,self.x-(self.w/2),self.y-30,self.w*2,self.w*2)
            
    # moves the spaceship left right based on the key movement
    def move_ship(self):
        if self.buttons[LEFT]==True and self.x>=100:
            self.x-=20

        if self.buttons[RIGHT]==True and self.x<=900:
            self.x+=20
            
    # controls collision happend and ends game when collision happend with asteriod
    def collision(self,obstacles,powerup):
        global Game
        if powerup.turbo==False :
            if self.x >= obstacles.x_meteor -50 and self.x <= obstacles.x_meteor+50:
                if self.y >= obstacles.y_meteor and self.y <= obstacles.y_meteor+150:
                    Game=False
                    
 
#code for the gems that when all collected lead to the invincibility shield
class Power_Up():
    def __init__(self):
        self.turbo=False
        self.booster=False
        self.check=0
        self.collected = []
        self.imgnumber = str(random.randint(1,4))
        self.booster_img=loadImage(path + "/images/" + "stone" + self.imgnumber+ ".png")
    
    # controlls falling of shield
    def instance(self):
        if self.booster == False:
            self.x_pos = random.randint(100,900)
            self.y_pos = -1000
            self.booster =True
        image(self.booster_img, self.x_pos,self.y_pos-20,50,50)    
                  
        
        if self.booster==True:
            self.y_pos=self.y_pos+20
            
        if self.y_pos >800:
            self.imgnumber = str(random.randint(1,4))
            self.booster_img=loadImage(path + "/images/" + "stone" + self.imgnumber+ ".png")
            self.booster = False

    
     # controls collision with gems    
    def collision(self,ship,counter):
        if self.x_pos in range(ship.x-50,ship.x+51) and self.y_pos in range(ship.y,ship.y+51):
            if self.imgnumber not in self.collected:
                self.collected.append(self.imgnumber)
                counter.score+=10
            
            self.booster=False
                        
            self.imgnumber = str(random.randint(1,4))
            self.booster_img=loadImage(path + "/images/" + "stone" + self.imgnumber+ ".png") 
    #if all gems collecetd activiate invincibility shield
        if len(self.collected) == 4 or counter.score == 0:
            self.turbo = True
            self.check = counter.score
            self.collected = []
        
        #deactivate invincibility shield after 15 points
        if counter.score-self.check >= 15:
            self.turbo = False 
            self.check = 0 
        
        #display images of collected gems on the top right 
        for i in self.collected:
            self.img_show = loadImage(path + "/images/" + "stone" + i + ".png")
            image(self.img_show, 40, 10+(50*int(i)),50,50) 
            noFill()
            stroke(255)
            strokeWeight(4)
            rect(30,60,80,200)
# coins
class Coins:

    def __init__(self):
        self.new=True
        self.x_pos=1
        self.coin = loadImage(path + "/images/" + str("yellowcoin.png"))
    
    
    #control display of coins on screen
    def instance(self):            
        if self.new==True:
            self.x_pos=random.randint(100,900)
            self.y_pos= -10
            self.new=False
        image(self.coin,self.x_pos,self.y_pos,50,50)
        
        if self.new==False:
            self.y_pos=self.y_pos+25
        if self.y_pos>1000:
            self.new=True
    # code for when we collect the coints increments score         
    def collect(self,ship,counter):
        if self.x_pos in range(ship.x-50,ship.x+51) and self.y_pos in range(ship.y,ship.y+51):
            counter.score+=5
            self.new=True
    
    
#code for asteroids
class Obstacles():
    
    def __init__(self):
        self.onscreen=True
        self.meteor = loadImage(path + "/images/" +"meteor.png")
        self.speed = 20
        self.speed_check = True
   #controls falling of asteroids 
    def incoming(self,target,counter):
        if self.onscreen == True:
            self.x_meteor = random.randint(250,750)
            self.y_meteor = -50    
            self.onscreen = False
        image(self.meteor,self.x_meteor,self.y_meteor,100,200)
        
        # increase speed of asteroids after 100 points
        if  self.speed_check == True and counter.score !=0 and counter.score%100 == 0:
            self.speed += 5
            self.speed_check = False
        else:
            self.speed_check = True
        
        if self.y_meteor >= 900:
            self.onscreen = True
        else:
            if self.onscreen == False:
                self.y_meteor += self.speed


# controls score counter and also has the display screens
class Counter:
    def __init__(self):
        self.score=0
        self.game=True
        
    def incrementer(self, target):
        global Game
        global Select

        if Game==False:
            self.game=False
        if Game==True and self.game==False:
            self.game=True
            self.score=0    


    def display(self,target):
        textSize(30)
        fill(255)
        font2 = loadFont('PTMono-Regular-16.vlw')
        textFont(font2, 22);
        text("Score: " +str(self.score),30,50)
  
    def display_endscreen(self,x,y):
        background(0)
        textSize(40)
        fill(255)
        font2 = loadFont('PTMono-Regular-16.vlw')
        textFont(font2, 50);
        text("GAME OVER",365,400)
        textSize(25)
        textFont(font2, 24);    
        text("Your Score: " +str(self.score),400,450)  
        text("Click anywhere to restart.",335,500)
       

class Menu:
    def __init__(self):
        self.bg=loadImage(path + "/images/" +"bg.jpeg")
        
    def display(self):
        image(self.bg,0,0,1000,1000)
        font = loadFont('Phosphate-Inline-16.vlw')
        textFont(font, 50);
        text("~ Sexa Rush ~", 325, 175);
        font2 = loadFont('PTMono-Regular-16.vlw')
        textFont(font2, 22);
        text("1. Use the left and right arrow keys to move your space ship.", 55, 250);
        text("2. Collect the 4 different infinity stones to get a sexa shield.", 55, 290);
        text("3. When activated, the sexa shield protects you from asteroids!", 55, 330);
       
       
        text("Click the play button below to get started.", 200, 400);
        fill(0)
        rect(430,500,100,50, 20)
        fill(255)
        textFont(font, 32);
        text("PLAY", 445 ,535)
  
    def mouseClickedd(self):
        global Game
        global Select
        if Game==True and Select==True:
            if mousePressed:
                if mouseX in range(430,530) and mouseY in range(500,550):
                    Select=False

                    
ship = SpaceShip(535,700,100,170)
coin = Coins()
background_screen = Background(0,0,0,-1000,1000,1000)
obstacles = Obstacles()
counter = Counter()
menu = Menu()
power_up=Power_Up()

def setup():
    global Game        
    size(1000,1000)
    stroke(255)
    background(0)
    
    
    
def draw():
    global Game
    global Select
    global turbo
    if Select==True and Game==True:
        menu.display()
        menu.mouseClickedd()
        music = player.loadFile(path + "/data/piano.mp3")
        music.loop()
    
    if Game==True and Select==False:

        background_screen.back_loop()
        coin.instance()
        coin.collect(ship,counter)
        power_up.instance()
        power_up.collision(ship,counter)
        ship.move_ship()
        ship.instance(menu,power_up)
        obstacles.incoming(power_up,counter)
        ship.collision(obstacles,power_up)
        counter.incrementer(ship)
        counter.display(ship)

           
    if Game==False and Select==False:
        counter.display_endscreen(400,600)
        
        obstacles.speed = 20
        obstacles.x_meteor = 0
        obstacles.y_meteor = 0
   
        
        if mousePressed:
            Select=True
            Game=True
            
            
# these are the keyhandlers controlling the key presses    
def keyPressed():
    if keyCode == LEFT:
        ship.buttons[LEFT] = True    
    elif keyCode == RIGHT:
        ship.buttons[RIGHT] = True

        
def keyReleased():
    if keyCode == LEFT:
        ship.buttons[LEFT] = False
    elif keyCode == RIGHT:
        ship.buttons[RIGHT] = False


        
        
        
    
        
    
        
        
