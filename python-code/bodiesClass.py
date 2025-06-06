# Bodies Class

# Imports
from vectorsClass import Vector
from forceCalculation import force_calculation
import hashlib
import math # Used for radius calculation

# Colour dictionary

colourDictionary = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    # Add more colours in the future.
}

# Bodies Class
class Bodies():
    """
    Class for bodies, containing all the functions required to update acceleration, velocity and position.
    """
    def __init__(self, name, mass, colour, position, velocity):
        """
        Used to define the attributes and call validation methods.
        
        Attributes:
        name | The name of the body, designated by the user.
        identifier | The identifier, created by a hashing algorithm.
        mass | The mass of the body.
        size | The size of the body, calculated with an algorithm.
        colour | The colour of the body, defined by a dictionary.
        position | Vector describing the position of the body.
        velocity | Vector describing the velocity of the body.
        acceleration | Vector describing the velocity of the body.
        resultant_force | Vector describing the total force acting on the body.
        recent_positions | List storing the recent positions of the body, used to make a trail.
        """
        # Validate the parameters before assigning them.
        if not self.mass_validation(mass):
            raise ValueError("Mass value is invalid.")
        
        if not self.colour_validation(colour):
            raise ValueError("Colour is invalid.")
        
        if not self.name_validation(name):
            raise ValueError("Name is not a string.")
        
        vectors = [position, velocity]
        for i in range(0, 2):
            if not self.vector_validation(vectors[i]):
                raise ValueError("Position / Velocity is not a vector object.")

        # Assigning the parameters after validation.
        self.mass = mass
        self.colour = colour
        self.name = name
        self.initial_position = position
        self.initial_velocity = velocity
        self.position = position
        self.velocity = velocity
        self.acceleration = 0
        self.resultant_force = Vector(0.0, 0.0)
        self.recent_positions = []
        self.identifier = self.identifier_creation()
        self.radius = self.radius_calculation()
        self.potential_energy = 0
        self.kinetic_energy = 0
        self.total_energy = 0
    
    def colour_change(self, new_colour):
        if self.colour_validation(new_colour):
            self.colour = new_colour
        else:
            print("Colour is invalid.")

    def name_change(self, new_name):
        if self.name_validation(new_name):
            self.name = new_name
        else:
            print("Name is not a string.")

    def total_energy_calculation(self):
        """
        Calculates the total energy a body has.
        """
        self.total_energy = self.potential_energy + self.kinetic_energy

    def kinetic_energy_calculation(self):
        """
        Calculates the kinetic energy of the body.
        """
        self.kinetic_energy = 0.5 * self.mass * (self.velocity.magnitude() ** 2)

    def acceleration_calculation(self):
        """
        Uses Newton's Second Law to calculate the acceleration vector on a body after the resultant force has been calculated.
        """
        self.acceleration =  self.resultant_force.scalar_multiplication(1 / self.mass)

    def leapfrog_integration_initial(self, timestep):
        """
        This method is an adapted leapfrog integration to create the initial conditions required to use leapfrog integration.
        It is only called once for each body, during the first time-step.
        """
        velocity_half_step = self.velocity.vector_addition((self.acceleration.scalar_multiplication(0.5)).scalar_multiplication(timestep))
        self.position = self.position.vector_addition(velocity_half_step.scalar_multiplication(timestep))
        self.velocity = velocity_half_step

    def leapfrog_integration(self, timestep):
        """
        This method used leapfrog integration to find the position and velocity of a body every single time-step.
        """
        self.velocity = self.velocity.vector_addition(self.acceleration.scalar_multiplication(timestep))
        self.position = self.position.vector_addition(self.velocity.scalar_multiplication(timestep))

    def radius_calculation(self):
        """
        Finds the radius of a body.
        """
        return ((3 * self.mass) / (4 * math.pi * 3000)) ** (1/3)
    
    def identifier_creation(self):
        """
        Calculates the identifier using SHA256
        """
        position_mass_multipled = str(self.position.x_coordinate * self.position.y_coordinate * self.mass)
        before_hash = position_mass_multipled + self.name
        return (hashlib.sha256(before_hash.encode())).hexdigest() # Uses SHA256 to hash the string, .encode() to turn the string into its bytes and .hexdigest() to turn it into a hex representation.

    def resultant_force_update(self, new_force):
        """
        Updates the resultant force attribute of a body>
        """
        self.resultant_force = self.resultant_force.vector_addition(new_force)

    def mass_validation(self, number):
        """
        Checks that the mass is a float and is greater than 0.
        """
        if isinstance(number, float):
            if number > 0:
                return True
        return False
    
    def colour_validation(self, string):
        """
        Checks that the colour is a string, applies the .lower() function and checks that the string is defined in colourDictionary.
        """
        if isinstance(string, str):
            string1 = string.lower()
            if string1 in colourDictionary:
                return True
        return False
    
    def name_validation(self, string):
        """
        Checks that the name is a string.
        """
        if isinstance(string, str):
            return True
        return False
    
    def vector_validation(self, vector):
        """
        Checks that the parameter is a vector object.
        """
        if isinstance (vector, Vector):
            return True
        return False
