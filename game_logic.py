import pygame

from constants import LINE_COLOR


def initialize_board(size):
    return [['' for _ in range(size)] for _ in range(size)]


def draw_symbol(screen, row, col, symbol, square_size):
    font = pygame.font.Font(None, 100)
    text = font.render(symbol, True, LINE_COLOR)
    text_rect = text.get_rect(center=(col * square_size + square_size // 2, row * square_size + square_size // 2))
    screen.blit(text, text_rect)

def check_win(board):
    size = len(board)
    win_length = 3  # Set the desired number of consecutive symbols for a win

    def check_line(line):
        for i in range(len(line) - win_length + 1):
            # Check if there are win_length consecutive symbols in the line
            if all(symbol == line[i] and symbol != '' for symbol in line[i:i+win_length]):
                return True
        return False

    # Check rows
    for i in range(size):
        if any(check_line(row) for row in board):
            return True

    # Check columns
    for i in range(size):
        if any(check_line([row[i] for row in board]) for i in range(size)):
            return True

    # Check diagonals
    for i in range(size - win_length + 1):
        for j in range(size - win_length + 1):
            # Check main diagonals
            if check_line([board[i + k][j + k] for k in range(win_length)]):
                return True
            # Check reverse diagonals
            if check_line([board[i + k][j + win_length - 1 - k] for k in range(win_length)]):
                return True

    return False

