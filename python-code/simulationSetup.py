# Simulation set-up screen

# Imports

import pygame
from buttonsClass import Button
from textboxClass import textbox

# Simulation set-up function

def simulation_set_up(screen, bodies_dict):
    """
    A screen where the user can adjust parameters of the simulation.
    """

    simulationSetUp = True
    clock = pygame.time.Clock()

    # Creating the title at the top left of the screen.
        
    title_text = (pygame.font.Font(None, 40)).render("N-body Simulation: Simulation set-up", True, (255, 255, 255))
    text_position = title_text.get_rect(center = (260, 25))

    # Buttons and objects rendered for the user

    start_simulation_button = Button(100, 100, 200, 50, "Start Simulation", pygame.font.Font(None, 30), (255, 255, 255), (192, 192, 192), (124, 192, 255), screen)
    change_timestep_textbox = textbox(100, 200, 50, 10, pygame.font.Font(None, 40), (255, 255, 255), (192, 192, 192), screen)
    change_gravitational_constant_textbox = textbox(100, 300, 50, 10, pygame.font.Font(None, 40), (255, 255, 255), (192, 192, 192), screen)

    # Variables displayed to the user.

    timestep = 1
    gravitational_constant = 6.67430e-11
    timestep_label = pygame.font.Font(None, 30).render("Timestep: " + str(timestep) + " (default is 1 second).", True, (255, 255, 255))
    timestep_label_position = (240, 195)
    gravitational_constant_label = pygame.font.Font(None, 30).render("Gravitational Constant: " + str(gravitational_constant) + " (default is 6.67430e-11).", True, (255, 255, 255))
    gravitational_constant_label_position = (240, 295)

    # For loop creating a list of the names of each body currently active in simulation and creating text telling the user how many bodies there are.

    bodies_amount_string = str(len(bodies_dict))

    body_names_text = (pygame.font.Font(None, 30)).render("Bodies in simulation: " + bodies_amount_string, True, (255, 255, 255))
    body_names_text_position = (1000, 100)

    # Loop controlling the screen.

    while simulationSetUp:

        # Resetting the screen

        screen.fill((0, 0, 0))

        # Checking for events.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                simulationSetUp = False
                return False
            if start_simulation_button.clicked(event):
                simulationSetUp = False
                return (1, timestep, gravitational_constant)
            
            # Temporary variable r used for the textboxes.

            r = change_timestep_textbox.clicked(event)
            if r != None:
                timestep = float(r)
                timestep_label = pygame.font.Font(None, 30).render("Timestep: " + str(timestep) + " (default is 1 second).", True, (255, 255, 255))

            r = change_gravitational_constant_textbox.clicked(event)
            if r != None:
                gravitational_constant = float(r)
                gravitational_constant_label = pygame.font.Font(None, 30).render("Gravitational Constant: " + str(gravitational_constant) + " (default is 6.67430e-11).", True, (255, 255, 255))


        # Drawing the objects onto the screen.
        
        screen.blit(title_text, text_position)
        screen.blit(body_names_text, body_names_text_position)
        screen.blit(timestep_label, timestep_label_position)
        screen.blit(gravitational_constant_label, gravitational_constant_label_position)
        pygame.draw.line(screen, (255, 255, 255), (0, 40), (1920, 40), 5)
        start_simulation_button.draw_button()
        change_timestep_textbox.draw_box()
        change_gravitational_constant_textbox.draw_box()

        clock.tick(60)
        pygame.display.flip()
