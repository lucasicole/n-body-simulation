# Simulation Screen

# Imports

import pygame
from bodiesClass import Bodies, colourDictionary
from vectorsClass import Vector
from forceCalculation import force_calculation

# Simulation screen function

def simulation(screen, bodies_dict, timestep, gravitational_constant):
    """
    This function runs the simulation, calling the methods to calculate all the required information and displays it to the user.
    """

    simulation_running = True

    # If there are less than two or two bodies in the simulation we set the cameras position to the origin and the scale to 1.
    if len(bodies_dict) <= 2:
        scale_factor = 1
        camera_position = Vector(0.0, 0.0)
    elif len(bodies_dict) > 2:
        scale_factor = (1080 / max(bodies_dict.values(), key = lambda body: body.mass).radius) / 100 # Pixels per metre, we find the object of highest mass and adjust the scale factor so that the user can see the mass and the surrounding area when the simulation starts.
        camera_position = max(bodies_dict.values(), key = lambda body: body.mass).initial_position # Camera is initially at the centre of the largest object.

    iteration = 0
    time_simulated = timestep * iteration
    clock = pygame.time.Clock()
    screen_centre = Vector(960.0, 540.0)

    current_scale_text_position = (40, 1050) # The position of this text will never change therefore I don't need to initialise it every loop.
    current_camera_position_text_position = (40, 1030)
    current_timestep_text_position = (500, 1030)
    current_timestep_text = pygame.font.Font(None, 20).render("Timestep: " + str(timestep) + "s", True, (255, 255, 255))
    current_iteration_text = pygame.font.Font(None, 20).render("Iterations: " + str(iteration), True, (255, 255, 255))
    current_iteration_text_position = (700, 1030)
    current_time_simulated_text = pygame.font.Font(None, 20).render("Time simulated: " + str(time_simulated), True, (255, 255, 255))
    current_time_simulated_text_position = (900, 1030)

    pan_factor = 1 # The multiplier when panning the camera.
    
    def world_to_screen(world_position):
        """
        This nested function applies a transformation to the coordinates calculated, taking them from world coordinates to relevant camera coordinates
        """
        # I find the relative distance between the camera and the object.

        relative_position = world_position.vector_subtraction(camera_position)

        # We then apply the scale factor.

        screen_position_scaled = relative_position.scalar_multiplication(scale_factor)

        # Then we convert the world coordinates to screen coordinates and return the vector.

        return Vector((screen_centre.x_coordinate + screen_position_scaled.x_coordinate), (screen_centre.y_coordinate - screen_position_scaled.y_coordinate)) # Y is minus due to the flipping from Cartesian to screen.
    
    def screen_to_world(screen_position):
        """
        This nested function converts screen coordinates to world coordinates, used for labelling the axis.
        """
        # Finds the position relative to the centre of the screen.
        relative_position = Vector((screen_position.x_coordinate - screen_centre.x_coordinate), -(screen_position.y_coordinate - screen_centre.y_coordinate))

        # Divides by the scale factor.
        relative_position_world = relative_position.scalar_multiplication(1 / scale_factor)

        # Adds the cameras position to get the final world position.
        world_position = relative_position_world.vector_addition(camera_position)
        
        return world_position

    def in_screen_bounds(screen_position):
        """
        This nested function checks whether a bodies screen position is visible to the user - if not I skip rendering it to save resources.
        """
        if screen_position.x_coordinate < 0 or screen_position.x_coordinate > 1920:
            return False
        elif screen_position.y_coordinate < 0 or screen_position.y_coordinate > 1080:
            return False
        else:
            return True
        
    # For loop resetting the motion of the bodies.

    for i in bodies_dict.values():
        i.position = i.initial_position
        i.velocity = i.initial_velocity

    # A list storing consecutive arrow key presses, used for exponetial camera panning.

    key_presses = []
    while simulation_running:
        """
        Main loop for the simulation.
        """
        # Handling events first:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                simulation_running = False
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN: # Using exponential zooming.
                if event.button == 4: # Scroll wheel up, zoom in
                    scale_factor *= 1.1
                elif event.button == 5: # Scroll wheel down, zoom out
                    scale_factor /= 1.1
            elif event.type == pygame.KEYDOWN: # Checking if the user presses up, down, left, or right. If statements are used for exponential panning.
                if event.key == pygame.K_UP:
                    if len(key_presses) == 0:
                        key_presses.append(1)
                    else:
                        if key_presses[0] == 1:
                            key_presses.append(1)
                            pan_factor = len(key_presses)
                        else:
                            key_presses = []
                            pan_factor = 1
                    camera_position = camera_position.vector_addition(Vector(0.0, 1.0 * pan_factor * (1 / scale_factor)))
                elif event.key == pygame.K_DOWN:
                    if len(key_presses) == 0:
                        key_presses.append(2)
                    else:
                        if key_presses[0] == 2:
                            key_presses.append(2)
                            pan_factor = len(key_presses)
                        else:
                            key_presses = []
                            pan_factor = 1
                    camera_position = camera_position.vector_addition(Vector(0.0, -1.0 * pan_factor * (1 / scale_factor)))
                elif event.key == pygame.K_LEFT:
                    if len(key_presses) == 0:
                        key_presses.append(3)
                    else:
                        if key_presses[0] == 3:
                            key_presses.append(3)
                            pan_factor = len(key_presses)
                        else:
                            key_presses = []
                            pan_factor = 1
                    camera_position = camera_position.vector_addition(Vector(-1.0 * pan_factor * (1 / scale_factor), 0.0))
                elif event.key == pygame.K_RIGHT:
                    if len(key_presses) == 0:
                        key_presses.append(4)
                    else:
                        if key_presses[0] == 4:
                            key_presses.append(4)
                            pan_factor = len(key_presses)
                        else:
                            key_presses = []
                            pan_factor = 1
                    camera_position = camera_position.vector_addition(Vector(1.0 * pan_factor * (1 / scale_factor), 0.0))
        # Resetting the screen

        screen.fill((0, 0, 0))

        # For loop resetting the resultant force on the bodies.

        for i in bodies_dict.values():
            i.resultant_force = Vector(0.0, 0.0)
            i.potential_energy = 0

        total_simulation_energy = 0

        # For loop iterating through the bodies dictionary, then another for loop for each body again calculating the forces and then the motion of the body.

        i_loop_count = -1 # Indexing starts at 0

        for i in bodies_dict.values():
            i_loop_count += 1
            j_loop_count = -1
            for j in bodies_dict.values():
                j_loop_count += 1
                if i_loop_count == j_loop_count:
                    continue
                elif j_loop_count < i_loop_count: # If i is less than j we have already calculated the force through Newton's Third Law.
                    continue
                else:
                    current_force, potential_energy = force_calculation(i.mass, j.mass, i.position, j.position, i.radius, gravitational_constant)
                    i.resultant_force_update(current_force)
                    i.potential_energy = i.potential_energy + potential_energy
                    j.resultant_force_update(current_force.scalar_multiplication(-1)) # Newton's Third Law, so the force is equal and opposite for body j.
                    j.potential_energy = j.potential_energy + potential_energy

            # After the resultant force has been calculated, we calculate the motion of the particle.

            i.acceleration_calculation()
            if iteration == 0:
                i.leapfrog_integration_initial(timestep)
            else:
                i.leapfrog_integration(timestep)
            i.kinetic_energy_calculation()
            i.total_energy_calculation()

            total_simulation_energy += i.total_energy

            # We then decide if we are going to render this object or cull it.
            body_screen_position = world_to_screen(i.position)
            current_radius = i.radius * scale_factor
            
            # Ensuring that all visible bodies are rendered, even if theyre too small.

            if current_radius < 3:
                current_radius = 3

            if current_radius > 1080:
                pass # Used when you don't want to execute any code.
            elif in_screen_bounds(body_screen_position):
                pygame.draw.circle(screen, colourDictionary[i.colour], (body_screen_position.x_coordinate, body_screen_position.y_coordinate), current_radius, 0) # Creates a circle with the correct colour, position and radius (multiplied by the scale factor for zooming in and out), with a width of 0 (filled)

        print("System energy: " + str(total_simulation_energy) + " at iteration " + str(iteration) + ".")

        # Rendering the UI displaying information to the user, such as the current scale factor and the position of the camera.

        current_scale_text = (pygame.font.Font(None, 20)).render("Metres per pixel: " + str(1 / scale_factor), True, (255, 255, 255)) # This has to be updated incase the user zooms in and out.
        current_camera_position_text = (pygame.font.Font(None, 20)).render("Camera position: " + str(camera_position.x_coordinate) + ", " + str(camera_position.y_coordinate), True, (255, 255, 255))
        current_iteration_text = pygame.font.Font(None, 20).render("Iterations: " + str(iteration), True, (255, 255, 255))
        time_simulated = timestep * iteration
        current_time_simulated_text = pygame.font.Font(None, 20).render("Time simulated: " + str(time_simulated), True, (255, 255, 255))

        pygame.draw.line(screen, (255, 255, 255), (30, 1015), (30, 0), 3) # Draws a vertical line used for the vertical scale of the screen.
        pygame.draw.line(screen, (255, 255, 255), (30, 1015), (1920, 1015), 3) # Draws a horizontal line used for the horizontal scale of the screen.

        # For loop drawing lines onto the scale along with the text telling the user the scale.

        for i in range(10):
            multiplier = i * 100
            pygame.draw.line(screen, (255, 255, 255), (60 + (multiplier * 2), 1025), (60 + (multiplier * 2), 1005), 3)
            screen.blit(pygame.font.Font(None, 15).render(str(screen_to_world(Vector((60.0 + (multiplier * 2)), 0.0)).x_coordinate), True, (255, 255, 255)), (60 + (multiplier * 2), 990))

            pygame.draw.line(screen, (255, 255, 255), (20, 940 - multiplier), (40, 940 - multiplier))
            screen.blit(pygame.font.Font(None, 15).render(str(screen_to_world(Vector(0.0, (940.0 - multiplier))).y_coordinate), True, (255, 255, 255)), (55, (940 - multiplier)))

        screen.blit(current_scale_text, current_scale_text_position)
        screen.blit(current_camera_position_text, current_camera_position_text_position)
        screen.blit(current_timestep_text, current_timestep_text_position)
        screen.blit(current_iteration_text, current_iteration_text_position)
        screen.blit(current_time_simulated_text, current_time_simulated_text_position)

        clock.tick(120)
        pygame.display.flip()
        iteration += 1
