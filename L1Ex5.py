class Matrix:
    def __init__(self, row, col, val):
        self._row = row
        self._col = col
        self._matrix = [[val for _ in range(col)] for _ in range(row)]

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self._matrix])

    def size(self):
        return (self._row, self._col)

    def _check_index(self, row, col):
        if row < 0 or col < 0 or row > self._row or col > self._col:
            raise IndexError("Index outside matrix")

    def get_cell(self, row, col):
        self._check_index(row, col)
        return self._matrix[row][col]

    def set_cell(self, row, col, val):
        self._check_index(row, col)
        self._matrix[row][col] = val
