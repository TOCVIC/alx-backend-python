#!/usr/bin/env python3
"""Safely get value"""
from typing import Mapping, Any, Union, TypeVar

def safely_get_value(dct, key, default = None) -> Union[Any, TypeVar('T')]:
    if key in dct:
        return dct[key]
    else:
        return default