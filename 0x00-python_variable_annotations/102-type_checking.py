#!/usr/bin/env python3

"""
Module for type checking
"""
from typing import Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """ Type checking """
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
