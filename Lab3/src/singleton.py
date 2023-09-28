""" This module implements the Logger class as a singleton class."""


class Logger:
    """
    A singleton class that allows adding messages to a list of messages.

    This class ensures that only one instance of the Logger class is created
    throughout the lifetime of the program. The instance can be accessed using
    the `instance` class method.

    Attributes:
        messages (list): A list of messages added to the logger.
    """

    _instance = None  # Private class variable to hold the single instance

    def __init__(self):
        """
        Private method to initialize the instance of the Logger class.
        This method is called only once when the instance is created.
        """
        self.messages = []

    @classmethod
    def instance(cls):
        """Class method to get the single instance
        Attributes:
            cls
        """
        if cls._instance is None:
            cls._instance = cls()  # Creating an instance
            # cls._instance.__init__()  # Initializing the instance
            print("Logger created exactly once")
        else:
            print("logger already created")
        return cls._instance

    def add_message(self, message):
        """Method to add a message to the list of messages

        Args:
            message
        """
        self.messages.append(message)


def main():
    """
    Main function to test the Logger class
    """
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    for i in range(3):
        logger = Logger().instance()
        logger.add_message(f"Adding message number: {i}")


if __name__ == "__main__":
    main()
