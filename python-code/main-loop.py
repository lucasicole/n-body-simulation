# Main game loop

# Imports and initialisation
import pygame
pygame.init()
from startScreen import start_screen
from addbodyScreen import add_body_screen
from bodiesClass import Bodies
from simulationSetup import simulation_set_up
from simulationScreen import simulation

# Initialising the window

initial_window = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("N-body Simulation: Lucas Cole")

# Dictionary storing each body with the hash as the key.

bodies_dict = {

}

# The main loop - where everything happens.

running = True
startScreen = True
addBodyScreen = False
simulationSetupScreen = False
simulationScreen = False

while running:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
              running = False

     if startScreen:
          r = start_screen(initial_window)
          if not r:
               running = False
          elif r == 1:
               startScreen = False
               addBodyScreen = True
          elif r == 2:
               startScreen = False
               simulationSetupScreen = True


     if addBodyScreen:
          r = add_body_screen(initial_window)
          if not r:
               addBodyScreen = False
               startScreen = True
          elif isinstance(r, Bodies):
               bodies_dict[r.identifier] = r
               addBodyScreen = False
               startScreen = True
          elif isinstance(r, list):
               for i in range(len(r)):
                    bodies_dict[r[i].identifier] = r[i]
               addBodyScreen = False
               startScreen = True
          elif r == "0":
               bodies_dict.popitem()
               addBodyScreen = False
               startScreen = True

     if simulationSetupScreen:
          r = simulation_set_up(initial_window, bodies_dict)
          if not r:
               simulationSetupScreen = False
               startScreen = True
          elif r[0] == 1:
               simulationSetupScreen = False
               simulationScreen = True
               timestep = r[1]
               gravitational_constant = r[2]

     if simulationScreen:
          r = simulation(initial_window, bodies_dict, timestep, gravitational_constant)
          if not r:
               simulationScreen = False
               simulationSetupScreen = True

pygame.quit()
