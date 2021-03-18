import pygame

#constant variables
SCREEN_SIZE = (1080, 1920)
DARK_GREY = (50, 50, 50)



#init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Amanda\'s Platform Game')

running = True
while running:
#game loop

    #input
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
           
            running = False

    #update

    #draw
    screen.fill(DARK_GREY)     #type an rgb value in bracket
    pygame.display.flip()       #one buffer while another is being drawn, the frames flip which prevents tearing

#quit
pygame.quit()
