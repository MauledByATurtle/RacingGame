import pygame
import global_Module


class Car(pygame.sprite.Sprite):  # This class will handle everything that the car does



    def __init__(self):  # Init's the car class
        pygame.sprite.Sprite.__init__(self)  # Init's the sprite class

        self.scale = 100  # Size of the car. Increasing will increase car size

        # stores all the different cars images
        self.car_image = {'car' : self.scale_size(pygame.image.load('red_car.png'), self.scale),
                          'car_left' : self.scale_size(pygame.image.load('red_car_left.png'), self.scale),
                          'car_right' : self.scale_size(pygame.image.load('red_car_right.png'), self.scale)}

        self.image = self.car_image['car']  # Image is the main car image

        self.rect = self.image.get_rect()  # Gets the rect of the car
        self.rect.x = self.rect.y = 100  # Relocate the car's x and y

        self.keys_dict = {}  # Keys dictionary

    def update(self, keys):  # This is the main update function
        self.keys_dict = keys  # Gets the keys from the main.py


        self.move_dir()  # Changes the direction that the cars tires are facing

    def move_dir(self):  # This function changes the sprite that's used based on the directions you're pressing

        # This will change the image that is being displayed
        if self.keys_dict['A'] and self.keys_dict['D']:  # If both keys are pressed then its normal sprite
            self.image = self.car_image['car']
        elif self.keys_dict['A']:
            self.image = self.car_image['car_left']
        elif self.keys_dict['D']:
            self.image = self.car_image['car_right']
        else:
            self.image = self.car_image['car']


    def scale_size(self, image, size):  # Scales the car size
        return pygame.transform.scale(image, (size, size))  # returns the scaled car


