import pygame
import sys
import game_logic
import game_menu
import user_name_input
from constants import LINE_COLOR
import datetime
import random

pygame.init()

WIDTH, HEIGHT = 600, 600

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

nickname = user_name_input.get_nickname(screen)

# Show game menu and get user choices
size, symbol = game_menu.show_menu(screen)

board = game_logic.initialize_board(size)

SQUARE_SIZE = WIDTH // size
WHITE = (255, 255, 255)


# Function to draw the grid
def draw_grid():
    for row in range(1, size):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE))
    for col in range(1, size):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT))



# Function to draw the current state of the board
def draw_board_state():
    screen.fill(WHITE)
    draw_grid()

    # Draw Xs and Os on the board based on the 'board' variable
    for row in range(size):
        for col in range(size):
            if board[row][col] != '':
                game_logic.draw_symbol(screen, row, col, board[row][col], SQUARE_SIZE)

    pygame.display.flip()


# Function to show a message box
def show_message(message):

    message_font = pygame.font.Font(None, 36)
    message_text = message_font.render(message, True, (0, 0, 0))

    message_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.fill(WHITE)

    screen.blit(message_text, message_rect.topleft)
    pygame.display.flip()
    pygame.time.delay(2000)  # Display the message for 2 seconds (adjust as needed)
    draw_board_state()
    pygame.time.delay(2000)



player_moved = False  # Flag to track the player's move

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()

            # Determine the clicked cell
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            # Check if the cell is empty before making a move
            if 0 <= clicked_row < size and 0 <= clicked_col < size and board[clicked_row][clicked_col] == '':

                if symbol == 'X':
                    current_player = 'X' if sum(row.count('X') for row in board) <= sum(
                        row.count('O') for row in board) else 'O'
                elif symbol == 'O':
                    current_player = 'O' if sum(row.count('O') for row in board) <= sum(
                        row.count('X') for row in board) else 'X'
                else:
                    current_player = 'X' if sum(row.count('X') for row in board) <= sum(
                        row.count('O') for row in board) else 'O'



                # Update the board
                board[clicked_row][clicked_col] = current_player


                # Check for a win
                if game_logic.check_win(board):

                    if current_player == symbol:
                        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
                        with open('game_history.txt', 'a') as file:
                            file.write(
                                f"{nickname} has won the game. They played as {current_player}. Date: {current_date}\n")
                            show_message(f"{current_player} wins! {nickname} has won the game.")
                    else:
                        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
                        with open('game_history.txt', 'a') as file:
                            file.write(
                                f"Bot has won the game. They played as {current_player}. Date: {current_date}\n")
                            show_message(f"{current_player} wins! Bot has won the game.")


                    # Go back to the menu
                    size, symbol = game_menu.show_menu(screen)
                    board = game_logic.initialize_board(size)
                    SQUARE_SIZE = WIDTH // size
                    continue  # Restart the game loop with the new settings

                # Check for a tie (board is full)
                if all(all(cell != '' for cell in row) for row in board):
                    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
                    with open('game_history.txt', 'a') as file:
                        file.write(f"{nickname} and Bot tied the game. Date: {current_date}\n")
                    show_message("It's a tie!")

                    # Go back to the menu
                    size, symbol = game_menu.show_menu(screen)
                    board = game_logic.initialize_board(size)
                    SQUARE_SIZE = WIDTH // size
                    continue  # Restart the game loop with the new settings

                # Set flag to indicate the player has moved
                player_moved = True

                    # Bot's move logic after the player's move
                if player_moved:
                    available_spots = [(i, j) for i in range(size) for j in range(size) if board[i][j] == '']

                    # Choose a random spot for the bot's move
                    if available_spots:
                        bot_move = random.choice(available_spots)
                        row, col = bot_move
                        if current_player == 'O':
                            current_player = 'X'
                            board[row][col] = current_player
                        else:
                            current_player = 'O'
                            board[row][col] = current_player
                    player_moved = False  # Reset the flag for the next player's move

                    # Check for a win
                    if game_logic.check_win(board):

                        if current_player == symbol:
                            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
                            with open('game_history.txt', 'a') as file:
                                file.write(
                                    f"{nickname} has won the game. They played as {current_player}. Date: {current_date}\n")
                                show_message(f"{current_player} wins! {nickname} has won the game.")
                        else:
                            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
                            with open('game_history.txt', 'a') as file:
                                file.write(
                                    f"Bot has won the game. They played as {current_player}. Date: {current_date}\n")
                                show_message(f"{current_player} wins! Bot has won the game.")

                        # Go back to the menu
                        size, symbol = game_menu.show_menu(screen)
                        board = game_logic.initialize_board(size)
                        SQUARE_SIZE = WIDTH // size
                        continue  # Restart the game loop with the new settings

                    # Check for a tie (board is full)
                    if all(all(cell != '' for cell in row) for row in board):
                        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
                        with open('game_history.txt', 'a') as file:
                            file.write(f"{nickname} and Bot tied the game. Date: {current_date}\n")
                        show_message("It's a tie!")

                        # Go back to the menu
                        size, symbol = game_menu.show_menu(screen)
                        board = game_logic.initialize_board(size)
                        SQUARE_SIZE = WIDTH // size
                        continue  # Restart the game loop with the new settings




    draw_board_state()
