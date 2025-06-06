# Add body screen

# Imports

import pygame
from buttonsClass import Button
from textboxClass import textbox
from bodiesClass import Bodies
from vectorsClass import Vector
import random

# Add body function

def add_body_screen(screen):
    """
    This function creates a screen that allows the user to create a body object.
    """
    addBodyScreen = True

    def add_random_bodies(number_of_bodies):
        """
        Creates a random number of bodies of the same mass at random positions with random velocities.
        """
        random_body_list = []
        for i in range(number_of_bodies):
            random_position = Vector(float(random.randint(-800, 800)), float(random.randint(-800, 800)))
            random_velocity = Vector(0.0, 0.0)#Vector((float(random.randint(-10, 10)) / 10), (float(random.randint(-10, 10)) / 10))
            random_body_list.append(Bodies("RandomBody_" + str(i), randomBody_mass, "red", random_position, random_velocity))
        return random_body_list

    # Creating the variables 

    newBody_name = ''
    newBody_mass = ''
    newBody_colour = ''
    newBody_position_x = ''
    newBody_position_y = ''
    newBody_velocity_x = ''
    newBody_velocity_y = ''
    randomBody_mass = ''
    randomBody_number = ''

    # Creating the title at the top left of the screen (taken from the start screen function).
        
    title_text = (pygame.font.Font(None, 40)).render("N-body Simulation: Add body screen", True, (255, 255, 255))
    text_position = title_text.get_rect(center = (272, 25))

    # Creating the text for labelling the textboxes.

    name_label = (pygame.font.Font(None, 30)).render(("Name of the body: " + newBody_name), True, (255, 255, 255))
    name_label_position = (450, 100)

    mass_label = (pygame.font.Font(None, 30)).render("Mass of the body: " + newBody_mass, True, (255, 255, 255))
    mass_label_position = (450, 160)

    colour_label = (pygame.font.Font(None, 30)).render("Colour of the body: " + newBody_colour, True, (255, 255, 255))
    colour_label_position = (450, 220)

    xPosition_label = (pygame.font.Font(None, 30)).render("X-coordinate of the body: " + newBody_position_x, True, (255, 255, 255))
    xPosition_label_position = (450, 280)

    yPosition_label = (pygame.font.Font(None, 30)).render("Y-coordinate of the body: " + newBody_position_y, True, (255, 255, 255))
    yPosition_label_position = (450, 340)

    xVelocity_label = (pygame.font.Font(None, 30)).render("X-coordinate (velocity) of the body: " + newBody_velocity_x, True, (255, 255, 255))
    xVelocity_label_position = (450, 400)

    yVelocity_label = (pygame.font.Font(None, 30)).render("Y-coordinate (velocity) of the body: " + newBody_velocity_y, True, (255, 255, 255))
    yVelocity_label_position = (450, 460)

    randomBodysMass_label = pygame.font.Font(None, 30).render("Mass of the random bodies: " + randomBody_mass, True, (255, 255, 255))
    randomBodysMass_position = (450, 580)

    randomBodysNumber_label = pygame.font.Font(None, 30).render("Number of random bodies: " + randomBody_number, True, (255, 255, 255))
    randomBodysNumber_position = (450, 520)

    # Creating the input buttons for the parameters of the bodies class.

    name_textbox = textbox(200, 100, 50, 20, pygame.font.Font(None, 40), (255, 255, 255), (192, 192, 192), screen)

    mass_textbox = textbox(200, 160, 50, 20, pygame.font.Font(None, 40), (255, 255, 255), (192, 192, 192), screen)

    colour_textbox = textbox(200, 220, 50, 20, pygame.font.Font(None, 40), (255, 255, 255), (192, 192, 192), screen)

    xPosition_textbox = textbox(200, 280, 50, 20, pygame.font.Font(None, 40), (255, 255, 255), (192, 192, 192), screen)

    yPosition_textbox = textbox(200, 340, 50, 20, pygame.font.Font(None, 40), (255, 255, 255), (192, 192, 192), screen)

    xVelocity_textbox = textbox(200, 400, 50, 20, pygame.font.Font(None, 40), (255, 255, 255), (192, 192, 192), screen)

    yVelocity_textbox = textbox(200, 460, 50, 20, pygame.font.Font(None, 40), (255, 255, 255), (192, 192, 192), screen)

    addBody_button = Button(100, 1000, 200, 50, "Add body", pygame.font.Font(None, 40), (255, 255, 255), (192, 192, 192), (124, 192, 255), screen)

    randomBodysNumber_textbox = textbox(200, 520, 50, 20, pygame.font.Font(None, 40), (255, 255, 255), (192, 192, 192), screen)

    randomBodysMass_textbox = textbox(200, 580, 50, 20, pygame.font.Font(None, 40), (255, 255, 255), (192, 192, 192), screen)
    
    randomBodys_button = Button(100, 640, 200, 50, "Add random bodies", pygame.font.Font(None, 30), (255, 255, 255), (192, 192, 192), (124, 192, 255), screen)

    deleteLastBody_button = Button(350, 1000, 200, 50, "Delete last body", pygame.font.Font(None, 30), (255, 255, 255), (192, 192, 192), (124, 192, 255), screen)

    # Creates a clock object allowing me to limit the frame rate.

    clock = pygame.time.Clock()
    clock.tick(60)

    while addBodyScreen:

        # Resetting the screen (taken from start screen function).

        screen.fill((0, 0, 0))
        
        # Drawing a line to separate the text at the top of the screen from the rest of the screen.

        pygame.draw.line(screen, (255, 255, 255), (0, 40), (1920, 40), 5)

        # Checking for events.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                addBodyScreen = False
                return False
            
            # r is my placeholder variable used to detect when a value is sent from the user.
            r = name_textbox.clicked(event) 
            if r != None:
                newBody_name = r
                name_label = (pygame.font.Font(None, 30)).render(("Name of the body: " + newBody_name), True, (255, 255, 255))

            # Detecting when a user sends a mass value.
            r = mass_textbox.clicked(event)
            if r != None:
                try: # Try lets us run a piece of code that may cause an error, and allows us to catch it and stop a big program crash.
                    newBody_mass = float(r)
                    mass_label = (pygame.font.Font(None, 30)).render("Mass of the body: " + r, True, (255, 255, 255))
                except ValueError:
                    mass_label = (pygame.font.Font(None, 30)).render("Mass of the body: Error, input numbers rather than letters", True, (255, 255, 255))

            # Detecting when the user sends a colour value.
            r = colour_textbox.clicked(event)
            if r != None:
                newBody_colour = r
                colour_label = (pygame.font.Font(None, 30)).render("Colour of the body: " + newBody_colour, True, (255, 255, 255))

            # Detecting when the user sends an x value (position)
            r = xPosition_textbox.clicked(event)
            if r != None:
                newBody_position_x = float(r)
                xPosition_label = (pygame.font.Font(None, 30)).render("X-coordinate of the body: " + r, True, (255, 255, 255))

            # Detecting when the user sends a y value (position)
            r = yPosition_textbox.clicked(event)
            if r != None:
                newBody_position_y = float(r)
                yPosition_label = (pygame.font.Font(None, 30)).render("Y-coordinate of the body: " + r, True, (255, 255, 255))

            # Detecting when the user sends an x value (velocity)
            r = xVelocity_textbox.clicked(event)
            if r != None:
                newBody_velocity_x = float(r)
                xVelocity_label = (pygame.font.Font(None, 30)).render("X-coordinate (velocity) of the body: " + r, True, (255, 255, 255))

            # Detecting when the user send a y value(velocity)
            r = yVelocity_textbox.clicked(event)
            if r != None:
                newBody_velocity_y = float(r)
                yVelocity_label = (pygame.font.Font(None, 30)).render("Y-coordinate (velocity) of the body: " + r, True, (255, 255, 255))

            # Detecting if the user sends a mass value to insert random bodies.
            r = randomBodysMass_textbox.clicked(event)
            if r != None:
                randomBody_mass = float(r)
                randomBodysMass_label = pygame.font.Font(None, 30).render("Mass of the random bodies: " + r, True, (255, 255, 255)) 
            
            # Detecting if the user sends a value for the number of bodies
            r = randomBodysNumber_textbox.clicked(event)
            if r != None:
                randomBody_number = int(r)
                randomBodysNumber_label = pygame.font.Font(None, 30).render("Number of random bodies: " + r, True, (255, 255, 255))

            # Detects if the user clicks the add body button.

            if addBody_button.clicked(event):

                # Creates the position and velocity vector objects ready to make the body object.

                newBody_position_vector = Vector(newBody_position_x, newBody_position_y)
                newBody_velocity_vector = Vector(newBody_velocity_x, newBody_velocity_y)

                # Creating the new body object.

                return Bodies(newBody_name, newBody_mass, newBody_colour, newBody_position_vector, newBody_velocity_vector) # All the values are validated in the bodies class.
            
            # Detects if the user clicks the random body button.

            if randomBodys_button.clicked(event):
                return add_random_bodies(randomBody_number)
            
            # Detects if the user clicks the delete last body button.

            if deleteLastBody_button.clicked(event):
                return "0"
        
        # Drawing objects onto the screen.

        screen.blit(title_text, text_position)
        screen.blit(name_label, name_label_position)
        name_textbox.draw_box()

        screen.blit(mass_label, mass_label_position)
        mass_textbox.draw_box()

        screen.blit(colour_label, colour_label_position)
        colour_textbox.draw_box()

        screen.blit(xPosition_label, xPosition_label_position)
        xPosition_textbox.draw_box()

        screen.blit(yPosition_label, yPosition_label_position)
        yPosition_textbox.draw_box()

        screen.blit(xVelocity_label, xVelocity_label_position)
        xVelocity_textbox.draw_box()

        screen.blit(yVelocity_label, yVelocity_label_position)
        yVelocity_textbox.draw_box()

        screen.blit(randomBodysMass_label, randomBodysMass_position)
        randomBodysMass_textbox.draw_box()

        screen.blit(randomBodysNumber_label, randomBodysNumber_position)
        randomBodysNumber_textbox.draw_box()

        randomBodys_button.draw_button()
        addBody_button.draw_button()
        deleteLastBody_button.draw_button()
            
        # Refreshes the entire screen

        pygame.display.flip()
