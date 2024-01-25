import numpy as np
from itertools import groupby

def are_arrays_equal(arrays):
    return all(np.array_equal(arr, arrays[0]) for arr in arrays)

def group_arrays_by_wavenumbers(arrays):
    # Enumerate to get both arrays and their indices
    enumerated_arrays = list(enumerate(arrays))

    # Sort the arrays based on their wavenumbers
    enumerated_arrays.sort(key=lambda x: tuple(x[1]))

    grouped_arrays = []
    for key, group in groupby(enumerated_arrays, lambda x: tuple(x[1])):
        indices, arrays_with_same_wavenumbers = zip(*group)
        grouped_arrays.append({'wavenumbers': key, 'indices': list(indices), 'arrays': list(arrays_with_same_wavenumbers)})

    return grouped_arrays
