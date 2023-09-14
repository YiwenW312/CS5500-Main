"""import enum"""
from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    """
    enum class Fruit
    Args:
        Enum (_type_): _description_
    """
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()


def main():
    """
    main() --> Does nothing special,
    define enumerations using the Enum base class
    """
    # enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # print the auto-generated value
    print(Fruit.PEAR.value)

    # enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA])


if __name__ == "__main__":
    main()
