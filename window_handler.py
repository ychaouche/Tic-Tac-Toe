##import the variables
import pygame
import possible_moves

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
O = "O"
X = "X"

# score
comps_score = 0
plyrs_score = 0

def draw_handler(canvas, white_color, wordfont, XorO_color, XorO_font, currentgrid, comps_turn, plyrs_turn):

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
        # Zeroth square top left
        if pos[1] < first_row and pos[1] > top_edge and possible_moves.isSpaceFree(currentgrid, 0):
            currentgrid[0] = O
        # First square center left
        if pos[1] < second_row and pos[1] > first_row and possible_moves.isSpaceFree(currentgrid, 1):
            currentgrid[1] = O
        # Second square lower left
        if pos[1] < bottom_edge and pos[1] > second_row and possible_moves.isSpaceFree(currentgrid, 2):
            currentgrid[2] = O

    # Second column
    if pos[0] > first_col and pos[0] < second_col and plyrs_turn:
        # Third square top center
        if pos[1] < first_row and pos[1] > top_edge and possible_moves.isSpaceFree(currentgrid, 3):
            currentgrid[3] = O
        # Fourth square center
        if pos[1] < second_row and pos[1] > first_row and possible_moves.isSpaceFree(currentgrid, 4):
            currentgrid[4] = O
        # Fifth square bottom center
        if pos[1] < bottom_edge and pos[1] > second_row and possible_moves.isSpaceFree(currentgrid, 5):
            currentgrid[5] = O

    # Third column
    if pos[0] > second_col and pos[0] < right_edge and plyrs_turn:
        # Sixth square top right
        if pos[1] < first_row and pos[1] > top_edge and possible_moves.isSpaceFree(currentgrid, 6):
            currentgrid[6] = O
        # Seventh square center right
        if pos[1] > first_row and pos[1] < second_row and possible_moves.isSpaceFree(currentgrid, 7):
            currentgrid[7] = O
        # Eighth square bottom right
        if pos[1] > second_row and pos[1] < bottom_edge and possible_moves.isSpaceFree(currentgrid, 8):
            currentgrid[8] = O

def scorekeeper(winner):
    global comps_score, plyrs_score

    if winner == X:
        comps_score += 1
        possible_moves.dead_game()

    if winner == O:
        plyrs_score += 1
    
# checks for a winner
def is_winner(gr, le):
    # gr == grid and le == letter, returns True if there is a winner

    return ((gr[0] == le and gr[1] == le and gr[2] == le) or # up the left side
            (gr[0] == le and gr[4] == le and gr[8] == le) or # top left to bottom right diagonally
            (gr[0] == le and gr[3] == le and gr[6] == le) or # top row
            (gr[1] == le and gr[4] == le and gr[7] == le) or # middle row
            (gr[2] == le and gr[5] == le and gr[8] == le) or # bottom row
            (gr[2] == le and gr[4] == le and gr[6] == le) or # top right to bottom left diagonally
            (gr[8] == le and gr[7] == le and gr[6] == le) or # up the right side
            (gr[3] == le and gr[4] == le and gr[5] == le))   # up the middle

