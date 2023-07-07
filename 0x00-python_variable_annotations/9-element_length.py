#!/usr/bin/env python3
"""Type Checking"""
from typing import List, Sequence, Tuple

def element_length(lst: List[Sequence]) -> List[int]:
    """Annotate the below function’s parameters and return values with the
    appropriate types"""
    return [len(i) for i in lst]