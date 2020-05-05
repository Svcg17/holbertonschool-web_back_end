"""Basic annotations task 12"""
from typing import Union, Any, Mapping, TypeVar, Tuple, List
T = TypeVar('T')

def zoom_array(lst: List, factor: int = 2) -> List:
    """Returns a list of by a factor
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)
print(zoom_2x)
zoom_3x = zoom_array(array, int(3.0))