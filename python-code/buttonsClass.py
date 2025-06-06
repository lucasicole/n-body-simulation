# Button Class (for use in the GUI):

# Imports
import pygame

# Button Class

class Button:
    """
    This class creates an object for buttons, used in the GUI.
    """
    def __init__(self, x_coordinate, y_coordinate, length, width, text, text_font, text_colour, button_colour, hover_colour, screen):
        """
        Initialises the parameters.
        """
        self.button = pygame.Rect(0, 0, length, width) # Creates a rect object (rectangle) with the top-left corner 
        self.button.center = (x_coordinate, y_coordinate)
        self.text = text
        self.text_font = text_font
        self.text_colour = text_colour
        self.button_colour = button_colour
        self.hover_colour = hover_colour
        self.screen = screen # This is the screen that the button is being used on.

    def draw_button(self):
        """
        Draws the button onto the screen.
        """
        pygame.draw.rect(self.screen, self.button_colour, self.button) # Draws the button on the desired screen, in the desired colour and the correct size.#

        # Detecting if the mouse is hovering over the button, to adjust the colour.
        if self.button.collidepoint(pygame.mouse.get_pos()):
            text_current_colour = self.hover_colour
        else:
            text_current_colour = self.text_colour

        displayed_text = self.text_font.render(self.text, True, text_current_colour) # Displayed text is the rendered version of the text, with antialisaing and the text's colour.
        displayed_text_centre = displayed_text.get_rect(center = self.button.center)
        self.screen.blit(displayed_text, displayed_text_centre)
    
    def clicked(self, event):
        """
        Checks if the button has been clicked.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.button.collidepoint(pygame.mouse.get_pos()):
            return True
        return False
