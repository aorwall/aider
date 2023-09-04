from typing import List, Any

def flatten(iterable: List) -> List[Any]:
    """
    Flattens a nested list-like structure into a flat list.
    
    Args:
    iterable (List): The nested list-like structure to flatten.
    
    Returns:
    List[Any]: The flattened list.
    """
    if not isinstance(iterable, list):
        raise ValueError("Input must be of type 'list'.")

    def _flatten(lst):
        result = []

        for item in lst:
            if isinstance(item, list):
                result += _flatten(item)
            elif item is not None:
                result.append(item)

        return result

    return _flatten(iterable)