#!/usr/bin/env python3
"""Type Checking"""
from typing import Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """Returns a tuple"""
    zoomed_in: Tuple = tuple([item for item in lst for i in range(factor)])
    return zoomed_in