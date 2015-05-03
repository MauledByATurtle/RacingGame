"""
    This class is used to make menus.
    You send it 3 args.
        - The screen/surface
        - A clock
        - A dictionary of the locations
        and names of the buttons
        ex. menu_dict = {'Start' : (100,100)}
    You also need a keyboard_mouse_Class to
    take care of the key inputs/mouse pos.
    Can be done without, just edit
    keys['mousePos'] to pygame.mouse.get_pos()
"""

import pygame
import global_Module
import keyboard_mouse_Class
from pygame.locals import *


class Menu():

    def __init__(self, surface, clock,  menu_dict, title):  # Loads the settings into the menu - Takes Surface and menu_dict of locs
        self.surface = surface  # This is so we can show the menu on the screen
        self.clock = clock
        self.title = title
        self.box_size = 200
        self.text_font = pygame.font.SysFont(None, (self.box_size/5))
        self.title_font = pygame.font.SysFont(None, 60)
        self.title_color = global_Module.colors['black']
        self.userKeys = keyboard_mouse_Class.Keyboard()
        self.keys = {}
        self.menu_dict = menu_dict   # This is so we know where to place the buttons
        self.button_sprite_list = pygame.sprite.Group()  # Creates the sprite group
        self.quit = False
        self.title_pos = (self.get_font_pos(),(global_Module.screen_size[1] / 6))

    def get_font_pos(self):
        font_size = self.title_font.size(self.title)
        return (global_Module.screen_size[0] - font_size[0]) / 2

    def load(self):  # This will load the buttons and make them into a sprite list
        for i in self.menu_dict:  # This checks all the buttons you want and inter's throught them to make them.
            # i = text on the button and menu_dict[i] = pos of button
            menu_button = MenuButton(i, self.menu_dict[i], self.text_font, self.box_size)
            self.button_sprite_list.add(menu_button)

    def update(self):
        title = self.title_font.render(self.title, 0, self.title_color)
        self.surface.blit(title, self.title_pos)

    def main(self):  # This is the main for the menu. If you run this it will create the menu and work with that.

        self.load()  # makes the buttons

        while not self.quit:  # Closes the menu

            self.keys = self.userKeys.update()

            self.surface.fill(global_Module.colors['white'])

            for i in self.button_sprite_list:
                if i.rect.collidepoint(self.keys['mousePos']):
                    i.update_color(global_Module.colors['blue'])
                else: i.update_color(global_Module.colors['red'])

            self.update()

            self.button_sprite_list.draw(self.surface)
            self.button_sprite_list.update(self.surface)

            self.clock.tick(30)
            pygame.display.update()


# Class for the menubutton
class MenuButton(pygame.sprite.Sprite):  # This is a child of pygame.sprite.Sprite()

    def __init__(self, text , pos, font, size):  # Inits the class

        pygame.sprite.Sprite.__init__(self)  # Inits sprite.Sprite()
        self.color = global_Module.colors['red']  # Sets Color
        self.font_text = text
        self.width = size  # Sets Width
        self.height = size/2  # Sets Height
        self.image = pygame.Surface([self.width,self.height])  # Sets the image to surface
        self.image.fill(self.color)  # Fills the image with color!
        self.rect = self.image.get_rect()  # gets the rect from the image
        self.rect.centerx , self.rect.centery = self.pos = pos # Sets x and y
        self.font = font  # Creates the font for use in the buttons
        self.font_color = global_Module.colors['black']
        self.font_pos = self.get_font_pos()

    def update(self, surface):  # This is unused atm
        font_draw = self.font.render(self.font_text, 0, self.font_color)
        surface.blit(font_draw, (self.font_pos))

    def update_color(self, color):
        self.color = color
        self.image.fill(self.color)

    def get_font_pos(self):
        font_size = self.font.size(self.font_text)
        font_distx = self.width - font_size[0]
        font_disty = self.height - font_size[1]
        font_loc = ((self.rect.x + (font_distx / 2)), (self.rect.y + (font_disty /2)))
        return font_loc




