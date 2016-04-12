import pygame
from game import Game
from spot import Spot
from road import Road
from tower import Tower
from enemy import Enemy
from random import randint
import sys


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
money=1000
prev_time=0
peli=Game()
pygame.init()
done=False
lost=False
buttonx=120
buttony=37
firstx=350
firsty=600
space=(100-2*buttony-8)/3
name1="Cannon"
name2="Adv. cannon"
name3="Super cannon"
name4="Sniper"
def update_screen():
  
    for i in range(12):
        for j in range(20):
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
                sys.exit(0)
    for i in range(12):
        for j in range(20):
            if isinstance(peli.board.get_spot(i, j),Tower):
                draw_tower(peli.board.get_spot(i,j),50*j,50*i)
                continue
       
    draw_menu()     
    
    pygame.display.flip()
    
def draw_lose_screen():
    s=pygame.Surface((1000,600))
    s.set_alpha(128)
    s.fill((176,0,0))
    screen.blit(s,(0,0))

def draw_tower(tower,x,y):
    ya=tower.shot_y(pygame.time.get_ticks())
    xa=tower.shot_x(pygame.time.get_ticks())
    screen.blit(rotatecenter(torni,tower.angletoenemy(pygame.time.get_ticks())),(x,y))
    if(ya!=0 or xa!=0):
        pygame.draw.circle(screen,(1,0,0),(x+25+ya,y+25+xa),7,0)
    
    if (tower.target!= None and tower.target.gotshot(pygame.time.get_ticks(),tower.timetotarget)):
            frame=tower.target.get_frame()
            xd=0
            yd=0
            if (tower.target.spot.x>tower.target.spot.next.x):
                xd=-frame
            if (tower.target.spot.x<tower.target.spot.next.x):
                xd=frame
            if (tower.target.spot.y>tower.target.spot.next.y):
                yd=-frame
            if (tower.target.spot.y<tower.target.spot.next.y):
                yd=frame
            
            screen.blit(boom_s, (12+yd+tower.target.spot.y*50,12+xd+tower.target.spot.x*50))
    

def rotatecenter(image,angle):    
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def draw_enemy(enemy):
    kuva=bugu
    ya=0
    xa=0
    frame=enemy.get_frame()
    
    if not (enemy.spot.goal):
        if (enemy.spot.x>enemy.spot.next.x):
            kuva=bugu
            xa=-frame
        if (enemy.spot.x<enemy.spot.next.x):
            kuva=rotatecenter(bugu,180)
            xa=frame
        if (enemy.spot.y>enemy.spot.next.y):
            kuva=rotatecenter(bugu,90)
            ya=-frame
        if (enemy.spot.y<enemy.spot.next.y):
            kuva=rotatecenter(bugu,270)
            ya=frame
        screen.blit(kuva,(ya+enemy.spot.y*50,xa+enemy.spot.x*50))
        
        draw_enemy_hp(enemy,ya,xa)
        #print(str(int(ya+enemy.spot.y*50))+"   "+str(int(xa+enemy.spot.x*50)))         
        enemy.add_frame(25*((pygame.time.get_ticks()/1000)-enemy.get_lastmove())/enemy.get_timetonext(),pygame.time.get_ticks()/1000)
        
    else:
        for i in range(12):
            for j in range(20):
                if isinstance(peli.board.get_spot(i, j),Tower):
                    screen.blit(boom,(50*j,50*i))
        for i in range(enemycount):
            if (enemies[i]!=None and enemies[i]!=enemy):
                draw_enemy(enemies[i])
        screen.blit(kuva,(enemy.spot.y*50,enemy.spot.x*50))
        pygame.display.flip()
        lost=True
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
    font=pygame.font.Font("Mono.ttf", 10)
    text=font.render(teksti1,1,(10,10,10))
    text2=font.render(teksti2,1,(10,10,10))
    text3=font.render(teksti3,1,(10,10,10))
    screen.blit(text,(20,675))
    screen.blit(text2,(20,650))
    screen.blit(text3,(20,625))

