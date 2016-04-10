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
towers={}
enemycount=0
towercount=0
time=0
prev_time=0
peli=Game()
pygame.init()
done=False

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
            if(draw_enemy(enemies[i])):
                pygame.time.wait(500)
                new_text("You lose")
                draw_lose_screen()
                font=pygame.font.Font(None, 200)
                text=font.render(teksti1,1,(10,10,10))
                screen.blit(text,(250,250))
                pygame.display.flip()
                pygame.time.wait(2000)
                pygame.quit()
    print_time()
    pygame.display.flip()
    
def draw_lose_screen():
    s=pygame.Surface((1000,600))
    s.set_alpha(128)
    s.fill((176,0,0))
    screen.blit(s,(0,0))
        
def draw_enemy(enemy):
    kuva=None
    ya=0
    xa=0
    if not (enemy.spot.goal):
        if (enemy.spot.x>enemy.spot.next.x):
            kuva=bugu
            xa=-enemy.get_frame()
        if (enemy.spot.x<enemy.spot.next.x):
            kuva=bugd
            xa=enemy.get_frame()
        if (enemy.spot.y>enemy.spot.next.y):
            kuva=bugl
            ya=-enemy.get_frame()
        if (enemy.spot.y<enemy.spot.next.y):
            kuva=bugr
            ya=enemy.get_frame()
        screen.blit(kuva,(ya+enemy.spot.y*50,xa+enemy.spot.x*50))
        draw_enemy_hp(enemy,ya,xa)
        print(str(ya+enemy.spot.y*50)+"   "+str(xa+enemy.spot.x*50))         
        enemy.add_frame(50*((pygame.time.get_ticks()/1000)-enemy.get_lastmove())/enemy.get_timetonext(),pygame.time.get_ticks()/1000)
        
    else:
        screen.blit(kuva,(enemy.spot.y*50,enemy.spot.x*50))
        pygame.display.flip()
        return True
    
def draw_enemy_hp(enemy,ya,xa):
    percentage=enemy.get_relative_hp()
    green=40*percentage
    red=40-green
    if(green>0):
        pygame.draw.rect(screen,(0,200,0),(ya+enemy.spot.y*50+5,xa+enemy.spot.x*50+5,green,5),0)
    if(red>0 and red<=40):
        pygame.draw.rect(screen,(200,0,0),(ya+enemy.spot.y*50+5+green,xa+enemy.spot.x*50+5,red,5),0)

    
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
    
def spawn_enemy(name,hp,speed,start):
    global enemycount
    
    enemies[enemycount]=Enemy(name,hp,speed,start,enemycount)
    
    enemycount=enemycount+1
    
def add_tower(a,price,power,myrange,speed):
    global towercount
    if not (isinstance(peli.board.get_spot(int(a[1]/50),int(a[0]/50)),Road)):
        if not (isinstance(peli.board.get_spot(int(a[1]/50),int(a[0]/50)),Tower)):
            new_text(peli.board.add_tower(int(a[1]/50), int(a[0]/50),price,power,myrange,towercount,speed))
            towers[towercount]=peli.board.get_spot(int(a[1]/50), int(a[0]/50))
            towercount+=1
    
    
    
def remove_tower(a):
    global towercount
    if  (isinstance(peli.board.get_spot(int(a[1]/50), int(a[0]/50)),Tower)):
        del towers[peli.board.get_spot(int(a[1]/50),int(a[0]/50)).get_index()]
    new_text(peli.board.remove_tower(int(a[1]/50), int(a[0]/50)))
    
    
    
          
def print_time():
    pygame.draw.rect(screen,color,(850,610,125,80),0)
    teksti="Time: "+str(int(time))
    font=pygame.font.Font(None, 20)
    text=font.render(teksti,1,(10,10,10))
    screen.blit(text,(850,610))
    
def shoot_towers():
    for i in towers:
        if ((pygame.time.get_ticks()/1000)-towers[i].lastshot>(2/towers[i].speed)):
            towers[i].shoot(enemies,pygame.time.get_ticks()/1000)
            
make_road()


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
    



spawn_enemy("vihu", 1000, 4,start)


    
pygame.display.flip()

running=True

while running:
    
    a=(pygame.mouse.get_pos())
    if pygame.mouse.get_pressed()==(1,0,0):
        if(a[1]<=600):
            add_tower(a, 100, 100, 5, 2)
            #new_text(peli.board.add_tower(int(a[1]/50), int(a[0]/50),100,5,5))
    if pygame.mouse.get_pressed()==(0,0,1):
        if(a[1]<=600):
            remove_tower(a)
            
    
    for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                
    if running:      
        update_screen()
    #clock.tick(30)
    time=pygame.time.get_ticks()/1000
    
    #if(time>5 and not done):
        #done=True
        #spawn_enemy("name", 100, 4, start)
        
    shoot_towers()
    for i in enemies:
        if (enemies[i]!=None):
            if(enemies[i].is_alive()):
                if(time>prev_time+enemies[i].get_timetonext()):
                    

                    enemies[i].move()
                    #enemies[i].shot(10)
                    
                    enemies[i].framezero()
                    prev_time+=enemies[i].get_timetonext()
            else:
                enemies[i]=None
    
    
    
