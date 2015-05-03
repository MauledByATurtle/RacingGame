import pygame
from pygame.locals import *


# This class handles all the keyboard and mouse input
class Keyboard():

    # This inits the nice long dictionary we have here
    def __init__(self):
        self.keys = {
            'A' : False,
            'B' : False,
            'C' : False,
            'D' : False,
            'E' : False,
            'F' : False,
            'G' : False,
            'H' : False,
            'I' : False,
            'J' : False,
            'K' : False,
            'L' : False,
            'M' : False,
            'N' : False,
            'O' : False,
            'P' : False,
            'Q' : False,
            'R' : False,
            'S' : False,
            'T' : False,
            'U' : False,
            'V' : False,
            'W' : False,
            'X' : False,
            'Y' : False,
            'Z' : False,
            'LSHIFT' : False,
            'SPACE' : False,
            'LEFT' : False,
            'RIGHT' : False,
            'UP' : False,
            'DOWN' : False,
            'mouseLeft' : False,
            'mouseRight' : False,
            'mouseScrollup' : False,
            'mouseScrolldown' : False,
            'mousePos' : (0,0),
            '1' : False,
            '2' : False,
            '3' : False,
            '4' : False,
            '5' : False,
            '6' : False,
            '7' : False,
            '8' : False,
            '9' : False,
            '0' : False,
            'F1': False}


    # this checks for any pygame events such as user input
    def update(self):
        # looping over all the events
        for events in pygame.event.get():
            # This will quit th game if you close it
            if events.type == QUIT: raise SystemExit, "QUIT"
        # KEY DOWN  EVENTS
            if events.type == KEYDOWN:
                if events.key == K_ESCAPE:
                    raise SystemExit, "ESCAPE"
                elif events.key == K_a:
                    self.keys['A'] = True
                elif events.key == K_b:
                    self.keys['B'] = True
                elif events.key == K_c:
                    self.keys['C'] = True
                elif events.key == K_d:
                    self.keys['D'] = True
                elif events.key == K_e:
                    self.keys['E'] = True
                elif events.key == K_f:
                    self.keys['F'] = True
                elif events.key == K_g:
                    self.keys['G'] = True
                elif events.key == K_h:
                    self.keys['H'] = True
                elif events.key == K_i:
                    self.keys['I'] = True
                elif events.key == K_j:
                    self.keys['J'] = True
                elif events.key == K_k:
                    self.keys['K'] = True
                elif events.key == K_l:
                    self.keys['L'] = True
                elif events.key == K_m:
                    self.keys['M'] = True
                elif events.key == K_n:
                    self.keys['N'] = True
                elif events.key == K_o:
                    self.keys['O'] = True
                elif events.key == K_p:
                    self.keys['P'] = True
                elif events.key == K_q:
                    self.keys['Q'] = True
                elif events.key == K_r:
                    self.keys['R'] = True
                elif events.key == K_s:
                    self.keys['S'] = True
                elif events.key == K_t:
                    self.keys['T'] = True
                elif events.key == K_u:
                    self.keys['U'] = True
                elif events.key == K_v:
                    self.keys['V'] = True
                elif events.key == K_w:
                    self.keys['W'] = True
                elif events.key == K_x:
                    self.keys['X'] = True
                elif events.key == K_y:
                    self.keys['Y'] = True
                elif events.key == K_z:
                    self.keys['Z'] = True
                elif events.key == K_LSHIFT:
                    self.keys['LSHIFT'] = True
                elif events.key == K_SPACE:
                    self.keys['SPACE'] = True
                elif events.key == K_LEFT:
                    self.keys['LEFT'] = True
                elif events.key == K_RIGHT:
                    self.keys['RIGHT'] = True
                elif events.key == K_UP:
                    self.keys['UP'] = True
                elif events.key == K_DOWN:
                    self.keys['DOWN'] = True
                elif events.key == K_1:
                    self.keys['1'] = True
                elif events.key == K_2:
                    self.keys['2'] = True
                elif events.key == K_3:
                    self.keys['3'] = True
                elif events.key == K_4:
                    self.keys['4'] = True
                elif events.key == K_5:
                    self.keys['5'] = True
                elif events.key == K_6:
                    self.keys['6'] = True
                elif events.key == K_7:
                    self.keys['7'] = True
                elif events.key == K_8:
                    self.keys['8'] = True
                elif events.key == K_9:
                    self.keys['9'] = True
                elif events.key == K_0:
                    self.keys['0'] = True
                elif events.key == K_F1:
                    self.keys['F1'] = True

        # MOUSE DOWN EVENTS
            if events.type == MOUSEBUTTONDOWN:
                if events.button == 1:
                    self.keys['mouseLeft'] = True
                elif events.button == 3:
                    self.keys['mouseRight'] = True
                elif events.button == 4:
                    self.keys['mouseScrollup'] = True
                elif events.button == 5:
                    self.keys['mouseScrolldown'] = True

        # KEY UP EVENTS
            if events.type == KEYUP:
                if events.key == K_a:
                    self.keys['A'] = False
                elif events.key == K_b:
                    self.keys['B'] = False
                elif events.key == K_c:
                    self.keys['C'] = False
                elif events.key == K_d:
                    self.keys['D'] = False
                elif events.key == K_e:
                    self.keys['E'] = False
                elif events.key == K_f:
                    self.keys['F'] = False
                elif events.key == K_g:
                    self.keys['G'] = False
                elif events.key == K_h:
                    self.keys['H'] = False
                elif events.key == K_i:
                    self.keys['I'] = False
                elif events.key == K_j:
                    self.keys['J'] = False
                elif events.key == K_k:
                    self.keys['K'] = False
                elif events.key == K_l:
                    self.keys['L'] = False
                elif events.key == K_m:
                    self.keys['M'] = False
                elif events.key == K_n:
                    self.keys['N'] = False
                elif events.key == K_o:
                    self.keys['O'] = False
                elif events.key == K_p:
                    self.keys['P'] = False
                elif events.key == K_q:
                    self.keys['Q'] = False
                elif events.key == K_r:
                    self.keys['R'] = False
                elif events.key == K_s:
                    self.keys['S'] = False
                elif events.key == K_t:
                    self.keys['T'] = False
                elif events.key == K_u:
                    self.keys['U'] = False
                elif events.key == K_v:
                    self.keys['V'] = False
                elif events.key == K_w:
                    self.keys['W'] = False
                elif events.key == K_x:
                    self.keys['X'] = False
                elif events.key == K_y:
                    self.keys['Y'] = False
                elif events.key == K_z:
                    self.keys['Z'] = False
                elif events.key == K_LSHIFT:
                    self.keys['LSHIFT'] = False
                elif events.key == K_SPACE:
                    self.keys['SPACE'] = False
                elif events.key == K_LEFT:
                    self.keys['LEFT'] = False
                elif events.key == K_RIGHT:
                    self.keys['RIGHT'] = False
                elif events.key == K_UP:
                    self.keys['UP'] = False
                elif events.key == K_DOWN:
                    self.keys['DOWN'] = False
                elif events.key == K_1:
                    self.keys['1'] = False
                elif events.key == K_2:
                    self.keys['2'] = False
                elif events.key == K_3:
                    self.keys['3'] = False
                elif events.key == K_4:
                    self.keys['4'] = False
                elif events.key == K_5:
                    self.keys['5'] = False
                elif events.key == K_6:
                    self.keys['6'] = False
                elif events.key == K_7:
                    self.keys['7'] = False
                elif events.key == K_8:
                    self.keys['8'] = False
                elif events.key == K_9:
                    self.keys['9'] = False
                elif events.key == K_0:
                    self.keys['0'] = False
                elif events.key == K_F1:
                    self.keys['F1'] = False

        # MOUSE UP EVENT
            if events.type == MOUSEBUTTONUP:
                if events.button == 1:
                    self.keys['mouseLeft'] = False
                elif events.button == 3:
                    self.keys['mouseRight'] = False

        # MOUSE MOVE EVENT
            if events.type == MOUSEMOTION:
                self.keys['mousePos'] = pygame.mouse.get_pos()

        # RETURNS THE KEYS DICT
        return self.keys
