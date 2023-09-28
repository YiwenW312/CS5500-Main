# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- Mobject is a concrete class because it is not defined with Abstract Base classes(ABC) and in Python, a method becomes abstract when decorated with the keyword @abstractmethod.
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- As it's currently commented out, it won't have any effect. If it were active and had actual code inside, that code would be executed whenever an Image object was about to be destroyed.The Commented URL provided in the comment is a link to Python's official documentation, specifically to the section detailing the __del__ method. This link is likely included as a reference or note to explain the purpose and behavior of the __del__ method.
	- the commented-out __del__ method in the provided Image class serves as a placeholder or a note about the destructor method. It is called when an object is about to be destroyed, which usually occurs when the object is no longer referenced in the program or the program terminates. It can be used to release external resources or perform cleanup activities.
1. What class does Texture inherit from?
	- from Image Class
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- it inherits all the methods and attributes that are defined in the Image class. Attributes: m_width, m_height, m_colorChannels, m_Pixels. Methods: __init__(self, w, h), getWidth(self), getHeight(self), getPixelColorR(self, x, y), getPixels(self), setPixelsToRandomValue(self).
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- I consider a texture should have a "has-a" (conposition) relationship with "Image". Composition offers more flexibility and aligns well with the likely future complexities of a Texture. If in the future you wanted the Texture to have multiple images for different mipmap levels or additional attributes like normal maps, specular maps, etc., the composition approach would make more sense. Inheritance would tie the Texture strictly as a type of Image, which could become problematic if the distinction between them becomes more pronounced in future developments. Furthermore, composition reduces the tight coupling between the classes, promoting better software design principles.
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Yes, Python provides a default constructor for classes that do not define their own. This default constructor does not perform any actions, and its primary role is to allow the creation of an instance of the class without errors.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

*edit the code directly*  
  