def print_buttons():
    teksti=("Build")
    font=pygame.font.Font("mono.ttf",16)
    text=font.render(teksti,1,(10,10,10))
    
    screen.blit(text,(firstx-70,firsty+space+6,buttonx,buttony))
    normal1=(200,191,200)
    normal2=(1,0,0)
    chosen1=(200,100,100)
    chosen2=(200,0,0)
    a=(pygame.mouse.get_pos())
    if(a[0]>firstx and a[0]<firstx+buttonx and a[1]>firsty+space+4  and a[1]<firsty+space+4+buttony ):
        pygame.draw.rect(screen,chosen1,(firstx,firsty+space+4,buttonx,buttony),0)
        pygame.draw.rect(screen,chosen2,(firstx,firsty+space+4,buttonx,buttony),1)
    else:
        pygame.draw.rect(screen,normal1,(firstx,firsty+space+4,buttonx,buttony),0)
        pygame.draw.rect(screen,normal2,(firstx,firsty+space+4,buttonx,buttony),1)
        
    if(a[0]>firstx and a[0]<firstx+buttonx and a[1]>firsty+space+4+buttony+space  and a[1]<firsty+space+4+2*buttony+space ):
        pygame.draw.rect(screen,chosen1,(firstx,firsty+space+4+buttony+space,buttonx,buttony),0)
        pygame.draw.rect(screen,chosen2,(firstx,firsty+space+4+buttony+space,buttonx,buttony),1)
    else:
        pygame.draw.rect(screen,normal1,(firstx,firsty+space+4+buttony+space,buttonx,buttony),0)
        pygame.draw.rect(screen,normal2,(firstx,firsty+space+4+buttony+space,buttonx,buttony),1)

    if(a[0]>firstx+buttonx+space and a[0]<firstx+2*buttonx+space and a[1]>firsty+space+4  and a[1]<firsty+space+4+buttony ):
        pygame.draw.rect(screen,chosen1,(firstx+buttonx+space,firsty+space+4,buttonx,buttony),0)
        pygame.draw.rect(screen,chosen2,(firstx+buttonx+space,firsty+space+4,buttonx,buttony),1)
    else:
        pygame.draw.rect(screen,normal1,(firstx+buttonx+space,firsty+space+4,buttonx,buttony),0)
        pygame.draw.rect(screen,normal2,(firstx+buttonx+space,firsty+space+4,buttonx,buttony),1)

    if(a[0]>firstx+buttonx+space and a[0]<firstx+2*buttonx+space and  a[1]>firsty+space+4+buttony+space  and a[1]<firsty+space+4+2*buttony+space ):
        pygame.draw.rect(screen,chosen1,(firstx+buttonx+space,firsty+space+buttony+space+4,buttonx,buttony),0)
        pygame.draw.rect(screen,chosen2,(firstx+buttonx+space,firsty+space+buttony+space+4,buttonx,buttony),1)
    else:
        pygame.draw.rect(screen,normal1,(firstx+buttonx+space,firsty+space+buttony+space+4,buttonx,buttony),0)
        pygame.draw.rect(screen,normal2,(firstx+buttonx+space,firsty+space+buttony+space+4,buttonx,buttony),1)
    
def draw_menu():
    pygame.draw.rect(screen,color,(0,600,1000,100),0)
    pygame.draw.lines(screen, (1,0,0), False,[(0,600),(998,600),(998,698),(0,698),(0,600)],4)
    print_text()
    print_stats()
    print_buttons()
    
def make_road():
    global start
    for i in range(17):
        peli.board.add_road(3, i)
        
    start=peli.board.get_spot(3, 0)
    
    for i in range (3):
        peli.board.add_road(3+i,17)
    for i in range (16):
        peli.board.add_road(6,17-i)
    for i in range (3):
        peli.board.add_road(6+i,1)
    for i in range(19):
        peli.board.add_road(9, 1+i)
    
def spawn_enemy(name,hp,speed,start):
    global enemycount
    
    enemies[enemycount]=Enemy(name+(" ")+str(enemycount),hp,speed,start,enemycount)
    
    enemycount=enemycount+1
    
