class Matrix:
    def __init__(self, mtrx):
        self.mtrx = mtrx
    def __str__(self):
        mt = ''
        for string in self.mtrx:
            mt = mt + f'{" ".join(str(x) for x in string)}' + '\n'
        return mt
    def __add__(self, other):
        _summary = []
        result = ''
        for string1, string2 in zip(self.mtrx, other.mtrx):
            _string = []
            for i, j in zip(string1, string2):
                item = i + j
                _string.append(item)
            _summary.append(_string)
        for string in _summary:
            result = result + f'{" ".join(str(x) for x in string)}' + '\n'
        return result

mt1 = Matrix([[1, 2, 3],[3, 2, 1]])
mt2 = Matrix([[4, 5, 6], [7, 8, 9]])

print(mt1)
print(mt2)

print(mt1 + mt2)