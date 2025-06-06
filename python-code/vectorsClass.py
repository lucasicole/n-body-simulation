# Imports
import math # Used for the square root function.

# Vectors Class
class Vector():
    """
    Class for vector objects, containing all necessary vector operations.
    """
    def __init__(self, x_coordinate, y_coordinate):
        """
        Defines the specific instance's attributes (the x and y coordinates)

        Attributes:
        x_coordinate | The value of the vector in the x / horizontal axis
        y_coordinate | The value of the vector in the y / vertical axis.
        """
        # Validating the parameters before assigning them.
        if not self.parameter_validation(x_coordinate, y_coordinate):
            raise ValueError("Parameter values are invalid.") # ValueError raises an error and terminates the code while sending an error message stating why it happened.

        self.x_coordinate = x_coordinate # This assigns the x_coordinate parameter to the instance's x_coordinate attribute.
        self.y_coordinate = y_coordinate

    def parameter_validation(self, x_coordinate, y_coordinate):
        """
        This method validates the inputs for the vector.
        - It checks that the value is a float
        - It checks that the value is within a range or -1x10^100 < x < 1x10^100
        - It checks that the value is not none / empty.
        """
        def check(number):
            """
            This sub-method is used to validate the parameters
            """
            if isinstance(number, float): # isinstance checks that the parameter is of the same class as a float. Float is a built-in object in Python.
                if -1e100 < number < 1e100:
                    return True
            return False
        
        # Send the x_coordinate to the check sub-method.
        if not check(x_coordinate):
            return False
        
        # Send the y_coordinate to the check sub-method.
        if not check(y_coordinate):
            return False
        
        return True
    
    def vector_addition(self, second_vector):
        """
        Create a new vector by summing the components of two individual vectors.
        """
        new_x = self.x_coordinate + second_vector.x_coordinate
        new_y = self.y_coordinate + second_vector.y_coordinate
        return Vector(new_x, new_y)
    
    def vector_subtraction(self, second_vector):
        """
        Create a new vector by subtracting the components of two individual vectors.
        """
        new_x = self.x_coordinate - second_vector.x_coordinate
        new_y = self.y_coordinate - second_vector.y_coordinate
        return Vector(new_x, new_y)
    
    def scalar_multiplication(self, scalar):
        """
        Multiplying a vector by a scalar value.
        """
        new_x = self.x_coordinate * scalar
        new_y = self.y_coordinate * scalar
        return Vector(new_x, new_y)
    
    def magnitude(self):
        """
        Finds the magnitude of a vector.
        """
        return math.sqrt((self.x_coordinate ** 2) + (self.y_coordinate ** 2))
    
    def string_conversion(self):
        """
        Converts the components into a string and outputs it to the user.
        """
        return "X-component: " + str(self.x_coordinate) + " | Y-component: " + str(self.y_coordinate)
