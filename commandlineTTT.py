import computer_AI
import possibleMoves

# Tic Tac Toe
import random
def instructions():
    print("""
You will make your move by entering a number, 1 - 9.
The number will correspond to the board position as shown below

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

Have fun, and good luck.

"""
    )
def drawGameBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not possibleMoves.isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def isWinner(board, letter):

    return ((board[1] == letter and board[2] == letter and board[3] == letter) or # across the top
            (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
            (board[7] == letter and board[8] == letter and board[9] == letter) or # across the bottom
            (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
            (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
            (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
            (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
            (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

def isGameBoardFull(board):
    for i in range(1, 10):
        if possibleMoves.isSpaceFree(board, i):
            return False
    return True

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('Welcome to Jose\'s Unbeatable Tic Tac Toe!')
instructions()

while True:
    theGameBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = "X"
    print( turn + ' goes first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == playerLetter:
            drawGameBoard(theGameBoard)
            move = getPlayerMove(theGameBoard)
            possibleMoves.makeMove(theGameBoard, playerLetter, move)
            if isWinner(theGameBoard, playerLetter):
                drawGameBoard(theGameBoard)
                print('You win.')
                gameIsPlaying = False
            else:
                if isGameBoardFull(theGameBoard):
                    drawGameBoard(theGameBoard)
                    print('The game is a tie.')
                    gameIsPlaying = False
                else:
                    turn = computerLetter
        else:
            move = computer_AI.getComputerMove(theGameBoard, computerLetter)
            possibleMoves.makeMove(theGameBoard, computerLetter, move)
            if isWinner(theGameBoard, computerLetter):
                drawGameBoard(theGameBoard)
                print('You Lose.')
                gameIsPlaying = False
            else:
                if isGameBoardFull(theGameBoard):
                    drawGameBoard(theGameBoard)
                    print('The game is a tie!')
                    gameIsPlaying = False
                else:
                    turn = playerLetter
    if not playAgain():
        break
