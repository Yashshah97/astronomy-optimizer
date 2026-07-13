"""
Configuration loader for Astronomy Parameter Optimizer.

This module provides a simple way to load configuration parameters from various sources,
with default values in case of missing or invalid configuration.
"""

import os

class Config:
    def __init__(self):
        self.config = {
            'search_strategy': 'grid',
            'num_iterations': 1000,
            'population_size': 50,
            'temperature': 1.0,
            'cooling_rate': 0.9,
            'mutation_rate': 0.01
        }
        self.load_config()

    def load_config(self):
        config_file = os.environ.get('ASTRONOMY_OPTIMIZER_CONFIG_FILE')
        if config_file:
            with open(config_file, 'r') as f:
                for line in f.readlines():
                    key, value = line.strip().split('=')
                    self.config[key] = eval(value)

    def get(self, key, default=None):
        return self.config.get(key, default)


# Create a singleton instance of the Config class
config = Config()
