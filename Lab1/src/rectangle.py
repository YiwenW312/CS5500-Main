# import the abstract base class module
from abc import ABC, abstractmethod

# Create a class called Shape that is an abstract base class
class Shape(ABC):
    # Create an abstract method called set_values
    @abstractmethod
    def set_values(self, x, y):
        pass
    # Create an abstract method called area
    @abstractmethod
    def area(self):
        pass

# Create a class called Rectangle that inherits from Shape
class Rectangle(Shape):
    # Create a constructor that takes in width and height, and sets them to private variables
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    # Create a method called set_values that sets the width and height
    def set_values(self, x, y):
        self.__width = x
        self.__height = y

    # Create a method called area that returns the area of the rectangle
    def area(self):
        return self.__width * self.__height

    # Getter for width
    def get_width(self):
        return self.__width

    # Setter for width
    def set_width(self, width):
        self.__width = width

    # Getter for height
    def get_height(self):
        return self.__height

    # Setter for height
    def set_height(self, height):
        self.__height = height

# Main function
if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle(3, 4)

    # Print out the area function
    print("area:", rect.area())
