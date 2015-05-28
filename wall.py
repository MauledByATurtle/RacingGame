import global_Module
import pygame
import random


class wall(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.size = 21
        self.image = pygame.Surface((self.size,self.size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,global_Module.screen_size[0])
        self.rect.y = random.randint(0,global_Module.screen_size[0])
        self.color = global_Module.colors['blue']

        self.image.fill(self.color)