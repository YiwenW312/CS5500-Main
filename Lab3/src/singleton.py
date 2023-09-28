class Logger:
    _instance = None  # Private class variable to hold the single instance

    def __private_init(self): 
        self.messages = []

    @classmethod
    def instance(cls):  # Class method to get the single instance
        if cls._instance is None:
            cls._instance = cls()  # Creating an instance
            cls._instance.__private_init()  # Initializing the instance
            print("Logger created exactly once")
        else:
            print("logger already created")
        return cls._instance

    def add_message(self, message):
        self.messages.append(message)


def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")


if __name__ == "__main__":
    main()
