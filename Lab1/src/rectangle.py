from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def set_values(self, x, y):
        pass

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_values(self, x, y):
        self.__width = x
        self.__height = y

    def area(self):
        return self.__width * self.__height

    # Getter and setter for width and height if needed
    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle(3, 4)

    # Print out the area function
    print("area:", rect.area())
