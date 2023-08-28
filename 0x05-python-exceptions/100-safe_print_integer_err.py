#!/usr/bin/python3


def raise_exception():
    """Raise a TypeError exception."""
    raise TypeError
#!/usr/bin/python3


def raise_exception_msg(message=""):
    """Raise a NameError exception with a message."""
    raise NameError(message)
#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an int with "{:d}".format().

    If a ValueError message is caught, a corresponding
    message is printed to stdrr.

    Args:
        value (int):  int to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)

