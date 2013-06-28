import Plyr_Comp_options
import TTT

def kd_handler(key):
    if pygame.K_n == key:
        TTT.newgame()
    
def mc_handler(pos, players_turn, computers_turn, currentgrid):

    if pos[0] < first_col and pos[0] > left_edge and players_turn:
        if pos[1] < first_row and pos[1] > top_edge and Plyr_Comp_options.isSpaceFree(currentgrid, 0):
            currentgrid[0] = players_le
            computers_turn = True

