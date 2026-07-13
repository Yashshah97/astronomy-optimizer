"""
Configuration loader for Astronomy Parameter Optimizer.

This module provides a simple way to load configuration parameters from various sources,
with default values in case of missing or invalid configuration.
"""

import os
from typing import Any, Dict

class Config:
    """
    Configuration class for loading and managing configuration parameters.
    
    Attributes:
        config (dict): Dictionary containing configuration parameters.
        
    Methods:
        load_config: Load configuration parameters from a file.
        get: Retrieve the value of a specific configuration parameter.
    """

    def __init__(self) -> None:
        """
        Initialize the Config class with default configuration values.
        """
        self.config = {
            'search_strategy': 'grid',
            'num_iterations': 1000,
            'population_size': 50,
            'temperature': 1.0,
            'cooling_rate': 0.9,
            'mutation_rate': 0.01
        }
        self.load_config()

    def load_config(self) -> None:
        """
        Load configuration parameters from a file specified by the ASTRONOMY_OPTIMIZER_CONFIG_FILE environment variable.
        
        If the variable is not set, default values are used.
        
        Raises:
            FileNotFoundError: If the configuration file does not exist.
            ValueError: If the configuration file has invalid syntax.
        """
        config_file = os.environ.get('ASTRONOMY_OPTIMIZER_CONFIG_FILE')
        if config_file and os.path.isfile(config_file):
            try:
                with open(config_file, 'r') as f:
                    for line in f.readlines():
                        key, value = line.strip().split('=')
                        self.config[key] = eval(value)
            except FileNotFoundError:
                print(f"Configuration file '{config_file}' not found.")
            except SyntaxError as e:
                print(f"Invalid configuration syntax: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve the value of a specific configuration parameter.

        Args:
            key (str): Configuration parameter key.
            default (any, optional): Default value to return if the key is not found. Defaults to None.

        Returns:
            any: Value of the specified configuration parameter or the default value.
        """
        return self.config.get(key, default)


# Create a singleton instance of the Config class
config = Config()
