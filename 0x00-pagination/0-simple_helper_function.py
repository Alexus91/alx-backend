#!/usr/bin/env python3
"""
pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end for pagination.
    """
    start_index = 0
    end_index = 0
    for i in range(page):
        start_index = end_index
        end_index += page_size
    return (start_index, end_index)
