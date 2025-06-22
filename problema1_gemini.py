def diff(a: list[int], b: list[int]) -> list[int]:
    """
    Retorna uma lista contendo todos e somente os elementos
    da lista a que não estão presentes na lista b.
    """
    set_b = set(b)
    result = [item for item in a if item not in set_b]
    return result
