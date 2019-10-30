#!/usr/bin/env python3
"""
Leslie Meng
Class: CS 521 - Fall 2
Date: 12/12/2019
Final Project
This Player class is imported by main.py.
"""

import json
from Piece import Piece

class Player():
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
        self.__color = color
        self.score = 0
        self.pieces = self.__load_pieces_coor__(color)


    # official str
    def __repr__(self):
        # return 'Player: color={}, score={}, pieces={}'.format(self.color, self.score, [str(piece) for piece in self.pieces])
        return 'Player: color = {0:8s} |   score = {1:<9.0f}'.format(self.__color, self.score)
        # pieces not defined
        # return 'Player: color={}, score={}, pieces={}'.format(self.color, self.score, [str(piece) for piece in pieces if str(piece) not in self.pieces])

    # informal str
    def __str__(self):
        return repr(self)

    def __load_pieces_coor__(self, color):
        """ private method load pieces coordinates from JSON file,
        return to be catched by self.pieces in init
        """
        self.pieces_coor = []
        # load data from pieces.json
        with open('pieces.json') as pieces_json:
            pieces_coor = json.load(pieces_json)
            for piece in pieces_coor:
                self.pieces_coor.append(Piece(color=color, squares=piece))
        
        return self.pieces_coor

    # getters
    def get_color(self):
        """ This function returns the color of the Player.
        """
        return self.__color
        
    # setters
    def set_color(self, color):
        """ This function changes the new color of the Player.
        """
        self.__color = color

    def get_legal_moves(board):
        # TODO