#!/usr/bin/env python3
"""
module element_length
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """ return values with the appropriate types """
    return [(i, len(i)) for i in lst]
