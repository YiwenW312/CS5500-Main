# Demonstrate the usage of namdtuple objects

import collections


def main():
    """
    main() --> Does nothing special, just prints the result of addition() function.
    """
    # create a Point namedtuple
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1, p2)
    print(p1.x, p1.y)
    print(p2.x, p2.y)
    # use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1)


if __name__ == "__main__":
    main()
