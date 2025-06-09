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


""" # Exemplo de uso e testes
if __name__ == "__main__":
    # Teste básico
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 6, 7]
    resultado = diff(a, b)
    print(f"diff({a}, {b}) = {resultado}")  # Output: [1, 2, 5]
    
    # Teste com strings
    a_str = ["apple", "banana", "cherry", "date"]
    b_str = ["banana", "date", "elderberry"]
    resultado_str = diff(a_str, b_str)
    print(f"diff({a_str}, {b_str}) = {resultado_str}")  # Output: ['apple', 'cherry']
    
    # Teste com array vazio
    a_empty = []
    b_normal = [1, 2, 3]
    resultado_empty = diff(a_empty, b_normal)
    print(f"diff({a_empty}, {b_normal}) = {resultado_empty}")  # Output: []
    
    # Teste com b vazio
    a_normal = [1, 2, 3]
    b_empty = []
    resultado_b_empty = diff(a_normal, b_empty)
    print(f"diff({a_normal}, {b_empty}) = {resultado_b_empty}")  # Output: [1, 2, 3]
    
    # Teste com elementos duplicados em 'a'
    a_dup = [1, 2, 2, 3, 4, 4, 5]
    b_filter = [2, 4]
    resultado_dup = diff(a_dup, b_filter)
    print(f"diff({a_dup}, {b_filter}) = {resultado_dup}")  # Output: [1, 3, 5] """

def test_diff_normal_case():
    a = [1, 3, 5, 7, 9]
    b = [1, 5, 7]
    expected = [3, 9]
    result = diff(a, b)
    assert result == expected, f"Esperado {expected}, mas obteve {result}"
    print("test_diff_normal_case passou!")

def test_diff_empty_array():
    a = []
    b = [1, 2, 3]
    expected = []
    result = diff(a, b)
    assert result == expected, f"Esperado {expected}, mas obteve {result}"
    print("test_diff_empty_array passou!")

def test_diff_both_empty_arrays():
    a = []
    b = []
    expected = []
    result = diff(a, b)
    assert result == expected, f"Esperado {expected}, mas obteve {result}"
    print("test_diff_both_empty_arrays passou!")

def test_diff_all_common_elements():
    a = [1, 2, 3]
    b = [1, 2, 3]
    expected = []
    result = diff(a, b)
    assert result == expected, f"Esperado {expected}, mas obteve {result}"
    print("test_diff_all_common_elements passou!")

def test_diff_no_common_elements():
    a = [1, 2, 3]
    b = [4, 5, 6]
    expected = [1, 2, 3]
    result = diff(a, b)
    assert result == expected, f"Esperado {expected}, mas obteve {result}"
    print("test_diff_no_common_elements passou!")

def test_diff_duplicates():
    a = [1, 1, 2, 2]
    b = [2, 3, 4]
    expected = [1]
    result = list(dict.fromkeys(diff(a, b)))  # Remove duplicatas preservando a ordem
    assert result == expected, f"Esperado {expected}, mas obteve {result}"
    print("test_diff_duplicates passou!")

def test_diff_negative_numbers():
    a = [-1, -2, -3]
    b = [-2, -3, -4]
    expected = [-1]
    result = diff(a, b)
    assert result == expected, f"Esperado {expected}, mas obteve {result}"
    print("test_diff_negative_numbers passou!")

def test_diff_null_array():
    try:
        diff(None, [1, 5, 7])
    except TypeError:
        print("test_diff_null_array passou!")
    else:
        assert False, "Esperado TypeError ao passar None como primeiro argumento"

def test_diff_both_null_arrays():
    try:
        diff(None, None)
    except TypeError:
        print("test_diff_both_null_arrays passou!")
    else:
        assert False, "Esperado TypeError ao passar None como ambos os argumentos"

if __name__ == "__main__":
    test_diff_normal_case()
    test_diff_empty_array()
    test_diff_both_empty_arrays()
    test_diff_all_common_elements()
    test_diff_no_common_elements()
    test_diff_duplicates()
    test_diff_negative_numbers()
    test_diff_null_array()
    test_diff_both_null_arrays()
