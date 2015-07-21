import pygame, random
import sys, math
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN=(85,107,47)
YELLOW=(255, 250, 0)
color_lst=[RED, BLUE, GREEN, YELLOW]
flag,dist= 0,0
const_dimension=20
ppos=[0,0]
#TIME ELAPSED za
blastt=False
blit_lst=[]
t0=pygame.time.get_ticks()


#Text on Screen
def text_to_screen(screen, text, x,y, size):
    text=str(text)
    font =pygame.font.SysFont("comicsansms",size)
    text=font.render(text, True, BLACK)
    screen.blit(text, (x,y))
   
def healthbar(tt):
    text_to_screen(screen, "Health Bar", screen_width-120,1, 15)
         
    #print(tt)
    if tt/20000>=1: #TIME UP!
        print("TIME OVER")
        over()
    if tt%15000>= 7500:
        text_to_screen(screen, "CHANGE PLAYER COLOR!!", screen_width-150,30, int(4+4*math.sin((tt%1010)/2000)*math.pi))
       
    #if flag2==1:    #new color picked
    pygame.draw.rect(screen,BLACK, ((screen_width-120,20),(100-int((tt/20000.0)*100), 10)) )
    
def over():
    print("GAME OVER.")
    monster=pygame.image.load("monster.gif").convert_alpha()
    screen.blit(monster, (screen_width/2-180, screen_height/2-100 ))
    screen.blit(gameover, (int(screen_width/2-100),int(screen_height/2-30)))
    pygame.display.flip()
    pygame.time.wait(1500)
           
    pygame.quit()
    sys.exit()

# --- Classes
class Block(pygame.sprite.Sprite):
        
    def __init__(self, color):
# Call the parent class (Sprite) constructor
        super().__init__()

        self.images = []
        self.images.append(pygame.image.load("redbubble.png").convert_alpha())
        self.images.append(pygame.image.load("greenbubble.png").convert_alpha())
        self.images.append(pygame.image.load("bluebubble.png").convert_alpha())
        self.images.append(pygame.image.load("yellowbubble.png").convert_alpha())
        self.index=[0,1,2,3]

        
        self.image_index= random.choice(self.index)
        if color==RED:
            self.color=RED
            self.image = self.images[0]
        elif color==GREEN:
            self.color=GREEN
            self.image = self.images[1]
        elif color==BLUE:
            self.color=BLUE
            self.image = self.images[2]
        elif color==YELLOW:
            self.color=YELLOW
            self.image = self.images[3]
        
        
        self.radius=15
        self.color=color
       
        #self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        #pygame.draw.circle(self.image, color,(int(self.rect.x)+self.radius, int(self.rect.y)+self.radius), self.radius, 0)
        
    def update(self):
        self.rect.y+=1

class Block_x(pygame.sprite.Sprite):
          
    def __init__(self, color):
# Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.set_alpha(190)   
        self.radius=10
        self.color=color
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, self.color,(int(self.rect.x+3), int(self.rect.y)+self.radius), self.radius, 0)
    def update(self):
        self.rect.x+=1

       
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
        self.images = []
        self.images.append(pygame.image.load("red_p.png").convert_alpha())
        self.images.append(pygame.image.load("green_p.png").convert_alpha())
        self.images.append(pygame.image.load("blue_p.png").convert_alpha())
        self.images.append(pygame.image.load("yellow_p.png").convert_alpha())
        self.index=[0,1,2,3]
        
        self.image = self.images[0]          #image.load("player.png").convert_alpha()
       
        self.rect = self.image.get_rect()
        self.color=RED      #initially
        
        self.rect.y=screen_height-10
    def update(self):
 
# Get the current mouse position
        pos = pygame.mouse.get_pos()
       
        self.rect.x = pos[0]
       
        if self.color==RED:
            self.image = self.images[0]
        elif self.color==GREEN:
            self.image=self.images[1]
        elif self.color==BLUE:
            self.image=self.images[2]
        elif self.color==YELLOW:
            self.image=self.images[3]
            

class Bullet(pygame.sprite.Sprite):
 
    def __init__(self):
