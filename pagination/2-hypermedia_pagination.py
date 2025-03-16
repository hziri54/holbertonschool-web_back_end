#!/usr/bin/env python3
"""
Hypermedia pagination module
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start and end index for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple (start_index, end_index).
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """
        Loads and caches the dataset.

        Returns:
            List[List[str]]: The dataset without the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Retrieves a page from the dataset.

        Args:
            page (int): The page number (must be >= 1).
            page_size (int): The number of items per page (must be >= 1).

        Returns:
            List[List[str]]: The requested page of the dataset.
        """
        # Vérification des types et valeurs
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        start_index, end_index = index_range(page, page_size)

        data = self.dataset()

        return data[start_index:end_index] if start_index < len(data) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns pagination information in a hypermedia format.

        Args:
            page (int): The page number (default = 1).
            page_size (int): The number of items per page (default = 10).

        Returns:
            Dict[str, Any]: A dictionary containing pagination metadata.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
