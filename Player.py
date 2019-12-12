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


    # return legal moves
    def get_legal_moves(self, board):
        """ This function return legal moves, it uses borad.is_legal_move()
        to validate whether it is a legal move
        """
        legal_moves = []

        for piece in enumerate(self.pieces):
            # every rotation
            for rotation in range(4):
                piece[1].rotation = rotation
                # every flip
                for flip in [True, False]:
                    piece[1].flipped = flip
                    # every square
                    for row in range(board.height):
                        for column in range(board.length):
                            if board.is_legal_move(piece[1], [row, column]):
                                legal_moves.append(
                                    [piece[1], [row, column], rotation, flip])
        # moves are represented as:
        # [index in self.pieces, coords, rotation, flip]
        return legal_moves


if __name__ == '__main__':
    '''
    Unit Test
    
    We can only test:
    get_color()
    set_color()

    We CANNOT test the following as it requires the board class:
    get_legal_moves()
    '''

    # initiate Player object
    init_color = "Orange"
    test_player = Player(init_color)
    
    # test that get_color() returns the same value as init_color
    assert test_player.get_color() == init_color, (
            "Error matching color {} != {}".format(test_player.get_color(), init_color))

    # set color
    new_color = "Red"
    test_player.set_color(new_color)
    
    # test that get_color() returns the new_color after player.__color
    # is set to new_color using set_color(new_color)
    assert test_player.get_color() == new_color, (
            "Error matching color {} != {}".format(test_player.get_color(), new_color))
    
    # this will use __str__() & __repr__()
    print(test_player) # player.__color should be red
    test_player.set_color("Orange")
    print(test_player) # player.__color should be orange
    