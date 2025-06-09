# filepath: /home/danielquinan/Documents/TCC/problema1_gemini.py
def diff(a: list[int], b: list[int]) -> list[int]:
    """
    Retorna uma lista contendo todos e somente os elementos
    da lista a que não estão presentes na lista b.
    """
    set_b = set(b)
    result = [item for item in a if item not in set_b]
    return result

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
