"""
Module for human-readable output formatting.

This module provides functions to format the results of optimization processes in a way that is easy to read and understand.
"""

def format_result(result):
    """
    Format the result dictionary into a string.

    Args:
        result (dict): The result dictionary containing parameters and their values.

    Returns:
        str: A human-readable representation of the result.

    Raises:
        TypeError: If `result` is not a dict.
    """
    if not isinstance(result, dict):
        raise TypeError("Result must be a dictionary")
    
    formatted = "Optimization Result:\n"
    for key, value in result.items():
        formatted += f"{key}: {value}\n"
    return formatted

def format_grid_result(result):
    """
    Format a grid search result into a string.

    Args:
        result (dict): The result dictionary containing parameters and their values.

    Returns:
        str: A human-readable representation of the result.
    """
    return format_result(result)

def format_annealing_result(result):
    """
    Format a simulated annealing search result into a string.

    Args:
        result (dict): The result dictionary containing parameters and their values.

    Returns:
        str: A human-readable representation of the result.
    """
    return format_result(result)
