#!/usr/bin/env python3
"""0-simple_helper_function module
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range function

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        Tuple: Tuple of start and end index
    """
    return ((page - 1) * page_size, page * page_size)


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
        """get_page function

        Args:
            page (int, optional): page number. Defaults to 1.
            page_size (int, optional): page size. Defaults to 10.

        Returns:
            List[List]: list of lists containing the appropriate
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
