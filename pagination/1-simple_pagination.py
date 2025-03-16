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

    # Obtenir les indices de pagination
    start_index, end_index = index_range(page, page_size)

    # Charger le dataset
    data = self.dataset()

    # Retourner les éléments de la page ou une liste vide si out of range
    return data[start_index:end_index] if start_index < len(data) else []
