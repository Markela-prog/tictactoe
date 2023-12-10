import pygame
import sys

chosen_size = 3
chosen_symbol = 'X'

def show_menu(screen):
    global chosen_size, chosen_symbol
    font = pygame.font.Font(None, 36)


    size_button = pygame.Rect(150, 200, 300, 50)
    symbol_button = pygame.Rect(150, 300, 300, 50)
    start_button = pygame.Rect(150, 400, 300, 50)

    size_text = font.render(f"Choose Board Size: {chosen_size}", True, (0, 0, 0))
    symbol_text = font.render(f"Choose Symbol: {chosen_symbol}", True, (0, 0, 0))
    start_text = font.render("Start Game", True, (0, 0, 0))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if size_button.collidepoint(mouse_pos):
                    if chosen_size in [3,4]:
                        chosen_size += 1
                    elif chosen_size == 5:
                        chosen_size = 3
                    else:
                            chosen_size = 3
                    size_text = font.render(f"Choose Board Size: {chosen_size}", True, (0, 0, 0))
                elif symbol_button.collidepoint(mouse_pos):
                    chosen_symbol = 'X' if chosen_symbol == 'O' else 'O'
                    symbol_text = font.render(f"Choose Symbol: {chosen_symbol}", True, (0, 0, 0))
                elif start_button.collidepoint(mouse_pos):
                    return chosen_size, chosen_symbol

        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, (200, 200, 200), size_button)
        pygame.draw.rect(screen, (200, 200, 200), symbol_button)
        pygame.draw.rect(screen, (200, 200, 200), start_button)

        screen.blit(size_text, (size_button.x + 10, size_button.y + 10))
        screen.blit(symbol_text, (symbol_button.x + 10, symbol_button.y + 10))
        screen.blit(start_text, (start_button.x + 10, start_button.y + 10))

        pygame.display.flip()


