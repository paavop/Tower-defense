import pygame
from game import Game
from spot import Spot
from road import Road
from tower import Tower
from enemy import Enemy

teksti1=""
teksti2=""
teksti3="" 
color=(200,191,231)
start=None
enemies={}
enemycount=0
time=0
prev_time=0
peli=Game()

def update_screen():
    for i in range(12):
        for j in range(20):
            if isinstance(peli.board.get_spot(i, j),Tower):
                screen.blit(torni,(50*j,50*i))
                continue
            if isinstance(peli.board.get_spot(i, j),Road):
                if(peli.board.get_spot(i, j).start):
                    screen.blit(tie_start,(50*j,50*i))
                    continue
                if(peli.board.get_spot(i, j).goal):
                    screen.blit(tie_goal,(50*j,50*i))
                    continue
            
                screen.blit(tie,(50*j,50*i))
                continue
            if isinstance(peli.board.get_spot(i, j),Spot):
                screen.blit(maa,(50*j,50*i))
    pygame.draw.lines(screen, (1,0,0), False,[(0,600),(998,600),(998,698),(0,698),(0,600)],4)
    print_text()
    for i in range(enemycount):
        if enemies[i]!=None:
            draw_enemy(enemies[i])
    print_time()
    pygame.display.flip()
    
def draw_enemy(enemy):
    if not (enemy.spot.goal):
        
        if (enemy.spot.x>enemy.spot.next.x):
            kuva=bugu
        if (enemy.spot.x<enemy.spot.next.x):
            kuva=bugd
        if (enemy.spot.y>enemy.spot.next.y):
            kuva=bugl
        if (enemy.spot.y<enemy.spot.next.y):
            kuva=bugr
        screen.blit(kuva,(enemy.spot.y*50,enemy.spot.x*50))
    else:
        print("You lose")
        running=False
def new_text(teksti):
    if (teksti!=None):
        global teksti1
        global teksti2
        global teksti3
        teksti3=teksti2
        teksti2=teksti1
        teksti1=teksti
    
def print_text():
    
    pygame.draw.rect(screen,(200,191,200),(10,610,200,80),0)
    pygame.draw.rect(screen,(1,0,0),(10,610,200,80),1)
    font=pygame.font.Font(None, 15)
    text=font.render(teksti1,1,(10,10,10))
    text2=font.render(teksti2,1,(10,10,10))
    text3=font.render(teksti3,1,(10,10,10))
    screen.blit(text,(20,675))
    screen.blit(text2,(20,650))
    screen.blit(text3,(20,625))


def make_road():
    global start
    for i in range(7):
        peli.board.add_road(5, i)
        
    start=peli.board.get_spot(5, 0)
    
    for i in range (3):
        peli.board.add_road(5+i,7)
    for i in range (6):
        peli.board.add_road(8,7+i)
    for i in range (3):
        peli.board.add_road(8-i,13)
    for i in range(7):
        peli.board.add_road(5, 13+i)
    
def spawn_enemy(name,speed,hp,start):
    global enemycount
    
    enemies[enemycount]=Enemy(name,speed,hp,start)
    
    enemycount=enemycount+1
    
def print_time():
    pygame.draw.rect(screen,color,(850,610,125,80),0)
    teksti="Time: "+str(int(time))
    font=pygame.font.Font(None, 20)
    text=font.render(teksti,1,(10,10,10))
    screen.blit(text,(850,610))
    
make_road()

pygame.init()
clock=pygame.time.Clock()
    
logo = pygame.image.load("logo32x32.png")
torni=pygame.image.load("tower.png")
tie=pygame.image.load("road.png")
tie_start=pygame.image.load("road_start.png")
tie_goal=pygame.image.load("road_goal.png")
maa=pygame.image.load("empty.png")
bugu=pygame.image.load("bug_u.gif")
bugd=pygame.image.load("bug_d.gif")
bugl=pygame.image.load("bug_l.gif")
bugr=pygame.image.load("bug_r.gif")

pygame.display.set_icon(logo)
pygame.display.set_caption("Tower defense")

size=1000
    
    # create a surface on screen that has the size of 240 x 180
screen_width=size
screen_height=size-300
screen = pygame.display.set_mode((screen_width,screen_height))



screen.fill(color)
    



spawn_enemy("vihu", 5, 100,start)

enemies[0].move()
    
pygame.display.flip()

running=True

while running:
    
    a=(pygame.mouse.get_pos())
    if pygame.mouse.get_pressed()==(1,0,0):
        if(a[1]<=600):
            new_text(peli.board.add_tower(int(a[1]/50), int(a[0]/50),100,5,5))
    if pygame.mouse.get_pressed()==(0,0,1):
        if(a[1]<=600):
            new_text(peli.board.remove_tower(int(a[1]/50), int(a[0]/50)))
    
    for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                
    if running:      
        update_screen()
    clock.tick(30)
    time=pygame.time.get_ticks()/1000
    if(int(time)>prev_time):
        enemies[0].move()
        prev_time+=1
    pygame.display.flip()
    
    
