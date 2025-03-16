def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
    """
    Returns a dictionary containing a paginated view of the dataset
    while ensuring resilience against deletions.

    Args:
        index (int): The start index for the page. Default is None (equivalent to 0).
        page_size (int): The number of items per page.

    Returns:
        Dict[str, Any]: A dictionary with pagination metadata.
    """
    if index is None:
        index = 0

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
