#!/usr/bin/env python3
"""
This module provides a helper function to calculate
the start and end indexes for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the start and end indexes for pagination
    based on the given page number and page size.

    Args:
        page (int): The page number, 1-indexed.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indexes
        for the specified page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
