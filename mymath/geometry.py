from math import pi

def area_of_rectangle(length, width):
    """
    This function calculates the area of a rectangle given its length and width.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width

def area_of_circle(radius):
    """
    This function calculates the area of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return pi * (radius ** 2)
