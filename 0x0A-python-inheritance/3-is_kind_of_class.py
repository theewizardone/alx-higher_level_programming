#!/usr/bin/python3
"Outlines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """ if an object is an instance or inherited instance of a class.

    Args:
        obj (any):object to check.
        a_class (type): class to match the type of obj to.
    Returns:
        When obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
