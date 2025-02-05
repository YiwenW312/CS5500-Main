# Use lambdas as in-place functions


def CelsisusToFahrenheit(temp):
    """CelsisusToFahrenheit(temp) --> Converts Celsisus to Fahrenheit.

    Args:
        temp (_type_): _description_

    Returns:
        _type_: _description_
    """
    return (temp * 9/5) + 32


def FahrenheitToCelsisus(temp):
    """FahrenheitToCelsisus(temp) --> Converts Fahrenheit to Celsisus.

    Args:
        temp (_type_): _description_

    Returns:
        _type_: _description_
    """
    return (temp-32) * 5/9


def main():
    """
    main() --> Does nothing special, just prints the result of addition() function.
    """
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # Use regular functions to convert temps
    print(list(map(FahrenheitToCelsisus, ftemps)))
    print(list(map(CelsisusToFahrenheit, ctemps)))

    # Use lambdas to accomplish the same thing
    print(list(map(lambda t: (t-32) * 5/9, ftemps)))
    print(list(map(lambda t: (t * 9/5) + 32, ctemps)))


if __name__ == "__main__":
    main()
