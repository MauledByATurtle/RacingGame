import pygame
import global_Module
import math


class Car(pygame.sprite.Sprite):  # This class will handle everything that the car does

    def __init__(self):  # Init's the car class
        pygame.sprite.Sprite.__init__(self)  # Init's the sprite class

        self.scale = 50  # Size of the car. Increasing will increase car size

        # stores all the different cars images
        self.car_image = {'car' : self.scale_size(pygame.image.load('red_car1.png'), self.scale),
                          'car_left' : self.scale_size(pygame.image.load('red_car_left1.png'), self.scale),
                          'car_right' : self.scale_size(pygame.image.load('red_car_right1.png'), self.scale)}

        self.image = self.car_image['car']  # Image is the main car image

        self.rect = self.image.get_rect()  # Gets the rect of the car
        self.rect.x = self.rect.y = 200.00  # Relocate the car's x and y

        self.x = self.rect.y  # This sets the self.x to the rect.x
        self.y = self.rect.x  # this sets the self.y to the rect.y
        self.velocity = 0  # Velocity
        self.degree = 0

        self.keys_dict = {}  # Keys dictionary

        self.acc = 0.1
        self.de_acc = 0.05
        self.rev_acc = 0.5  # This gets multiplied by self.acc so 1 == normal acc, .5 == half normal acc
        self.max_vel = 2
        self.turn_speed = 1

        self.font = pygame.font.SysFont(None, 36)
        self.debug = ''


    def update(self, keys, surface):  # This is the main update function
        self.keys_dict = keys  # Gets the keys from the main.py

        font_render = self.font.render(self.debug, 1, pygame.Color(0,0,0))

        if self.keys_dict['R']:
            if self.degree == 0:
                self.degree = 1
            elif self.degree == 90:
                self.degree = 180
            elif self.degree == 180:
                self.degree = 270
            elif self.degree == 270:
                self.degree = 0
            else: self.degree = 0
            self.keys_dict['R'] = False


        surface.blit(font_render, (0,0))

        self.moving()  # Checks to see if the cars moving

    def moving(self):

        if self.keys_dict['W']:
            self.apply_acc('Forward')
        if self.keys_dict['S']:
            self.apply_acc('Backward')
        if not self.keys_dict['W'] and not self.keys_dict['S']:
            self.apply_acc()

        if self.keys_dict['A']:
            self.rotate_car(self.car_image['car_left'], self.degree)
            if self.velocity != 0:
                if self.keys_dict['S'] and self.velocity > 0:
                    self.degree -= self.turn_speed
                else: self.degree += self.turn_speed
        if self.keys_dict['D']:
            self.rotate_car(self.car_image['car_right'], self.degree)
            if self.velocity != 0:
                if self.keys_dict['S'] and self.velocity > 0:
                    self.degree += self.turn_speed
                else: self.degree -= self.turn_speed
        elif not self.keys_dict['D'] and not self.keys_dict['A']:
            self.rotate_car(self.car_image['car'], self.degree)

        self.degree = self.degree_check(self.degree)
        self.adding_velocity()  # Calculates velocity and applies them to x and y

    def apply_acc(self, acc_dir = 'None'):

        if acc_dir == 'Forward' and self.velocity > (self.max_vel * -1):
            self.velocity -= self.acc
            if self.velocity < (self.max_vel * -1):
                self.velocity = self.max_vel * -1

        elif acc_dir == 'Backward' and self.velocity < self.max_vel*self.rev_acc:
            self.velocity += self.acc*self.rev_acc
            if self.velocity > self.max_vel*self.rev_acc:
                self.velocity = self.max_vel*self.rev_acc

        elif acc_dir == 'None':
            if self.velocity > 0:
                self.velocity -= self.de_acc
            elif self.velocity < 0:
                self.velocity += self.de_acc

        if acc_dir == 'None' and abs(self.velocity) <= self.de_acc:
            self.velocity = 0


    def degree_check(self, degree):  # This sets the degree to 0 if its 360 and set it to 359 if its -1

        new_degree = degree

        if degree >= 360:  # If degree is > then 359 then you set it to 0 + whatever was left
            new_degree = 360 % degree
        elif degree < 0:  # If degree is < then 0 you set it to 359 - whatever was left
            new_degree = 360 - abs(degree)

        return new_degree  # Returns the new degree. 0-359

    def adding_velocity(self):  # This function is used to add the velocity to the cars x and y

        cos_float = math.cos(math.radians(self.degree))  # This gets the cars y velocity
        y_velocity = cos_float * self.velocity
        sin_float = math.sin(math.radians(self.degree))  # This gets the cars x velocity
        x_velocity = sin_float * self.velocity

        self.x += x_velocity  # Without this the numbers would be rounded
        self.y += y_velocity  # ^

        self.rect.x = self.x  # This sets the x and y to the rect
        self.rect.y = self.y

    def rotate_car(self, image, degree):  # Rotates the car's image

        old_rect = self.rect  # the old rect is used to get the old rect.center so it spins on the center
        new_image = pygame.transform.rotate(image, degree)  # Actually rotates the image
        new_rect = new_image.get_rect()  # Gets the rect of the new image
        new_rect.center = old_rect.center  # Sets the new center of the old rect

        self.image = new_image  # Sets self image to new image
        self.rect = new_rect  # Sets self rect to new rect

        # Because new_rect.x is rounded and I had to set self.x
        # to it I got the remainder off of self.x and added it to it
        if math.trunc(self.x) != 0:
            self.x = new_rect.x + (self.x % math.trunc(self.x))
        else: self.x = new_rect.x + self.x
        if math.trunc(self.y) != 0:
            self.y = new_rect.y + (self.y % math.trunc(self.y))
        else: self.y = new_rect.y + self.y

    def scale_size(self, image, size):  # Scales the car size
        return pygame.transform.scale(image, (int(size/1.5), size))  # returns the scaled car


