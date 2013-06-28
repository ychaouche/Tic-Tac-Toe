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
plyrs_le = "O"
comps_le = "X"

# score
comps_score = 0
plyrs_score = 0

def draw_handler(canvas, white_color, wordfont, XorO_color, XorO_font, currentgrid):


    # black canvas -- create the grid
    canvas.fill((0, 0, 0))
    
    # Horizontal lines
    pygame.draw.line(canvas, white_color, (left_edge, first_row), (right_edge, first_row), 12)
    pygame.draw.line(canvas, white_color, (left_edge, second_row), (right_edge, second_row), 12)
    # Vertical lines
    pygame.draw.line(canvas, white_color, (first_col, top_edge), (first_col, bottom_edge), 12)
    pygame.draw.line(canvas, white_color, (second_col, top_edge), (second_col, bottom_edge), 12)

    # Text displaying score and reset option
    newgametext = wordfont.render("N = New Game", True, white_color)
    comp_scoretxt = wordfont.render("Computer: " + str(comps_score), True, white_color)
    plyr_scoretxt = wordfont.render("Player: " + str(plyrs_score), True, white_color)

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

    
def mc_handler(pos, plyrs_turn, comps_turn, currentgrid):

    # Checks if mouseclick was in the first column
    if pos[0] < first_col and pos[0] > left_edge and plyrs_turn:
        if pos[1] < first_row and pos[1] > top_edge and Plyr_Comp_options.isSpaceFree(currentgrid, 0):
            currentgrid[0] = plyrs_le
            computers_turn = True
        if pos[1] < second_row and pos[1] > first_row and Plyr_Comp_options.isSpaceFree(currentgrid, 1):
            currentgrid[1] = plyrs_le
            computers_turn = True
        if pos[1] < bottom_edge and pos[1] > second_row and Plyr_Comp_options.isSpaceFree(currentgrid, 2):
            currentgrid[2] = plyrs_le
            computers_turn = True

    # Second column
    if pos[0] > first_col and pos[0] < second_col and plyrs_turn:
        if pos[1] < first_row and pos[1] > top_edge and Plyr_Comp_options.isSpaceFree(currentgrid, 3):
            currentgrid[3] = plyrs_le
            computers_turn = True
        if pos[1] < second_row and pos[1] > first_row and Plyr_Comp_options.isSpaceFree(currentgrid, 4):
            currentgrid[4] = plyrs_le
            computers_turn = True
        if pos[1] < bottom_edge and pos[1] > second_row and Plyr_Comp_options.isSpaceFree(currentgrid, 5):
            currentgrid[5] = plyrs_le
            computers_turn = True

    # Third column
    if pos[0] > second_col and pos[0] < right_edge and plyrs_turn:
        if pos[1] < first_row and pos[1] > top_edge and Plyr_Comp_options.isSpaceFree(currentgrid, 6):
            currentgrid[6] = plyrs_le
            computers_turn = True
        if pos[1] > first_row and pos[1] < second_row and Plyr_Comp_options.isSpaceFree(currentgrid, 7):
            currentgrid[7] = plyrs_le
            computers_turn = True
        if pos[1] > second_row and pos[1] < bottom_edge and Plyr_Comp_options.isSpaceFree(currentgrid, 8):
            currentgrid[8] = plyrs_le
            computers_turn = True

def scorekeeper(winner):
    global comps_score, plyrs_score

    if winner == comps_le:
        comps_score += 1

    if winner == plyrs_le:
        plyrs_score += 1
