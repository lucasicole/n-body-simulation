# Newton's Law of Universal Gravitation:

# Imports
from vectorsClass import Vector
import math

# Global variables:
#gravitational_constant = 6.6743e-11

# Function:
def force_calculation(mass_body1, mass_body2, position_body1, position_body2, radius_body1, gravitational_constant):
    """
    Calculates the attractive force acting on a body due to another body and the potential energy it has.
    """
    epsilon = 0.1
    displacement = position_body2.vector_subtraction(position_body1)
    displacement_squared = (displacement.magnitude())**2
    softened_distance = math.sqrt(displacement_squared + epsilon**2)
    constant_mass = gravitational_constant * mass_body1 * mass_body2 # Prevent operand errors with this line, allowing the use of scalar multiplication.
    force_body1 = ((displacement.scalar_multiplication(constant_mass)).scalar_multiplication(1 / softened_distance ** 3))
    potential_energy = -1 * constant_mass / softened_distance

    return force_body1, potential_energy
