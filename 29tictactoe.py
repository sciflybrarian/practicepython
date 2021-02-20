import itertools as it
import numpy as np

def printgame(board):
    print("\n    A   B   C")
    for i in range(3):
        print("  " + " ---" * 3)
        print("{} | {} | {} | {} |".format(i + 1,
                                           symbols[board[i][0]],
                                           symbols[board[i][1]],
                                           symbols[board[i][2]]))
    print("  " + " ---" * 3)
    
def winner(board):
    rows = np.array(board)
    cols = rows.T
    diags = np.array([[board[i][i] for i in range(3)],
                      [board[i][2-i] for i in range(3)]])
    all_dimensions = np.concatenate((rows, cols, diags))
    
    for set in all_dimensions:
        if all(x == 1 for x in set) or all(x == 2 for x in set):
            return set[0]
    return 0

def printscores():
    print("\nSCOREBOARD")
    for player in [1, 2]:
        print("Player {}:  {}".format(player, wins[player]))
    print("Ties:      {}".format(wins[0]))
        
symbols = {0: " ", 1: "X", 2: "O"}
columns = {"a": 0, "b": 1, "c": 2}
wins = {0: 0, 1: 0, 2: 0}
newgame = True

print("TIC TAC TOE")

while newgame:
    playing = True
    game = [[0 for x in range(3)] for x in range (3)]
    turn = 0
    
    printgame(game)
    print("\nEnter the column letter followed by the row number. Example: A1\nLeave blank to exit.")
    
    while playing:
        for player in [1, 2]:
            move = input("\nPlayer {} ({}): ".format(player, symbols[player]))
            if len(move) == 0:
                playing = False
                break
            col, row = move[0], move[1:]
            game[int(row.strip())-1][columns[col.lower()]] = player
            printgame(game)
            if winner(game) == player:
                print("\nPLAYER {} WINS!".format(player))
                wins[player] += 1
                playing = False
                break
            if 0 not in it.chain.from_iterable(game):
                print("\nIT'S A TIE!")
                wins[0] += 1
                playing = False
                break
    printscores()
    newgameprompt = input("\nPlay again? (Y/N)")
    if newgameprompt.lower() != "y":
        newgame = False