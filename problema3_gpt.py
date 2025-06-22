class MatriceException(Exception):
    pass

class MatriceStringa:
    def __init__(self, r, c, val):
        if r <= 0 or c <= 0:
            raise RuntimeError()
        self.m = [[val for _ in range(c)] for _ in range(r)]

    def set(self, r, c, val):
        if r < 0 or r >= len(self.m) or c < 0 or c >= len(self.m[0]):
            raise MatriceException()
        self.m[r][c] = val

    def rigaToString(self, idx, separatore):
        if separatore is None or idx < 0 or idx >= len(self.m):
            raise MatriceException()
        return separatore.join(self.m[idx])
