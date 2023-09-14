# Demonstrate the use of variable argument lists


# define a function that takes variable arguments
def addition(*args):
    """
    addtion(*args) --> Returns the sum of all arguments.

    Returns:
        _type_: _description_
    """
    result = 0
    for arg in args:
        result += arg
    return result


def main():
    """main() --> Does nothing special, just prints the result of addition() function.
    """
    # TODO: pass different arguments
    print(addition(5, 10, 15, 20))
    print(addition(1, 2, 3))

    # TODO: pass an existing list
    myNums = [5, 10, 15, 20]
    print(addition(*myNums))

if __name__ == "__main__":
    main()
