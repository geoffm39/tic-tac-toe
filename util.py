import os


def clear_console():
    """
    Clear the output on the run console
    :return: None
    """
    if os.name == 'posix':
        os.system('clear')  # For macOS and Linux
    elif os.name == 'nt':
        os.system('cls')  # For Windows
