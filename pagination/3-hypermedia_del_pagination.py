#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """
        Creates an indexed version of the dataset, useful for deletion-resilient pagination.

        Returns:
            Dict[int, List[str]]: A dictionary mapping indices to dataset rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a dictionary containing a paginated view of the dataset
        while ensuring resilience against deletions.

        Args:
            index (int): The start index for the page.
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary with pagination metadata.
        """
        assert isinstance(index, int) and 0 <= index < len(self.dataset()), \
            "index must be within the valid dataset range"

        indexed_data = self.indexed_dataset()
        dataset_size = len(self.dataset())

        data = []
        current_index = index
        items_collected = 0

        while items_collected < page_size and current_index < dataset_size:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                items_collected += 1
            current_index += 1

        next_index = current_index if current_index < dataset_size else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
