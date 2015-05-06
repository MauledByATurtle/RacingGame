import pygame
import global_Module
import math


class Car(pygame.sprite.Sprite):  # This class will handle everything that the car does

    def __init__(self):  # Init's the car class
        pygame.sprite.Sprite.__init__(self)  # Init's the sprite class

        self.scale = 50  # Size of the car. Increasing will increase car size

        # stores all the different cars images
        self.car_image = {'car' : self.scale_size(pygame.image.load('red_car.png'), self.scale),
                          'car_left' : self.scale_size(pygame.image.load('red_car_left.png'), self.scale),
                          'car_right' : self.scale_size(pygame.image.load('red_car_right.png'), self.scale)}

        self.image = self.car_image['car']  # Image is the main car image

        self.rect = self.image.get_rect()  # Gets the rect of the car
        self.rect.x = self.rect.y = 200.00  # Relocate the car's x and y

        self.keys_dict = {}  # Keys dictionary

        self.velocity = 0
        self.acceleration = 0.1
        self.degree = 0
        self.turn_speed = 2

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

        self.moving()
        #self.move_dir()  # Changes the direction that the cars tires are facing

    def moving(self):

        # if self.keys_dict['W']:
        #     self.velocity -= self.acceleration
        # if self.keys_dict['S']:
        #     self.velocity += self.acceleration
        # if not self.keys_dict['W'] and not self.keys_dict['S']:
        #     if self.velocity > 0:
        #         self.velocity += self.acceleration
        #     elif self.velocity < 0:
        #         self.velocity -= self.acceleration

        if self.keys_dict['W']:
            self.velocity = -10
        if self.keys_dict['S']:
            self.velocity = 10
        if self.keys_dict['W'] == False and self.keys_dict['S'] == False:
            self.velocity = 0

        if self.keys_dict['A'] and self.velocity != 0:
            self.degree += self.turn_speed
            self.image, self.rect = self.rotate_car(self.car_image['car_left'], self.degree)
        if self.keys_dict['D'] and self.velocity != 0:
            self.degree -= self.turn_speed
            self.image, self.rect = self.rotate_car(self.car_image['car_right'], self.degree)
        elif not self.keys_dict['D'] and not self.keys_dict['A']:
            self.image, self.rect = self.rotate_car(self.car_image['car'], self.degree)

        if self.degree >= 360:
            self.degree = 360 % self.degree
        elif self.degree < 0:
            self.degree = 360 - abs(self.degree)

        print self.degree

        self.adding_velocity()

    def adding_velocity(self):

        cos_float = math.cos(math.radians(self.degree))
        y_velocity = cos_float * self.velocity
        sin_float = math.sin(math.radians(self.degree))
        x_velocity = sin_float * self.velocity

        self.rect.x = float(self.rect.x) + x_velocity
        self.rect.y = float(self.rect.y) + y_velocity

        self.debug = 'Degree = %r, X = %r, Y = %r' % (self.degree, self.rect.x, self.rect.y)

    def rotate_car(self, image, degree):

        new_image = pygame.transform.rotate(image, degree)
        new_rect = new_image.get_rect(center=self.rect.center)

        return new_image, new_rect

    def scale_size(self, image, size):  # Scales the car size
        return pygame.transform.scale(image, (size, size))  # returns the scaled car


