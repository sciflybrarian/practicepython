# Instructions at https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html

import itertools as it

def printgame(board):
    print("\n    1    2    3")
    for i in range(3):
        print(i + 1, board[i])
        
players = {"Player 1": "X", "Player 2": "O"}
game = [["-" for x in range(3)] for x in range (3)]
turn = 0
playing = True

print("TIC TAC TOE")
printgame(game)
print("\nEnter the row number and column number, separated by a comma.\nLeave blank to exit.")

while playing:
    for player, symbol in sorted(players.items()):
        move = input("\n{} ({}): ".format(player, symbol))
        if len(move) == 0:
            playing = False
            break
        row, col = move.split(",")
        game[int(row.strip())-1][int(col.strip())-1] = symbol
        printgame(game)
        if "-" not in it.chain.from_iterable(game):
            playing = False
            break
