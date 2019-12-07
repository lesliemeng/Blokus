#!/usr/bin/env python3

"""
Leslie Meng
Class: CS 521 - Fall 2
Date: 12/12/2019
Final Project
This Piece class is imported by main.py.
More description are below
"""

import copy

class Piece():
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

    # official str
    def __repr__(self):
        return 'Piece: color={}, value={}'.format(self.color, self.value)

    # informal str
    def __str__(self):
        return repr(self)

    # equal or not
    def __eq__(self, other):
        """ This function checks the squares are equal or not
        """
        return self.squares == other.squares

    # uses the squares list to create a list of squares
    # of where other pieces of the same color cannot go
    def get_edge_squares(self):
        """ This function identifies the location of each piece's edges.
        For example, 1 square located at square[0,0], its "edges" are [1,0], 
        [-1,0], [0,1], [0,-1]. These are where other pieces of the same color
        can not go.
        """
        edges = []
        for square in self.squares:
            # finds adjacent squares to each square
            possible_edges = [[square[0]+a, square[1]+b] for a, b, square in [
                (1, 0, square), (-1, 0, square), (0, 1, square), (0, -1, square)]]
            for edge in possible_edges:
                if edge not in self.squares:
                    edges.append(edge)
        # print(' '.join(map(str, edges)))
        return edges

    # uses the squares list and the edges list to create a list of squares
    # where other pieces of the same color can go
    def get_corner_squares(self):
        """ This function identifies the location of each piece's corners.
        These are where other pieces of the same color can go.
        """
        corners = []
        for square in list(self.squares):
            # finds the diagonal squares to each square
            possible_corners = [[square[0]+a, square[1]+b] for a, b, square in [
                (1, 1, square), (1, -1, square), (-1, 1, square), (-1, -1, square)]]
            for corner in possible_corners:
                if corner not in self.squares + self.edges:
                    corners.append(corner)
        # print(' '.join(map(str, corners)))
        return corners

    # returns a list of the locations of all squares, accounting for origin
    def square_locations(self, origin):
        """ returns a list of the locations of all squares, accounting for origin
        """
        squares_copy = copy.deepcopy(self.squares)

        for square in squares_copy:
            # account for rotation
            if self.rotation % 4 == 1:
                square[0], square[1] = square[1], -square[0]
            elif self.rotation % 4 == 2:
                square[0], square[1] = -square[0], -square[1]
            elif self.rotation % 4 == 3:
                square[0], square[1] = -square[1], square[0]
            # account for flip
            if self.flipped:
                square[0] *= -1
            # account for origin
            square[0] += origin[0]
            square[1] += origin[1]
#        print(' '.join(map(str, squares_copy))) 
        return squares_copy

    # returns a list of the locations of all corners, accounting for origin
    def edge_locations(self, origin):
        """ returns a list of the locations of all corners, accounting for origin
        """
        edges = []
        for square in self.square_locations(origin):
            # finds the adjacent squares to each square
            possible_edges = [[square[0]+a, square[1]+b] for a, b, square in [
                (1, 0, square), (-1, 0, square), (0, 1, square), (0, -1, square)]]
            for edge in possible_edges:
                if edge not in self.square_locations(origin):
                    edges.append(edge)
        return edges

    # returns a list of the locations of all corners, accounting for origin
    def corner_locations(self, origin):
        """ returns a list of the locations of all corners, accounting for origin
        """
        corners = []
        for square in self.square_locations(origin):
            # finds the diagonal squares to each square
            possible_corners = [[square[0]+a, square[1]+b] for a, b, square in [
                (1, 1, square), (1, -1, square), (-1, 1, square), (-1, -1, square)]]
            for corner in possible_corners:
                if corner not in self.square_locations(origin) + self.edge_locations(origin):
                    corners.append(corner)
        return corners
