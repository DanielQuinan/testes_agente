import unittest

class MatriceException(Exception):
    pass

class MatriceStringa:
    def __init__(self, r, c, val):
        if r <= 0 or c <= 0:
            raise RuntimeError()
        self.m = [[val for _ in range(c)] for _ in range(r)]

    def set(self, r, c, val):
        if not (0 <= r < len(self.m) and 0 <= c < len(self.m[0])):
            raise MatriceException()
        self.m[r][c] = val

    def rigaToString(self, idx, separatore):
        if separatore is None:
            raise MatriceException("Separatore cannot be null")
        if not (0 <= idx < len(self.m)):
            raise MatriceException("Index out of bounds")
        
        return separatore.join(self.m[idx])

