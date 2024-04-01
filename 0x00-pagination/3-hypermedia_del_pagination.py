#!/usr/bin/env python3
""" This module provides a server class to
paginate a database of popular baby names."""
import csv
import math
from typing import List, Dict, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieves a page of the dataset with hypermedia information
        based on index.

        Args:
            index (int): The start index of the page. Defaults to None.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing the page information and
            hypermedia links.
        """
        page_info = []
        info = self.indexed_dataset()
        index = 0 if index is None else index
        items = sorted(info.keys())
        assert index >= 0 and index <= items[-1]
        [page_info.append(i)
            for i in items if i >= index and len(page_info) <= page_size]
        data = [info[x] for x in page_info[:-1]]
        next_index = \
            page_info[-1] if len(page_info) - page_size == 1 else None
        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
