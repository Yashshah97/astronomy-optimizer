"""
Module for computation and analysis helpers.

This module contains functions to perform common astronomical computations
and analyses. These functions are designed to be used in conjunction with the
parameter optimizer.
"""

import math
from typing import List, Tuple

def calculate_distance(ra1: float, dec1: float, ra2: float, dec2: float) -> float:
    """
    Calculate the distance between two points on a sphere (e.g., celestial coordinates).

    :param ra1: Right ascension of point 1 in radians.
    :param dec1: Declination of point 1 in radians.
    :param ra2: Right ascension of point 2 in radians.
    :param dec2: Declination of point 2 in radians.
    :return: Distance between the two points on a sphere.
    """
    d_ra = math.radians(ra2 - ra1)
    d_dec = math.radians(dec2 - dec1)
    a = math.sin(d_dec / 2) ** 2 + math.cos(math.radians(dec1)) * math.cos(math.radians(dec2)) * math.sin(d_ra / 2) ** 2
    return 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def calculate_magnitude(mag: float, distance: float) -> float:
    """
    Calculate the apparent magnitude of an object given its absolute magnitude and distance.

    :param mag: Absolute magnitude of the object.
    :param distance: Distance to the object in parsecs.
    :return: Apparent magnitude of the object.
    """
    return mag + 5 * math.log10(distance)

def calculate_uncertainty(values: List[float], confidence_level: float = 0.95) -> Tuple[float, float]:
    """
    Calculate the mean and standard deviation of a list of values.

    :param values: List of values to calculate the mean and standard deviation for.
    :param confidence_level: Confidence level (default is 95%).
    :return: Mean and standard deviation of the input values.
    """
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    std_dev = math.sqrt(variance)
    return mean, std_dev
