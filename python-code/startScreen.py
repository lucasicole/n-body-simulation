# Start Screen

# Imports

import pygame
from buttonsClass import Button
from textboxClass import textbox

# Start Screen Function

def start_screen(screen):
    """
    This function creates the start screen where the user can input all the data they need for a simulation.
    """
    startScreen = True

    # Creating the title at the top left of the screen.
        
    title_text = (pygame.font.Font(None, 40)).render("N-body Simulation: Start Screen", True, (255, 255, 255))
    text_position = title_text.get_rect(center = (240, 25))

    # Creating a button to activate another screen to add a body to the program.

    add_body_button = Button(100, 100, 200, 50, "Add a body", pygame.font.Font(None, 40), (255, 255, 255), (192, 192, 192), (124, 192, 255), screen)

    # Creating a button leading to the simulation screen.

    simulation_screen_button = Button(100, 200, 200, 50, "Simulation Screen", pygame.font.Font(None, 30), (255, 255, 255), (192, 192, 192), (124, 192, 255), screen)

    while startScreen:

        # Resetting the screen

        screen.fill((0, 0, 0))

        # Creates a clock object allowing me to limit the frame rate.

        clock = pygame.time.Clock()
        
        # Drawing a line to separate the text at the top of the screen from the rest of the screen.

        pygame.draw.line(screen, (255, 255, 255), (0, 40), (1920, 40), 5)

        # Checking for events.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                startScreen = False
                return False
            if add_body_button.clicked(event):
                return 1
            if simulation_screen_button.clicked(event):
                return 2

        # Drawing the objects onto the screen.

        screen.blit(title_text, text_position)
        add_body_button.draw_button()

        simulation_screen_button.draw_button()

        # Refreshes the entire display.

        clock.tick(60)  
        pygame.display.flip()
