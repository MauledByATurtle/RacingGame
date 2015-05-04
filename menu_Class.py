"""
    This class is used to make menus.
    You send it 3 args.
        - The screen/surface
        - A clock
        - A dictionary of the locations
        and names of the buttons
        ex. menu_dict = {'Start' : (100,100)}
    You also need a keyboard_mouse_Class to
    take care of the key inputs/mouse pos and
    global file of all the colors.
    Can be done without, just edit
    keys['mousePos'] to pygame.mouse.get_pos()
    and the colors to pygame.Color(x,x,x)
"""

import pygame
import global_Module
import keyboard_mouse_Class
from pygame.locals import *


class Menu():  # This runs the menu, so you can create multiple menus easily

    def __init__(self, surface, clock,  menu_dict, title):  # Loads the settings into the menu - Takes Surface and menu_dict of locs
        self.surface = surface  # This is so we can show the menu on the screen
        self.clock = clock  # This gets the clock so we can have a game loop inside here
        self.quit = False  # Setting this to true will end the menu

        # Title properties, can be changed
        self.title = title  # gets the title of the menu that you sent it
        self.title_font = pygame.font.SysFont(None, 60)  # Sets the font to sysFont, Can be changed
        self.title_color = global_Module.colors['black']  # Sets the color of the title
        self.title_pos = (self.get_font_pos(),(global_Module.screen_size[1] / 6))  # Sets the pos of the title.

        self.box_size = 200  # This is the length of the box. You can change this for a different size box
        self.text_font = pygame.font.SysFont(None, (self.box_size/5))  # Sets the font of the box text, Can be changed

        self.keys = {}  # empty keys dict. Updated later to hold keyboard keys
        self.menu_dict = menu_dict   # This is so we know where to place the buttons
        self.button_sprite_list = pygame.sprite.Group()  # Creates the sprite group
        self.userKeys = keyboard_mouse_Class.Keyboard()  # Creates the keyboard class. Used for all keyboard and mouse

    def get_font_pos(self):  # Get the x pos for the font so its centered
        font_size = self.title_font.size(self.title)
        return (global_Module.screen_size[0] - font_size[0]) / 2

    def load(self):  # This will load the buttons and make them into a sprite list
        for i in self.menu_dict:  # This checks all the buttons you want and inter's through them to make them.
            # i = text on the button, menu_dict[i] = pos of button, self.text_font is the font obj and box_size is size
            menu_button = MenuButton(i, self.menu_dict[i], self.text_font, self.box_size)
            self.button_sprite_list.add(menu_button)

    def update(self):  # This makes a surface for the font then blits it onto the main
        title = self.title_font.render(self.title, 0, self.title_color)
        self.surface.blit(title, self.title_pos)

    def main(self):  # This is the main for the menu. If you run this it will create the menu and work with that.

        self.load()  # makes the buttons

        while not self.quit:  # Closes the menu

            self.keys = self.userKeys.update()  # Gets the users key/mouse inputs

            self.surface.fill(global_Module.colors['white'])  # background color

            for i in self.button_sprite_list:  # This goes through the buttons checking if they've been pressed
                if i.rect.collidepoint(self.keys['mousePos']):  # If the mouse is over the button
                    i.update_color(global_Module.colors['blue'])  # Change the color of the button
                    if self.keys['mouseLeft']:  # If the mouse is clicked on the button
                        if i.font_text == 'Start':  # and the button name is 'xxxx'
                            self.quit = True  # Then this will happen
                        elif i.font_text == 'Quit':  # if the button is 'xxxx'
                            raise SystemExit, 'Quit ' # then this will happen
                else:
                    i.update_color(global_Module.colors['red'])  # Otherwise, the button is this color

            self.update()  # Blits the title

            self.button_sprite_list.draw(self.surface)  # Draws the buttons
            self.button_sprite_list.update(self.surface)  # Blits the font on the buttons

            self.clock.tick(30)  # FPS clock
            pygame.display.update()  # Screen update


# Class for the menubutton
class MenuButton(pygame.sprite.Sprite):  # This is a child of pygame.sprite.Sprite()

    def __init__(self, text , pos, font, size):  # Inits the class

        pygame.sprite.Sprite.__init__(self)  # Inits sprite.Sprite()
        self.color = global_Module.colors['red']  # Sets Color
        self.width = size  # Sets Width
        self.height = size/2  # Sets Height
        self.image = pygame.Surface([self.width,self.height])  # Sets the image to surface
        self.image.fill(self.color)  # Fills the image with color!
        self.rect = self.image.get_rect()  # gets the rect from the image
        self.rect.centerx , self.rect.centery = self.pos = pos # Sets x and y

        self.font_text = text # sets the font on the button is text from the dict you sent the menu
        self.font = font  # Creates the font for use in the buttons, sent from menu
        self.font_color = global_Module.colors['black']  # sets color from globals
        self.font_pos = self.get_font_pos()  # calls the get_font_pos, which returns the pos for the middle of the but

    def update(self, surface):  # This renders the font
        font_draw = self.font.render(self.font_text, 0, self.font_color)  # Creates the surface of the button
        surface.blit(font_draw, (self.font_pos))  # blits the surface onto the main surface

    def update_color(self, color):  # Changes the color of the button so when you hover over it, it changes
        self.color = color  # sets to the new color
        self.image.fill(self.color)  # fills the button. Without this then you wouldn't see a change

    def get_font_pos(self):  # This function gets the X and Y of the text so its centered on the button
        font_size = self.font.size(self.font_text)  # How much room the font takes up.
        font_distx = self.width - font_size[0]  # How far the text has to be from the x of the button
        font_disty = self.height - font_size[1]  # HO far the text has to be from the y of the button
        font_loc = ((self.rect.x + (font_distx / 2)), (self.rect.y + (font_disty /2)))  # Location of button on screen
        return font_loc  # Returns buttons x and y properties




