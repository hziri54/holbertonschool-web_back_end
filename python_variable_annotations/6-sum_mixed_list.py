#!/usr/bin/env python3
"""Type-annotated function that takes a list mxd_lst of integers and floats
and returns their sum as a float."""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of integers and floats in the list mxd_lst."""
    return sum(mxd_lst)
