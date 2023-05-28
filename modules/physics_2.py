from physics import CONSTANTS


def height(t):
    if t > 10:
        CONSTANTS["G"] = 10
    return (CONSTANTS["G"] * (t ** 2)) / 2