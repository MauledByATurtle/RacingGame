"""
This is the start of a racing game!

TODO:
    - Menu

- KENT 'TURTLE' NEX
- Last Updated - March 2nd, 2015
"""

##############################
#          IMPORTS           #
##############################

import pygame
import keyboard_mouse_Class
import global_Module
import menu_Class
import car_Class
from pygame.locals import *

##############################
#          GLOBALS           #
##############################
#Globals
INT_SIZE = INT_WIDTH, INT_HEIGHT = global_Module.screen_size  # This is the size of the screen
FPS = 180  # FPS

##############################
#          FUNCTIONS         #
##############################




##############################
#            MAIN            #
##############################
# This is the main function of the program
def main():

    ##############################
    #     M    VARIABLES         #
    ##############################
    # Color
    colors = global_Module.colors  # Gets the colors from the globals
    game_loop = True  # Used to stop the game when you want it over
    menu_dict = {'Start' : (INT_WIDTH / 2, (INT_HEIGHT / 6) * 3),
                 'Multi-player' : (INT_WIDTH / 2, (INT_HEIGHT / 6) * 4),
                 'Quit' : (INT_WIDTH / 2 , (INT_HEIGHT / 6) * 5)}

    ##############################
    #     M       INIT           #
    ##############################
    pygame.init()  # inits
    fps_clock = pygame.time.Clock()  # sets the framerate clock
    win_screen_obj = pygame.display.set_mode(INT_SIZE)  # sets the display
    pygame.display.set_caption('Racing Game')  # sets the caption for the display
    userKeyboard = keyboard_mouse_Class.Keyboard()  # All keyboard and mouse are handled by this
    main_menu = menu_Class.Menu(win_screen_obj, fps_clock, menu_dict, "ULTIMATE RACING BUTLER SIMULATOR 2015")

    player_sprite_group = pygame.sprite.Group()
    player_car = car_Class.Car()
    player_sprite_group.add(player_car)

    ##############################
    #    M    MENU CLASS         #
    ##############################

    #main_menu.main()

    ##############################
    #     M    MAIN LOOP         #
    ##############################
    while game_loop:  # Game loop

        # Fetch info
        keys = userKeyboard.update()  # Fetches keyboard and mouse inputs

        # Updates
        win_screen_obj.fill(colors['white'])  # sets the screen color to white

        player_sprite_group.draw(win_screen_obj)
        player_sprite_group.update(keys)

        fps_clock.tick(FPS)  # This sets the block at the fps
        pygame.display.update()  # This updates the screen

##############################
#            START           #
##############################

# if the program is launched by itself then it runs main
if __name__ == '__main__':
    main()