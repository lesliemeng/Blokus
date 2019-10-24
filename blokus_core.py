#!/usr/bin/env python3

import copy
import json


class Piece:
    '''
    A single game piece.
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
