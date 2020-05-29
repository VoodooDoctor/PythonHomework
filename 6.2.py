class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self.width = _width

    def mass (self):
        self.weight = 25
        self.tickness = 0.05
        mass = (self._length * self.width * self.weight)/1000 * self.tickness * 100
        print(f'{mass}')

r = Road(20, 5000)
r.mass()
