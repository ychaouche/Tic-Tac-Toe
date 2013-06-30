# Clean code TTT

# import modules
import os
import sys
import pygame
import window_handler
import computer_AI
import possible_moves

# pygame specific locals/constants
from pygame.locals import *

# initializations
pygame.init()

# we'll call the window "canvas"
canvas = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Tic Tac Toe")

# colours and fonts (objects)
wordfont = pygame.font.Font(pygame.font.match_font('timesnewroman'), 18)
XorO_font = pygame.font.Font(pygame.font.match_font('timesnewroman'), 180)

XorO_color = pygame.Color(255, 0, 0)
white_color = pygame.Color(255, 255, 255)

def newgame():
    global currentgrid
    
    currentgrid = ["", "", "", "", "", "", "", "", ""] 
    possible_moves.comps_turn = True
    possible_moves.plyrs_turn = False

# keydown handler -- 
def kd_handler(key):
    if pygame.K_n == key:
        newgame()

# Start a new game
newgame()

def main():
    global comps_turn, plyrs_turn
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
                if pygame.mouse.get_pressed()[0] and possible_moves.plyrs_turn:
                    currentgrid[window_handler.mc_handler(pygame.mouse.get_pos(), possible_moves.plyrs_turn, possible_moves.comps_turn, currentgrid)] = window_handler.O
                    possible_moves.switch_turns()
                    
            elif event.type == pygame.KEYDOWN:
                kd_handler(event.key)

        # Computers go
        if possible_moves.comps_turn:
            currentgrid[computer_AI.computers_play(currentgrid)] = "X"
            possible_moves.switch_turns()
            if window_handler.is_winner(currentgrid, window_handler.X):
                window_handler.scorekeeper(window_handler.X)
                
            
        # the call to the draw handler
        window_handler.draw_handler(canvas, white_color, wordfont, XorO_color, XorO_font, currentgrid, possible_moves.comps_turn, possible_moves.plyrs_turn)

        # FPS limit to 60 -- essentially, setting the draw handler timing
        # it micro pauses so while loop only runs 60 times a second max.
        clock.tick(60)
        
#-----------------------------Frame Stops------------------------------------------

    # quit game -- we're now allowed to hit the quit call
    pygame.quit ()

# this calls the 'main' function when this script is executed
# could be thought of as a call to frame.start() of sorts
if __name__ == '__main__': main() 

