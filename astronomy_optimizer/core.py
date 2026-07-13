"""
Module providing the core functionality of the Astronomy Parameter Optimizer.

This module contains the main domain logic and public entry points for the optimizer.
It is designed to be self-contained, using only pure Python standard library features.
"""

import itertools
import random
import math


def grid_search(params, bounds):
    """
    Perform a grid search over the given parameter space.

    Args:
        params (list): List of parameters to optimize.
        bounds (dict): Dictionary mapping each parameter to its bounds.

    Returns:
        dict: Best set of parameters found by the search.
    """
    if not bounds or not all(len(b) == 2 for b in bounds.values()):
        raise ValueError("Invalid bounds")

    best_params = None
    best_score = float('-inf')
    for p in itertools.product(*[range(b[0], b[1] + 1) for b in bounds.values()]):
        score = _evaluate(params, dict(zip(bounds.keys(), p)))
        if score > best_score:
            best_score = score
            best_params = dict(zip(bounds.keys(), p))
    return best_params


def random_search(params, bounds, num_samples):
    """
    Perform a random search over the given parameter space.

    Args:
        params (list): List of parameters to optimize.
        bounds (dict): Dictionary mapping each parameter to its bounds.
        num_samples (int): Number of random samples to generate.

    Returns:
        dict: Best set of parameters found by the search.
    """
    if not isinstance(num_samples, int) or num_samples <= 0:
        raise ValueError("Invalid number of samples")

    best_params = None
    best_score = float('-inf')
    for _ in range(num_samples):
        p = {k: random.randint(b[0], b[1]) for k, b in bounds.items()}
        score = _evaluate(params, dict(zip(bounds.keys(), p)))
        if score > best_score:
            best_score = score
            best_params = dict(zip(bounds.keys(), p))
    return best_params


def simulated_annealing_search(params, bounds, initial_temperature):
    """
    Perform a simulated annealing search over the given parameter space.

    Args:
        params (list): List of parameters to optimize.
        bounds (dict): Dictionary mapping each parameter to its bounds.
        initial_temperature (float): Initial temperature for the search.

    Returns:
        dict: Best set of parameters found by the search.
    """
    if not isinstance(initial_temperature, (int, float)) or initial_temperature <= 0:
        raise ValueError("Invalid initial temperature")

    best_params = None
    best_score = float('-inf')
    current_params = {k: random.randint(b[0], b[1]) for k, b in bounds.items()}
    current_temperature = initial_temperature
    while current_temperature > 1e-6:
        new_params = _perturb(current_params)
        score = _evaluate(params, dict(zip(bounds.keys(), new_params)))
        if score > best_score:
            best_score = score
            best_params = new_params
        elif random.random() < math.exp((best_score - score) / current_temperature):
            current_params = new_params
        current_temperature *= 0.99  # cooling schedule
    return best_params


def _evaluate(params, values):
    """
    Evaluate the given parameters using the provided values.

    Args:
        params (list): List of parameters to optimize.
        values (dict): Dictionary mapping each parameter to its value.

    Returns:
        float: Score for the given set of parameters.
    """
    # TO DO: implement evaluation function
    return sum(values.values()) / len(values)


def _perturb(params):
    """
    Perturb the given parameters by a small amount.

    Args:
        params (dict): Dictionary mapping each parameter to its value.

    Returns:
        dict: Perturbed set of parameters.
    """
    perturbed_params = {}
    for k, v in params.items():
        if random.random() < 0.1:  # 10% chance of perturbation
            perturbed_params[k] = max(0, min(v + random.randint(-5, 5), 100))  # adjust range to [0, 100]
    return perturbed_params


def _check_bounds(bounds):
    """
    Check if the given bounds are valid.

    Args:
        bounds (dict): Dictionary mapping each parameter to its bounds.

    Returns:
        None
    """
    if not bounds or not all(len(b) == 2 for b in bounds.values()):
        raise ValueError("Invalid bounds")


def _check_initial_temperature(initial_temperature):
    """
    Check if the given initial temperature is valid.

    Args:
        initial_temperature (float): Initial temperature for the search.

    Returns:
        None
    """
    if not isinstance(initial_temperature, (int, float)) or initial_temperature <= 0:
        raise ValueError("Invalid initial temperature")
