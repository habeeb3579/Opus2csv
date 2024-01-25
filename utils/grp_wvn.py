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

# Example: Replace the arrays with your actual data
#array1 = np.array([11900, 4000, -8])
#array2 = np.array([11980, 3900, -8])
#array3 = np.array([11900, 4000, -8])
#array4 = np.array([12000, 4100, -8])
#array5 = np.array([11980, 3900, -8])
#array6 = np.array([12100, 4200, -8])

#arrays = [array1, array2, array3, array4, array5, array6]

# Group arrays with similar wavenumbers
#grouped_arrays = group_arrays_by_wavenumbers(arrays)

# Display the groups
#for idx, group in enumerate(grouped_arrays, 1):
#    print(f"Group {idx}:")
#    print(f"  Wavenumbers: {group['wavenumbers']}")
#    print(f"  Indices: {group['indices']}")
#    print(f"  Arrays: {group['arrays']}")
#    print("---------------------------------")