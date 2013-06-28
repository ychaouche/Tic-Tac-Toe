##import the variables
import pygame
import Plyr_Comp_options

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

# gridsquare constant
gridsquare_constant = [60, 20]

# game pieces
players_le = "O"
computers_le = "X"

# score
comps_score = 0
players_score = 0

def draw_handler(canvas, white_color, newgamefont, XorO_color, XorO_font, currentgrid):


    # black canvas -- create the grid
    canvas.fill((0, 0, 0))
    
    # Horizontal lines
    pygame.draw.line(canvas, white_color, (left_edge, first_row), (right_edge, first_row), 12)
    pygame.draw.line(canvas, white_color, (left_edge, second_row), (right_edge, second_row), 12)
    # Vertical lines
    pygame.draw.line(canvas, white_color, (first_col, top_edge), (first_col, bottom_edge), 12)
    pygame.draw.line(canvas, white_color, (second_col, top_edge), (second_col, bottom_edge), 12)

    # Text displaying score and reset option
    newgametext = newgamefont.render("N = New Game", True, white_color)
    comp_scoretxt = newgamefont.render("Computer: " + str(comps_score), True, white_color)
    plyr_scoretxt = newgamefont.render("Player: " + str(players_score), True, white_color)

    canvas.blit(comp_scoretxt, (8, 0))
    canvas.blit(plyr_scoretxt, (8, 25))
    canvas.blit(newgametext, (8, 480))

    # draw symbols
    for gridsquare in range(len(currentgrid)):
        XorO = XorO_font.render(currentgrid[gridsquare], True, XorO_color)
        canvas.blit(XorO,(gridsquare_constant[0] + (160 * (gridsquare // 3) ),
                          gridsquare_constant[1] + (140 * (gridsquare % 3 ) )))

    # update the display
    pygame.display.update()
    
def mc_handler(pos, players_turn, computers_turn, currentgrid):

    if pos[0] < first_col and pos[0] > left_edge and players_turn:
        if pos[1] < first_row and pos[1] > top_edge and Plyr_Comp_options.isSpaceFree(currentgrid, 0):
            currentgrid[0] = players_le
            computers_turn = True

