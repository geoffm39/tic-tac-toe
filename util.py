"""
The util module contains any general helpers and functions to use.
"""

import os


def clear_console() -> None:
    """
    Clear the output on the run console
    :return: None
    """
    if os.name == 'posix':
        os.system('clear')  # For macOS and Linux
    elif os.name == 'nt':
        os.system('cls')  # For Windows
