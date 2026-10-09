def is_highfive(x):
    """
    Check if a is a "high five" -
    a number that's greater than 100 and divisible by 5

    :param a: a number
    :return: True / False
    """

    return x > 100 and x % 5 == 0
