#!/usr/bin/env python3

"""
Leslie Meng
Class: CS 521 - Fall 2
Date: 12/12/2019
Final Project
This Board class is imported by main.py.
More description are below
"""

from Piece import Piece # only importing for unit test
from Player import Player

class Board():
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
        self.spaces  = [[None for _ in range(height)] for _ in range(length)]
        self.edges   = [[[]   for _ in range(height)] for _ in range(length)]
        self.corners = [[[]   for _ in range(height)] for _ in range(length)]

        self.__height = height
        self.__length = length

        if num_players == 4:
            self.players = [Player(color) for color in ['blue', 'yellow', 'red', 'green']]
            self.corners[0][0].append('blue')
            self.corners[length-1][0].append('yellow')
            self.corners[length-1][height-1].append('red')
            self.corners[0][height-1].append('green')

    # getters
    def get_height(self):
        """ This function returns the height of the board.
        """
        return self.__height
    
    def get_length(self):
        """ This function returns the length of the board.
        """
        return self.__length
    
    # setters
    def set_height(self, height):
        """ This function changes the new height of the board.
        """
        self.__height = height
    
    def set_length(self, length):
        """ This function changes the new length of the board.
        """
        self.__length = length

    def is_legal_move(self, piece, origin):
        """ return bool if is legal move, checked in each click on game board
        """
        try:
            has_corner = False
            for location in piece.square_locations(origin):
                # direct overlap
                if self.spaces[location[0]][location[1]]:
                    return False
                # adjacency
                if piece.color in self.edges[location[0]][location[1]]:
                    return False
                # corners
                if piece.color in self.corners[location[0]][location[1]]:
                    has_corner = True
            return has_corner
        except IndexError:  # if move goes out of bounds of the game board
            return False
        
if __name__ == '__main__':
    '''
    Unit Test:
    
    get_length()
    get_height()
    set_length()
    set_height()
    is_legal_move()
    '''
    # initiate Board object
    init_length = 10
    init_height = 5
    test_board = Board(4, init_length, init_height)
    
    # test that get_height() returns the same value as init_height
    assert test_board.get_height() == init_height, (
            "Error matching height {} != {}".format(test_board.get_height(), init_height))
    
    # test that get_length() returns the same value as init_length
    assert test_board.get_length() == init_length, (
            "Error matching length {} != {}".format(test_board.get_length(), init_length))

    mod_length = 5
    mod_height = 10
    test_board.set_length(mod_length)
    test_board.set_height(mod_height)

    # test that get_height() returns the same value as mod_height
    assert test_board.get_height() == mod_height, (
            "Error matching height {} != {}".format(test_board.get_height(), mod_height))
    
    # test that get_length() returns the same value as mod_length
    assert test_board.get_length() == mod_length, (
            "Error matching length {} != {}".format(test_board.get_length(), mod_length))


    piece = Piece([[0,0]])
    origin_sq = [0, 0]
    # test that is_legal_move() returns False
    assert test_board.is_legal_move(piece, origin_sq) == False, (
            "Error matching is_legal_move {} != {}".format(test_board.is_legal_move(piece, origin_sq), False))