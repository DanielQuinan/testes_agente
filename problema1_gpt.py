def diff(a, b):
    """
    Retorna uma lista com todos e somente os elementos de 'a' que não estão em 'b'.
    """
    b_set = set(b)
    return [x for x in a if x not in b_set]
