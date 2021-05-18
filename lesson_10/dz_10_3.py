

class Cells:
    def __init__(self, num):
        self.num = num

    def make_model(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.num // rows)]) + '\n' + '*' * (self.num % rows)

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return 'Sum =  ' + str(self.num + other.num)

    def __sub__(self, other):
        return 'Subtraction = ' + str(self.num - other.num) if self.num - other.num > 0 \
            else 'Ячеек в первой клетке меньше или равно второй'

    def __mul__(self, other):
        return 'Multiply = ' + str(self.num * other.num)

    def __truediv__(self, other):
        return 'Truediv = ' + str(round(self.num / other.num))

cell_1 = Cells(98)
cell_2 = Cells(54)

print(cell_1)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_model(10))