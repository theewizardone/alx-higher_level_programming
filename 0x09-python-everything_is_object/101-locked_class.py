#!/usr/bin/python3
"""Ilustrates a locked class."""


class LockedClass:
    """
    Hinders  user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
