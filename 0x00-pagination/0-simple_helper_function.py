#!/usr/bin/env python3
"""0-simple_helper_function module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range function

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        Tuple: Tuple of start and end index
    """
    return ((page - 1) * page_size, page * page_size)
