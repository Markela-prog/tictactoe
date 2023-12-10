import pygame
import sys

def get_nickname(screen):
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(150, 100, 300, 50)
    submit_button = pygame.Rect(200, 200, 200, 50)  # Button to submit input
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    input_color = color_inactive
    submit_color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the input box is clicked
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False

                # Check if the submit button is clicked
                if submit_button.collidepoint(event.pos) and text:
                    done = True  # Set done to True to submit the input

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((255, 255, 255))

        # Draw input box
        input_color = color_active if active else color_inactive
        pygame.draw.rect(screen, input_color, input_box)
        font_surface = font.render(text, True, (0, 0, 0))
        screen.blit(font_surface, (input_box.x + 10, input_box.y + 10))

        # Determine submit button color based on text input
        submit_color = color_active if text else color_inactive

        # Draw submit button
        pygame.draw.rect(screen, submit_color, submit_button)
        submit_text = font.render("Submit", True, (0, 0, 0))
        screen.blit(submit_text, (submit_button.x + 10, submit_button.y + 10))

        pygame.display.flip()

    return text


