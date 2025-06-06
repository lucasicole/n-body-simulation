# Textbox Class:

# Imports
 
import pygame

class textbox:

    def __init__(self, x_coordinate, y_coordinate, width, max_characters, text_font, text_colour, button_colour,screen):
        """
        Initialises the object.
        """
        self.textbox = pygame.Rect(0, 0, max_characters * 20, width)
        self.textbox.center = (x_coordinate, y_coordinate)
        self.text = ''
        self.text_font = text_font
        self.text_colour = text_colour
        self.button_colour = button_colour
        self.screen = screen
        self.active = False # Boolean flag used to check if the user has clicked on the textbox, and will allow them to type.
        self.max_characters = max_characters

    def draw_box(self):
        """
        Draws the text box and overlays the text on-top.
        """
        pygame.draw.rect(self.screen, self.button_colour, self.textbox)

        # Overlaying the text.
        
        displayed_text = self.text_font.render(self.text, True, self.text_colour) # Displayed text is the rendered version of the text, with antialisaing and the text's colour.
        displayed_text_centre = displayed_text.get_rect(center = self.textbox.center)
        self.screen.blit(displayed_text, displayed_text_centre)

    def clicked(self, event):
        """
        Checks if the textbox has been clicked.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.textbox.collidepoint(pygame.mouse.get_pos()):
            self.active = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not self.textbox.collidepoint(pygame.mouse.get_pos()):
            self.active = False
            self.text = ''
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_ESCAPE:
                    self.active = False
                    self.text = ''
                elif event.key == pygame.K_RETURN:
                    self.active = False
                    return_text = self.text
                    self.text = ''
                    return return_text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) == self.max_characters:
                        return
                    else:
                        self.text += event.unicode # This will add the character to the string.
