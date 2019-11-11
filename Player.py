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
        self.color = color
        self.score = 0
        self.pieces = []
        # possible piece coordinates are stored in pieces.json
        # load data from pieces.json
        with open('pieces.json') as pieces_json:
            pieces = json.load(pieces_json)
            for piece in pieces:
                self.pieces.append(Piece(color=color, squares=piece))

    # official str
    def __repr__(self):
        return 'Player: color={}, score={}, pieces={}'.format(self.color, self.score, [str(piece) for piece in self.pieces])

    # informal str
    def __str__(self):
        return repr(self)

    # TODO brute force approach
    # return legal moves
    def get_legal_moves(self, board):
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

    # TODO put choose_move(self, board) here?? hmm