#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of  list.

    Args:
        my_list (list): list to print elements from.
        x (int):number of elements of my_list to print.

    Returns:
        Number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
#!/usr/bin/python3


def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int):  integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

