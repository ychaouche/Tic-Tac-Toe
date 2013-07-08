import computer_AI

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

print('Welcome to Jose\'s Unbeatable Tic Tac Toe!')
instructions()

while True:
    theGameBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            drawGameBoard(theGameBoard)
            move = getPlayerMove(theGameBoard)
            makeMove(theGameBoard, playerLetter, move)
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
                    turn = 'computer'
        else:
            move = getComputerMove(theGameBoard, computerLetter)
            makeMove(theGameBoard, computerLetter, move)
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
                    turn = 'player'
    if not playAgain():
        break
