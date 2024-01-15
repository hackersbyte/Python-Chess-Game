import pygame

# Importing custom constants
from const import *
from board import *
from dragger import Dragger

class Game:
    """
    Game class to handle game logic and rendering
    """

    def __init__(self):
        """
        Initialize the game class
        """
        self.board = Board()
        self.dragger = Dragger()

    # Show methods

    def show_bg(self, surface):
        """
        Show the game board background

        :param surface: Surface to draw on
        """
        # Iterating through rows and columns
        for row in range(ROWS):
            for col in range(COLS):
                # Determining the color of the square based on its position
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)  # light green
                else:
                    color = (119, 154, 88)   # dark green

                # Calculating the position and size of the square
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                # Drawing the square on the surface
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)     
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

        