

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def total_weight(self):
        total_weight = int((self._length * self._width * 25 * 1) / 1000)
        print(f'Масса асфальта при толщине слоя в 1см на всей площади дороги составит {total_weight} т')


road = Road(5000, 20)
road_weight = road.total_weight()
