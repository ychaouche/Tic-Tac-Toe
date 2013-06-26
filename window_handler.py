##import the variables
import TTT
import pygame

# TTT border
left_edge = 50
right_edge = 530
top_edge = 60
bottom_edge = 460

# horizontal lines
first_row = 190
second_row = 330

# vertical lines
first_col = 200
second_col = 375



def draw_handler(canvas, line_color, font):

    # clear canvas -- create the grid
    canvas.fill((0, 0, 0))
    
    # Horizontal lines
    pygame.draw.line(canvas, color, (left_edge, first_row), (right_edge, first_row), 12)
    pygame.draw.line(canvas, color, (left_edge, second_row), (right_edge, second_row), 12)
    # Vertical lines
    pygame.draw.line(canvas, color, (first_col, top_edge), (first_col, bottom_edge), 12)
    pygame.draw.line(canvas, color, (second_col, top_edge), (second_col, bottom_edge), 12)
    # Text displaying score and reset option
    newgame_key = font.render("N = New Game", True, color)
    

    # update the display
    pygame.display.update()
    
##    canvas.draw_text("Computers wins: ", (20, 25), 32, "White")
##    canvas.draw_text("Players wins: " , (380, 25), 32, "White")
##

##def kd_handler(key):
##    if pygame.K_n == key:
##        init()
##    
###def mc_handler(pos):
##    
