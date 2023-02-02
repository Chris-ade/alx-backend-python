#!/usr/bin/env python3
"""
sums a mixed list module
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum a list of float
    """
    sum: float = 0
    i = 0
    for i in range(len(mxd_lst)):
        sum += mxd_lst[i]

    return sum
