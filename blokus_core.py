#!/usr/bin/env python3

import copy
import json


class Piece:
    '''
    A single game piece. 

    Methods:
    get_edge_squares()
        - returns a list of edges of this piece, only for init
    get_corner_squares() 
        - returns a list of corners of this piece, only for init
    square_locations()
        - returns a list of where the squares would be based on an origin
    edge_locations()
        - square_locations() but for edges
    corner_locations()
        - square_locations() but for corners

    Variables:
    color       - The color of the piece: red, blue, yellow, or green
    value       - The point value of the piece and the amount of squares it has

    squares     - List of location of all squares relative to an arbitrary 
    corners     - List of location of all squares that would be on a corner
    edges       - List of location of all squares that would be on an edge
                    origin square location 
    rotation    - Value from 0-3. An increase of 1 in this value corresponds 
                    with a 90-degree clockwise rotation
    flipped     - True if flipped. Always flipped over y-axis

    '''
    def __init__(self, color='blue', squares=[[0, 0]], rotation=0, flipped=False):
        self.color = color
        self.value = len(squares)

        self.squares = squares
        self.edges = self.get_edge_squares()
        self.corners = self.get_corner_squares()

        self.rotation = 0
        self.flipped = False
    

class Player:
    '''
    Represents a single player. Used to initialize all the pieces as well.
    
    Methods:
    get_legal_moves(board)
        - returns a list of all legal moves, used by choose_move()

    Variables:
    color       - blue, yellow, red, green
    score       - a tally of the player's score
    pieces      - a list of all pieces still in the player's hand
    '''
    def __init__(self, color):
        self.color = color
        self.score = 0
        self.pieces = []
        # possible piece coordinates are stored in pieces.json
        # load data from pieces.json
        with open('pieces.json') as pieces_json:
            pieces = json.load(pieces_json)
            for piece in pieces:
                self.pieces.append(Piece(color=color, squares=piece))



class Board:
    '''
    Represents the game board. Holds a 2d array and associated methods

    Methods:
    is_legal_move(self, piece, origin)
        - Returns True if move is legal. Accounts for corners, adjacency, and overlap

    Variables:
    spaces      - 2d array that holds pieces
    corners     - 2d array that holds lists of colors that can play for each square
    edges       - 2d array that holds lists of colors that cannot play for each square
    '''

    def __init__(self, num_players=4, length=20, height=20):
        self.spaces =  [[None for _ in range(height)] for _ in range(length)]
        self.edges =   [[[]   for _ in range(height)] for _ in range(length)]
        self.corners = [[[]   for _ in range(height)] for _ in range(length)]

        self.height = height
        self.length = length

        if num_players == 4:
            self.players = [Player(color) for color in ['blue', 'yellow', 'red', 'green']]
            self.corners[0][0].append('blue')
            self.corners[length-1][0].append('yellow')
            self.corners[length-1][height-1].append('red')
            self.corners[0][height-1].append('green')
        else: # TODO possibly implementing a two player game?? 
            self.players = [Player('blue'), Player('red')]
            self.corners[0][0].append('blue')
            self.corners[length-1][height-1].append('red')
