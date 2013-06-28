# Clean code TTT

# import modules
import os
import sys
import pygame
import window_handler

# pygame specific locals/constants
from pygame.locals import *

# initializations
pygame.init()

# we'll call the window "canvas"
canvas = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Tic Tac Toe")

# colours and fonts (objects)
newgamefont = pygame.font.Font(pygame.font.match_font('timesnewroman'), 18)
XorO_font = pygame.font.Font(pygame.font.match_font('timesnewroman'), 180)

XorO_color = pygame.Color(255, 0, 0)
white_color = pygame.Color(255, 255, 255)

# score
comp_score = 0
player_score = 0

def newgame():
    global computers_turn, currentgrid, players_turn
    
    currentgrid = ["", "", "", "", "", "", "", "", ""] 
    computers_turn = False
    players_turn = True

# Start a new game
newgame()

def main():
    # initialize loop until quit variable
    running = True
    
    # create our FPS timer clock
    clock = pygame.time.Clock()    

#---------------------------Frame is now Running-----------------------------------------
    
    # doing the infinte loop until quit -- the game is running
    while running:
        
        # event queue iteration
        for event in pygame.event.get():
            
            # window GUI ('x' the window)
            if event.type == pygame.QUIT:
                running = False

            # input - key and mouse event handlers
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                # just respond to left mouse clicks
                if pygame.mouse.get_pressed()[0]:
                    window_handler.mc_handler(pygame.mouse.get_pos(), players_turn, computers_turn, currentgrid)
                    
            elif event.type == pygame.KEYDOWN:
                window_handler.kd_handler(event.key)

         
        # the call to the draw handler
        window_handler.draw_handler(canvas, white_color, newgamefont, XorO_color, XorO_font, currentgrid)
        
        # FPS limit to 60 -- essentially, setting the draw handler timing
        # it micro pauses so while loop only runs 60 times a second max.
        clock.tick(60)
        
#-----------------------------Frame Stops------------------------------------------

    # quit game -- we're now allowed to hit the quit call
    pygame.quit ()

# this calls the 'main' function when this script is executed
# could be thought of as a call to frame.start() of sorts
if __name__ == '__main__': main() 