def add_tower(a,price,power,myrange,speed):
    global towercount
    global money
    if not (isinstance(peli.board.get_spot(int(a[1]/50),int(a[0]/50)),Road)):
        if not (isinstance(peli.board.get_spot(int(a[1]/50),int(a[0]/50)),Tower)):
            if(money<price):
                new_text("Not enough money")
            else:
                new_text(peli.board.add_tower(int(a[1]/50), int(a[0]/50),price,power,myrange,towercount,speed,money))
                towers[towercount]=peli.board.get_spot(int(a[1]/50), int(a[0]/50))
                money-=price
                towercount+=1
        else:
            new_text("Can't build on another tower")
    else:
        new_text("Can't build on road")

    
    
def remove_tower(a):
    global towercount
    global money
    if  (isinstance(peli.board.get_spot(int(a[1]/50), int(a[0]/50)),Tower)):
        del towers[peli.board.get_spot(int(a[1]/50),int(a[0]/50)).get_index()]
        money+=int(0.5*(peli.board.get_spot(int(a[1]/50), int(a[0]/50)).price))
    new_text(peli.board.remove_tower(int(a[1]/50), int(a[0]/50)))
    
    
    
          
def print_stats():
    #pygame.draw.rect(screen,color,(850,610,125,80),0)
    teksti2="Time : "+str(int(time))
    teksti="Money: "+str(int(money))
    font=pygame.font.Font("mono.ttf",12)
    text=font.render(teksti,1,(10,10,10))
    text2=font.render(teksti2,1,(10,10,10))
    screen.blit(text,(850,610))
    screen.blit(text2,(850,625))
    
def shoot_towers():
    for i in towers:
        if ((pygame.time.get_ticks()/1000)-towers[i].lastshot>(2/towers[i].speed)):
            towers[i].shoot(enemies,pygame.time.get_ticks()/1000)
            
def move_enemies(enemies):
    global money
    for i in enemies:
        if (enemies[i]!=None):
            if(enemies[i].is_alive()):
                
                if(time>enemies[i].prev_time+enemies[i].get_timetonext()):
                    

                    enemies[i].move(time)
                    #enemies[i].shot(10)
                    
                    enemies[i].prev_time+=enemies[i].get_timetonext()
            else:
                money+=enemies[i].price
                enemies[i]=None
make_road()


clock=pygame.time.Clock()
    
logo = pygame.image.load("logo32x32.png")
torni=pygame.image.load("cannon2.png")
boom=pygame.image.load("boom.png")
boom_s=pygame.image.load("boom_small.png")
tie=pygame.image.load("road.png")
tie_start=pygame.image.load("road_start.png")
tie_goal=pygame.image.load("road_goal.png")
maa=pygame.image.load("empty.png")
bugu=pygame.image.load("tank_u.png")


pygame.display.set_icon(logo)
pygame.display.set_caption("Tower defense")

size=1000
    
    # create a surface on screen that has the size of 240 x 180
screen_width=size
screen_height=size-300
screen = pygame.display.set_mode((screen_width,screen_height))



screen.fill(color)
    



#spawn_enemy("vihu", 100, 10,start)


    
pygame.display.flip()

running=True

while running:
    time=pygame.time.get_ticks()/1000
    a=(pygame.mouse.get_pos())
    if pygame.mouse.get_pressed()==(1,0,0):
        if(a[1]<=600):
            add_tower(a, 100, 10, 5, 10)
            #new_text(peli.board.add_tower(int(a[1]/50), int(a[0]/50),100,5,5))
    if pygame.mouse.get_pressed()==(0,0,1):
        if(a[1]<=600):
            remove_tower(a)
            spawn_enemy("Baddie", 100, 10*randint(1,2), start)
    
    for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                
    if running:      
        update_screen()
    #clock.tick(30)
    
    
    #if((time*1000)%100==0):
        #done=True
    #spawn_enemy("name", 100, 1, start)
        
    shoot_towers()
    move_enemies(enemies)
    
    
    
    
