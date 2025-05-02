#!/usr/bin/env python3
"""
Pagination helper function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start and end index
    for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple (start_index, end_index).
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
