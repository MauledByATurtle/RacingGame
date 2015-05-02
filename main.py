import pygame
from pygame.locals import *

#Globals
INT_SIZE = INT_WIDTH, INT_HEIGHT = (1280,720)  # This is the size of the screen
FPS = 180  # FPS

# this is the main function of the program
def main():

    colors = {'white' : pygame.Color(255,255,255),
              'black' : pygame.Color(0,0,0)}

    pygame.init()  # inits
    fps_clock = pygame.time.Clock()  # sets the framerate clock
    win_screen_obj = pygame.display.set_mode(INT_SIZE)  # sets the display
    pygame.display.set_caption('Level Creator')  # sets the caption for the display

    while True:  # Game loop

        for event in pygame.event.get():  # Checks all the events to see if anything is happening
            if event.type == QUIT:  # If you close it then type QUIT happens
                raise SystemExit, 'CLOSED'
            if event.type == KEYDOWN:  # Any keys that are pressed
                if event.key == K_ESCAPE:  # Closes it if you press escape
                    raise SystemExit, 'ESCAPE'


        win_screen_obj.fill(colors['white'])  # sets the screen color to white
        fps_clock.tick(FPS)  # This sets the block at the fps
        pygame.display.update()  # This updates the screen



# if the program is launched by itself then it runs main
if __name__ == '__main__':
    main()