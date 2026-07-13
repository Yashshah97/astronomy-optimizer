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
        title (str, optional): A custom title to use instead of "Optimization Result". Defaults to None.

    Returns:
        str: A human-readable representation of the result.
    """
    title = "Grid Search Result"
    if isinstance(result.get("title"), str):
        title = result["title"]
    return format_result({"title": title, **result})

def format_annealing_result(result):
    """
    Format a simulated annealing search result into a string.

    Args:
        result (dict): The result dictionary containing parameters and their values.
        temperature (float, optional): The final temperature of the annealing process. Defaults to None.

    Returns:
        str: A human-readable representation of the result.
    """
    formatted = format_result(result)
    if "temperature" in result and result["temperature"] is not None:
        formatted += f"\nFinal Temperature: {result['temperature']}"
    return formatted