# Call the parent class (Sprite) constructor
        super().__init__()
        self.image=pygame.image.load("bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
         
    def update(self):
 
        self.rect.y -= 3
       
# Initialize Pygame
pygame.init()

#XXXXXXXXXXXXXX Creating New Blocks       
def create_new_sprites():
   
    color=random.choice(color_lst)
    block = Block(color)
    color_x=random.choice(color_lst)
    block_x = Block_x(color)
 
    block.rect.x = random.randint(10, screen_width-20)
    block.rect.y = random.randint(-1800, -50)
    block_x.rect.x = random.randint(-1800, -50)
    block_x.rect.y = random.randint(8, screen_height-8)
 
    block_list.add(block)
    all_sprites_list.add(block)
    blockx_list.add(block_x)
    all_sprites_list.add(block_x)

 
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
gameover=pygame.image.load("gameover.png").convert_alpha()
#XXXX

# --- Sprite lists

all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
blockx_list=pygame.sprite.Group()

# --- Create the sprites
for i in range(20):
    color=random.choice(color_lst)
    block = Block(color)
    color_x=random.choice(color_lst)
    block_x = Block_x(color)
 
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randint(-2000, -50)
    block_x.rect.x = random.randint(-2000, -50)
    block_x.rect.y = random.randrange(screen_width)
 
    block_list.add(block)
    all_sprites_list.add(block)
    blockx_list.add(block_x)
    all_sprites_list.add(block_x)
   
# Create player block
player = Player()
all_sprites_list.add(player)

 
done = False
clock = pygame.time.Clock()
score = 0
player.rect.y = 370
 #imAGES
ppos[0], ppos[1]= player.rect.x, player.rect.y

flame=pygame.image.load("flame.png").convert_alpha()
#@background=pygame.image.load("space.png").convert_alpha() 

# -------- Main Program Loop -----------
while not done:
    t1=pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
        # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            bullet.rect.x = player.rect.x +const_dimension/2+8  ############
            bullet.rect.y = player.rect.y
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                dist=1.5
            elif event.key==pygame.K_UP:
                dist=-1.5
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                dist=0
            elif event.key==pygame.K_UP:
                dist=0
            
           
        elif event.type == pygame.USEREVENT + 1:
            create_new_sprites()
       
           
           
# --- Game logic
    player.rect.y+=dist
    all_sprites_list.update()
    #Bullet Block Collision
    for bullet in bullet_list:
 
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, False)
       
         
# For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            blast=pygame.image.load("blast.png").convert_alpha()
            blit_lst.append( (block.rect.x, block.rect.y))
            screen.blit(blast,(block.rect.x, block.rect.y))
            pygame.time.wait(15)
                 
            blastt=True
             
            screen.blit(blast, (block.rect.x, block.rect.y))
             
            block.rect.x = random.randrange(screen_width)
            block.rect.y = random.randint(-2000, -50)
            print(score)
 
        if bullet.rect.y < -10:  #Beyond Screen
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
    for block_x in blockx_list:             #Checking for Inter Blocks Collision
        inter_hit_list= pygame.sprite.spritecollide(block_x, block_list, False)
        for block in inter_hit_list:
            if block.color==block_x.color:  #collision of same COLOR Blocks
                block.rect.x = random.randrange(screen_width)
                block.rect.y = random.randint(-2000, -50)
                block_x.rect.x = random.randint(-2000, -50)
                block_x.rect.y = random.randrange(screen_width)

    #COLLISION With PLAYER:
    
    player_hit_list= pygame.sprite.spritecollide(player, block_list, False)
    if len(player_hit_list)>0:
        health_flag=1       #Implies a collision has taken place. Restart Healthbar
        tt=0
        t0=t1
        print(str(player_hit_list[0].color)+" PLAYER COLOR "+str(player.color))
        if player_hit_list[0].color==player.color:
            
            over()
            
        else:
            player.color=player_hit_list[0].color
            player_hit_list[0].rect.y, player_hit_list[0].rect.x =random.randint(-2000,-10) , random.randrange(screen_width-10)
    else:
        health_flag,tt=0,pygame.time.get_ticks()
               

     #Blocks Passing Down BEYOND Screen      
    for block in block_list:
        if block.rect.y>screen_height+10:
            over()
            block.rect.y=random.randint(-2000,-50)
     #Blocks Passing RHS BEYOND Screen      
    for block in blockx_list:
        if block.rect.x>screen_width+10:
            block.rect.x=random.randint(-2000,-50)
            block.rect.y=random.randint(10, screen_height-5)

           
    pygame.time.set_timer(pygame.USEREVENT + 1, 3500)
    screen.fill(WHITE)
    if blastt==True:
        blastt=False
        for i in range(len(blit_lst)):
            
            screen.blit(blast, (blit_lst[i][0], blit_lst[i][1]))
        blit_lst=[]
    #screen.blit(background, (0,0))
    screen.blit(flame, (0, screen_height/2+115 ))
    all_sprites_list.draw(screen)
    
    healthbar(t1-t0)
    text_to_screen(screen,score, 30,30, 20)
    pygame.display.flip()
# --- Limit to 20 frames per second
    clock.tick(60)
pygame.quit()
 
