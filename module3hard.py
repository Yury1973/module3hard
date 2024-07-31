data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    total = 0
    if data_structure is []:
        return total
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            total += calculate_structure_sum(key)
            total += calculate_structure_sum(value)
    elif isinstance(data_structure, (tuple, set, list)):
        for i in data_structure:
            total += calculate_structure_sum(i)
    elif isinstance(data_structure, (int, float)):
        total += data_structure
    elif isinstance(data_structure, str):
        total += len(data_structure)
    return total


result = calculate_structure_sum(data_structure)
print(result)
