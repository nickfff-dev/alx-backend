#!usr/bin/env python3
""" This module provides a server class to
paginate a database of popular baby names.
"""
import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of the dataset based on the given page
        number and page size.

        Args:
            page (int): The page number, 1-indexed. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A list of rows for the specified page.
        """
        # Verify that both arguments are integers greater than 0
        str_1 = "Page must be an integer greater than 0"
        str_2 = "Page size must be an integer greater than 0"
        assert isinstance(page, int) and page > 0, str_1
        assert isinstance(page_size, int) and page_size > 0, str_2

        # Calculate the start and end indexes for pagination
        start_index, end_index = index_range(page, page_size)

        # Retrieve the dataset
        dataset = self.dataset()

        # Check if the requested page is within the dataset range
        if start_index >= len(dataset):
            return []

        # Return the appropriate page of the dataset
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieves a page of the dataset with hypermedia information.

        Args:
            page (int): The page number, 1-indexed. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing the page information
            and hypermedia links.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
