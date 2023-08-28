#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a ftn safely.

    Args:
        fct: The function to execute.
        args: Arguments for fct.

    Returns:
        If  error occurs - None.
        Otherwise -  result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
#!/usr/bin/python3


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except:
            result = b + a
            break
    return (result)
