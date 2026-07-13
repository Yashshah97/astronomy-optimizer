"""
Module for input validation and error types.

This module provides functions to validate inputs and define custom error types.
"""

class AstronomyError(Exception):
    """Base class for all astronomy-related errors."""
    pass


class InvalidInput(AstronomyError):
    """Raised when the input is invalid or malformed."""
    def __init__(self, message):
        super().__init__(message)


def _validate_positive_integer(value, name):
    """
    Validate that a value is a positive integer.

    Args:
        value: The value to validate.
        name: The name of the value (used in error messages).

    Raises:
        InvalidInput: If the value is not a positive integer.
    """
    if not isinstance(value, int) or value <= 0:
        raise InvalidInput(f"{name} must be a positive integer")


def _validate_non_negative_integer(value, name):
    """
    Validate that a value is a non-negative integer.

    Args:
        value: The value to validate.
        name: The name of the value (used in error messages).

    Raises:
        InvalidInput: If the value is not a non-negative integer.
    """
    if not isinstance(value, int) or value < 0:
        raise InvalidInput(f"{name} must be a non-negative integer")


def _validate_float(value, name):
    """
    Validate that a value is a float.

    Args:
        value: The value to validate.
        name: The name of the value (used in error messages).

    Raises:
        InvalidInput: If the value is not a float.
    """
    if not isinstance(value, float):
        raise InvalidInput(f"{name} must be a float")


def _validate_string(value, name):
    """
    Validate that a value is a string.

    Args:
        value: The value to validate.
        name: The name of the value (used in error messages).

    Raises:
        InvalidInput: If the value is not a string.
    """
    if not isinstance(value, str):
        raise InvalidInput(f"{name} must be a string")
