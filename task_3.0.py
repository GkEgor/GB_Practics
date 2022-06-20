class Cell:
    def __init__(self, cell):
        if isinstance(cell, int) == True:
            self.cell = cell
        else:
            print("Число должно быть класса 'int'")


    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        return Cell(self.cell // other.cell)

    def __truediv__(self, other):
        return (Cell(int(self.cell / other.cell)))

    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return self.cell - other.cell
        else:
            print('Разность двух клеток меньше нуля, вычитание невозможно')

    def make_order(self, count):
        for i in range(self.cell // count):
            print('*' * count)
        print('*' * (self.cell % count))

cell_1 = Cell(10)
cell_2 = Cell(11)
print((cell_1 + cell_2).cell)
print((cell_1 - cell_2))
print((cell_1 / cell_2).cell)
print((cell_1 // cell_2).cell)
print((cell_1 * cell_2).cell)
cell_1.make_order(5)



