class Road:

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def tarmac_mass(self):
        mass = self._lenght * self._width * 25 * 5
        return mass

mass = Road(10, 10)

print(mass.tarmac_mass())