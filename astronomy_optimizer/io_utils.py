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
            a row in the CSV file. If the file is empty or does not exist,
            an empty list is returned.
    """
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        raise

def write_csv(filename: str, data: List[Dict[str, str]]) -> None:
    """
    Writes a list of dictionaries to a CSV file.

    Args:
        filename (str): The name of the CSV file.
        data (List[Dict[str, str]]): A list of dictionaries where each dictionary
            represents a row in the CSV file. If the input list is empty,
            an empty file will be created.
    """
    if not data:
        print("Warning: Writing an empty CSV file.")
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
            text file. If the file is empty or does not exist, an empty list
            is returned.
    """
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading text file: {e}")
        raise

def write_text(filename: str, data: List[str]) -> None:
    """
    Writes a list of strings to a text file.

    Args:
        filename (str): The name of the text file.
        data (List[str]): A list of strings where each string represents a line
            in the text file. If the input list is empty, an empty file will be
            created.
    """
    if not data:
        print("Warning: Writing an empty text file.")
    with open(filename, 'w') as f:
        for line in data:
            f.write(line + '\n')

def read_csv_or_text(filename: str) -> List[str]:
    """
    Attempts to read a CSV or text file into a list of strings.

    Args:
        filename (str): The name of the file to read.

    Returns:
        List[str]: A list of strings where each string represents a line in the
            file. If the file does not exist, an empty list is returned.
    """
    if filename.endswith('.csv'):
        return read_csv(filename)
    elif filename.endswith('.txt') or filename.endswith('.text'):
        return read_text(filename)
    else:
        print(f"Unsupported file type: {filename}")
        return []

def write_csv_or_text(filename: str, data: List[str]) -> None:
    """
    Attempts to write a list of strings to a CSV or text file.

    Args:
        filename (str): The name of the file to write.
        data (List[str]): A list of strings where each string represents a line
            in the file. If the input list is empty, an empty file will be created.
    """
    if filename.endswith('.csv'):
        write_csv(filename, [{'key': 'value'} if not data else data])
    elif filename.endswith('.txt') or filename.endswith('.text'):
        write_text(filename, data)
    else:
        print(f"Unsupported file type: {filename}")
