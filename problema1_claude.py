def diff(a, b):
    """
    Retorna um array que contém todos e somente os elementos
    do array 'a' que não estão presentes no array 'b'.
    
    Args:
        a: Lista de elementos
        b: Lista de elementos para comparação
    
    Returns:
        Lista contendo elementos de 'a' que não estão em 'b'
    """
    # Converte 'b' para um set para busca eficiente O(1)
    b_set = set(b)
    
    # Filtra elementos de 'a' que não estão em 'b'
    result = [element for element in a if element not in b_set]
    
    return result
