class MatriceException(Exception):
    """Custom exception for matrix operations"""
    def __init__(self):
        super().__init__()


class MatriceStringa:
    def __init__(self, r, c, val):
        """
        Initialize the matrix with r rows and c columns, filling each position with val.
        
        Args:
            r (int): number of rows
            c (int): number of columns  
            val (str): value to fill each position
            
        Raises:
            RuntimeError: if r or c are not valid (less than or equal to 0)
        """
        if r <= 0 or c <= 0:
            raise RuntimeError()
        
        self.m = [[val for _ in range(c)] for _ in range(r)]
        self.rows = r
        self.cols = c
    
    def set(self, r, c, val):
        """
        Set the value at position (r, c) in the matrix.
        
        Args:
            r (int): row index
            c (int): column index
            val (str): value to set
            
        Raises:
            MatriceException: if r or c are outside valid bounds
        """
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
            raise MatriceException()
        
        self.m[r][c] = val
    
    def rigaToString(self, idx, separatore):
        """
        Convert a row to string with the given separator.
        
        Args:
            idx (int): row index
            separatore (str): separator to use between elements
            
        Returns:
            str: string representation of the row
            
        Raises:
            MatriceException: if idx is outside valid bounds
        """
        if idx < 0 or idx >= self.rows:
            raise MatriceException()
        
        return separatore.join(self.m[idx])


# Example usage and testing
""" if __name__ == "__main__":
    try:
        # Test valid constructor
        matrix = MatriceStringa(3, 4, "default")
        print("Matrix created successfully")
        
        # Test set method
        matrix.set(0, 0, "hello")
        matrix.set(1, 2, "world")
        print("Values set successfully")
        
        # Test rigaToString method
        row_string = matrix.rigaToString(0, " | ")
        print(f"Row 0: {row_string}")
        
        row_string = matrix.rigaToString(1, ", ")
        print(f"Row 1: {row_string}")
        
        # Test exceptions
        try:
            invalid_matrix = MatriceStringa(-1, 5, "test")
        except RuntimeError:
            print("RuntimeError caught for invalid constructor parameters")
        
        try:
            matrix.set(10, 0, "invalid")
        except MatriceException:
            print("MatriceException caught for invalid set parameters")
        
        try:
            matrix.rigaToString(10, ",")
        except MatriceException:
            print("MatriceException caught for invalid rigaToString parameters")
            
    except Exception as e:
        print(f"Unexpected error: {e}") """