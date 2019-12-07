#!/usr/bin/env python3

"""
Leslie Meng
Class: CS 521 - Fall 2
Date: 12/12/2019
Final Project
This Board class is imported by main.py.
More description are below
"""

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
