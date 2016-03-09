# import the pygame module, so you can use it
import pygame

# define a main function
def main():
    
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    
    
    
    
    # create a surface on screen that has the size of 240 x 180
    screen_width=480
    screen_height=360
    screen = pygame.display.set_mode((screen_width,screen_height))
    
    start=pygame.image.load("start_button.png")
    startp=pygame.image.load("start_button_pressed.png")
    settings=pygame.image.load("settings_button.png")
    settingsp=pygame.image.load("settings_button_pressed.png")
    screen.fill((200,191,231))
    
    startpos=((screen_width/3)-50,(screen_height/2)-25)
    settingspos=(2*(screen_width/3)-50,(screen_height/2)-25)
    screen.blit(start,(startpos[0],startpos[1]))
    screen.blit(settings,(settingspos[0],startpos[1]))
    pygame.display.flip()
    

    clicked=False
    # define a variable to control the main loop
    running = True
    
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        a=(pygame.mouse.get_pos())
        
        #if(pygame.mouse.get_rel()[0]!=0 or pygame.mouse.get_rel()[1]!=0):
            #print(a)
        
        if(a[0]>(startpos[0]) and a[0]<startpos[0]+100 and a[1]>startpos[1] and a[1]<startpos[1]+50):
            
            if pygame.mouse.get_pressed()==(1,0,0):
                clicked=True
                screen.blit(startp,((startpos[0],startpos[1])))
            if pygame.mouse.get_pressed()==(0,0,0) and clicked:
                clicked=False
                screen.blit(start,((startpos[0],startpos[1])))

            
            pygame.display.flip()
        elif(a[0]>(settingspos[0]) and a[0]<settingspos[0]+100 and a[1]>settingspos[1] and a[1]<settingspos[1]+50):
            
            if pygame.mouse.get_pressed()==(1,0,0):
                clicked=True
                screen.blit(settingsp,((settingspos[0],settingspos[1])))
            if pygame.mouse.get_pressed()==(0,0,0) and clicked:
                clicked=False
                screen.blit(settings,((settingspos[0],settingspos[1])))

            
            pygame.display.flip()
        else:
            screen.blit(start,((startpos[0],startpos[1])))
            screen.blit(settings,((settingspos[0],settingspos[1])))
            pygame.display.flip()

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
    
             
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
