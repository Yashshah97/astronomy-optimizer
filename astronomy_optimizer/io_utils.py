"""
Module for handling input/output operations.

This module provides functions to read and write data in various formats.
"""

import csv
from typing import List, Dict

def read_csv(filename: str) -> List[Dict[str, str]]:
    """
    Reads a CSV file into a list of dictionaries.

    Args:
        filename (str): The name of the CSV file.

    Returns:
        List[Dict[str, str]]: A list of dictionaries where each dictionary represents
            a row in the CSV file.
    """
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def write_csv(filename: str, data: List[Dict[str, str]]) -> None:
    """
    Writes a list of dictionaries to a CSV file.

    Args:
        filename (str): The name of the CSV file.
        data (List[Dict[str, str]]): A list of dictionaries where each dictionary
            represents a row in the CSV file.
    """
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def read_text(filename: str) -> List[str]:
    """
    Reads a text file into a list of strings.

    Args:
        filename (str): The name of the text file.

    Returns:
        List[str]: A list of strings where each string represents a line in the
            text file.
    """
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def write_text(filename: str, data: List[str]) -> None:
    """
    Writes a list of strings to a text file.

    Args:
        filename (str): The name of the text file.
        data (List[str]): A list of strings where each string represents a line
            in the text file.
    """
    with open(filename, 'w') as f:
        for line in data:
            f.write(line + '\n')
