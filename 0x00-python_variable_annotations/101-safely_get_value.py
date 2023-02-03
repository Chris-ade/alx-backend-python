#!/usr/bin/env python3
"""
module : safely get value
"""

from typing import Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[Any, None] = None) -> Union[Any, None]:
    """ Get value safely """
    if key in dct:
        return dct[key]
    else:
        return default
