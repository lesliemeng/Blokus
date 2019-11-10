from Piece import Piece
from Player import Player
from Board import Board

# TODO see docs here: https://docs.python.org/3/library/tkinter.html
from tkinter import * # lib included in python3, hence requires python3

# set all globals to none
board, player, piece, piece_index, move_chosen, moves_not_made = [None]*6

def play_game(players=4):
    global board
    global player
    global piece
    global piece_index
    global move_chosen
    global moves_not_made

    # all 4 players are controlled by user(s)
    board = Board(players)
    game_over = False
    moves_not_made = 0

    # keep going while game not over
    while not game_over:
        # tkinter required updates
        root.update_idletasks()
        root.update()

        # each round
        for player in board.players:
            # prompt player turn by using color as indicator
            turn_indicator.config(bg=player.color)
            # default piece
            piece = player.pieces[0]
            piece_index = -1
            move_chosen = False
            # update & reset
            update_scores()
            refresh(board)
            cycle_piece('')

            # wait for player to make move
            while not move_chosen:
                root.update_idletasks()
                root.update()
            
            # if all players have skipped game over
            if moves_not_made >= players:
                game_over = True
                break
    
    # finish scoring

    # sort players into list of highest score first
    board.players.sort(key=lambda x: -x.score)

    # print winner with highest score from ^ sort()
    status_label.config(text=('Winner: ' + board.players[0].color))

    # TODO using lazy approach to handle ties, needs fix
    # if scores are tied, in (i < j),
    # player[i] will win player[j] due to sort and print player[0]
    # but I don't want to change display area/font to accomodate for
    # printing multiple winners... hmmmmmmmmm


# update score of each player to their respective grids
def update_scores():
    global board
    global score_display_grid

    for i, player in enumerate(board.players):
        score_display_grid[i].config(text=str(player.score))

# players can choose to not make a move in the round
def skip_move():
    global move_chosen
    global moves_not_made

    # keep track of this to determine if game should be over
    moves_not_made += 1
    move_chosen = True

# choose which move to make
def choose_move(i, j, e):
    global move_chosen
    global board
    global piece
    global moves_not_made

    if board.is_legal_move(piece, [i, j]):
        # apply move
        for k, l in piece.square_locations([i, j]):
            board.spaces[k][l] = piece.color
        for k, l in piece.corner_locations([i, j]):
            if -1 < k < 20 and -1 < l < 20:
                board.corners[k][l].append(piece.color)
        for k, l in piece.edge_locations([i, j]):
            if -1 < k < 20 and -1 < l < 20:
                board.edges[k][l].append(piece.color)

        # update score
        if len(player.pieces) == 1 and piece.value == 1:
            player.score += 20
        player.score += piece.value

        # remove piece from hand
        player.pieces.remove(piece)

        # once a player has made a move in the round, reset moves_not_made
        # (used to track if game should be over)
        moves_not_made = 0
        move_chosen = True


# cycle the pieces available
def cycle_piece(event):
    global player
    global piece
    global piece_index

    piece_index = (piece_index + 1) % len(player.pieces)
    piece = player.pieces[piece_index]

    display_piece(piece)

# cycle the position of current piece
def cycle_position(event):
    global piece

    if piece.rotation < 3:
        piece.rotation += 1
    else:
        piece.rotation = 0
        piece.flipped = False if piece.flipped else True
        # TODO lol I need to fix this idk

    display_piece(piece)

# display piece
def display_piece(piece):
    global piece_display_grid

    # make everything black again
    for row in piece_display_grid:
        for square in row:
            square.config(bg='black')

    # actually display the piece
    for x, y in piece.square_locations([4, 4]):
        piece_display_grid[x][y].config(bg=piece.color)

# refresh board
def refresh(board):
    global board_grid

    for i, row in enumerate(board.spaces):
        for j, space in enumerate(row):
            board_grid[i][j].config(bg=space)



if __name__ == '__main__':
    
    # init tkinter GUI
    root = Tk()
    root.title('CS521 :: Final Project :: BLOKUS')
    # TODO optional if adding custom tk icon
    # root.iconbitmap('logo.ico')

    # draw game board
    board = Frame(root, bg='black', width=500, height=500)
    board.pack(side=LEFT)
    board_grid = [[None for _ in range(20)] for _ in range(20)]

    # draw cells in game board
    # make each cell clickable (left click)
    for i, row in enumerate(board_grid):
        for j, column in enumerate(row):
            F = Frame(board, bg='grey', width=int((500/20)-4), height=int((500/20)-4), bd=0)
            F.grid(row=i, column=j, padx=2, pady=2)
            F.bind('<Button-1>', lambda e, i=i, j=j: choose_move(i, j, e))
            row[j] = F

    # draw status_frame containing everything to the right of the game board
    status_frame = Frame(root, bg='black', width=250, height=500)
    status_frame.pack(side=RIGHT)

    # draw turn_indicator that displays player turn by their color
    turn_indicator = Frame(status_frame, bg='blue', width=250, height=113)
    turn_indicator.grid(row=0, sticky='NESW')

    # draw skip turn button
    skip_turn_button = Button(status_frame, text='skip turn', command=skip_move)
    skip_turn_button.grid(row=1)

    # draw piece selector display
    piece_display = Frame(status_frame, bg='grey', width=250, height=250)
    piece_display.grid(row=2, pady=(4, 3), padx=(4, 3))
    piece_display_grid = [[None for _ in range(9)] for _ in range(9)]

    # draw cells in piece_display
    # make each cell clickable
    # - left click to cycle piece
    # - right click to cycle position
    for i, row in enumerate(piece_display_grid):
        for j, column in enumerate(row):
            F = Frame(piece_display, bg='black', width=int(250/9-4), height=int(250/9-4), bd=0)
            F.grid(row=i, column=j, padx=2, pady=2)
            F.bind('<Button-1>', cycle_piece)
            F.bind('<Button-2>', cycle_position)
            F.bind('<Button-3>', cycle_position)
            row[j] = F

    # draw score display area
    scores = Frame(status_frame, bg='blue', width=250, height=150)
    scores.grid(row=3)
    
    # draw score display grid
    score_display_grid = ['blue', 'yellow', 'red', 'green']
    for i, color in enumerate(score_display_grid):
        F = Frame(scores, bg=color, width=60, height=150)
        L = Label(F, bg=color, font=('Helvetica', '36'))
        L.pack()
        F.grid(column=i, row=0)
        score_display_grid[i] = L

    # draw status display area for announcing winners
    status_label_frame = Frame(status_frame, bg='orange', width=250, height=50)
    status_label = Label(status_label_frame, bg='orange', font=('Helvetica', '24'))
    status_label.place(relwidth=1.0, relheight=1.0)
    status_label_frame.grid(row=4, sticky='NSEW')

    # start the game!!
    play_game(4)

    # tkinter mainloop
    root.mainloop()