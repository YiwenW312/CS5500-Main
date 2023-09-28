"""This module demonstrates the use of classes and objects in Python."""
import random


class MObject:
    """A class to represent a generic object in a scene."""

    def __init__(self):
        pass


class Image:
    """
    A class to represent an image.
    """
    def __init__(self, w, h):
        print("Constructor called")
        self.m_width = w
        self.m_height = h
        self.m_colorChannels = 3  # Assume we support RGB channels only.
        self.m_Pixels = [random.randint(0, 255)
                         for _ in range(w * h * self.m_colorChannels)]

    # def __del__(self):
    # https://docs.python.org/3/reference/datamodel.html#object.__del__

    def getWidth(self):
        """Method to get the width of the image   
        Returns:
            int: width of the image
        """
        return self.m_width

    def getHeight(self):
        """
        Method to get the height of the image

        Returns:
            int: height of the image
        """
        return self.m_height

    def getPixelColorR(self, x, y):
        """
        Method to get the red color of the pixel at (x, y)

        Args:
            x (_type_): _description_
            y (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.m_Pixels[self.m_width * self.m_colorChannels * y + x]

    def getPixels(self):
        """
        Method to get the list of pixels

        Returns:
            _type_: _description_
        """
        return self.m_Pixels

    def setPixelsToRandomValue(self):
        """
        Method to set the pixels to a random value
        """
        value = random.randint(0, 255)
        # Set the entire list to one color in one function call
        self.m_Pixels = [value] * (self.m_width *
                                   self.m_height * self.m_colorChannels)


class Texture:
    """a class to represent a texture in a scene
    """
    def __init__(self, w, h):
        """
        Constructor

        Args:
            w 
            h 
        """
        self.image = Image(w, h)

    def getWidth(self):
        """
        Method to get the width of the texture

        Returns:
            int : width of the texture/image
        """
        return self.image.getWidth()

    def getHeight(self):
        """
        Method to get the height of the texture

        Returns:
            int : height of the texture/image
        """
        return self.image.getHeight()

    def getPixelColorR(self, x, y):
        """
        Method to get the red color of the pixel at (x, y)

        Args:
            x 
            y 

        Returns:
            int : red color of the pixel at (x, y)
        """
        return self.image.getPixelColorR(x, y)

    def getPixels(self):
        """
        Method to get the list of pixels

        Returns:
            _type_: _description_
        """
        return self.image.getPixels()

    def setPixelsToRandomValue(self):
        """
        Method to set the pixels to a random value
        """
        self.image.setPixelsToRandomValue()


def main():
    """
    Main function
    """
    random.seed()

    # Create a first image
    image1 = Image(100, 200)
    # Create a second image
    image2 = Image(image1.getWidth(), image1.getHeight())

    print(f"image1: {image1.getWidth()}, {image1.getHeight()}")
    print(f"image1 red color at (0, 0): {image1.getPixelColorR(0, 0)}")
    print(f"image2: {image2.getWidth()}, {image2.getHeight()}")
    print(f"image2 red color at (0, 0): {image2.getPixelColorR(0, 0)}")


if __name__ == "__main__":
    main()
