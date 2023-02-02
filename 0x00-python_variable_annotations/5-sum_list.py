#!/usr/bin/env python3
"""
5-sum_list: Module
"""


def sum_list(input_list: list[float]) -> float:
    """
    Takes the input_list arg and returns their sum as a float.
    """
    sum: float = 0
    i = 0
    for i in range(len(input_list)):
        sum += input_list[i]
    return sum
