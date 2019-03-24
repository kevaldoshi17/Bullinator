import pygame
from math import pi
import random
import requests
import json
import time
# Initialize the game engine
pygame.init()




# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [1920, 1080]
screen = pygame.display.set_mode(size)
#pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.Font(None,80)
myfont2 = pygame.font.Font(None,30)
bias = 25
bias2 = 5
#print(pygame.font.get_Sysfonts())
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
c = 0
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background

    r = requests.get("https://4e3f6147.ngrok.io/data")
    print(r.content)
    Data = r.json()
    kc = int(Data['keval_count'])
    ac = int(Data['akash_count'])
    pc = int(Data['anthony_counut'])
    sc = int(Data['safin_count'])


    screen.fill(BLACK)
    textsurface = myfont.render('BULLINATOR', False, (249, 215, 79))
    screen.blit(textsurface,(790,40))
    
    # Draw a circle
    pygame.draw.line(screen,(0,0,0),[60,250],[100,350],4)

    #######Keval
    pygame.draw.circle(screen, (0+kc*20,0,250-kc*40), [160, 250], 80 + kc*10)
    textsurface = myfont2.render('Keval', True, (249, 215, 79))
    screen.blit(textsurface,(160-bias,250-bias2))


    #######Safin
    pygame.draw.circle(screen, (0+sc*20,0,250-sc*40), [400, 650], 80 + sc*10)
    textsurface = myfont2.render('Safin', True, (249, 215, 79))
    screen.blit(textsurface,(400-bias,650-bias2))
    

    #######Anthony
    pygame.draw.circle(screen, (0+ac*20,0,250-ac*40), [780, 350], 80 + ac*10 )
    textsurface = myfont2.render('Anthony', True, (249, 215, 79))
    screen.blit(textsurface,(780-bias-10,350-bias2))

    #######Akash
    pygame.draw.circle(screen, (0+pc*20,0,250-pc*40), [1000, 850], 80 + pc*10)
    textsurface = myfont2.render('Akash', True, (249, 215, 79))
    screen.blit(textsurface,(1000-bias,850-bias2))
    
    
    #############Demo
    pygame.draw.circle(screen, (0,0,250), [1400, 250], 80)
    textsurface = myfont2.render('Tony', True, (249, 215, 79))
    screen.blit(textsurface,(1400-bias,250-bias2))


    pygame.draw.circle(screen, (0,0,250), [1700, 800], 80)
    textsurface = myfont2.render('David', True, (249, 215, 79))
    screen.blit(textsurface,(1700-bias,800-bias2))


    #pygame.draw.circle(screen, (0+c,0,250-c), [300, 650], 80)


    time.sleep(3.5)
    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()