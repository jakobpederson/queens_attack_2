from collections import namedtuple

Coordinates = namedtuple("Coordinates", ["y", "x"])

class QueensAttack():

    def get_right(self, queen, length):
        x = [x for x in range(length)]
        return len(x[queen:])

    def get_left(self, queen, length):
        x = [x for x in range(length)]
        return len(x[:queen])

    def solve_east_west(self, queen, length):
        coord = Coordinates(y=queen[0], x=queen[1])
        sum = self.get_right(coord.x, length) + self.get_right(coord.y, length) +  self.get_left(coord.x - 1, length) +  self.get_left(coord.y - 1, length)
        return sum


