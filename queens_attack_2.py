from collections import namedtuple

Coordinates = namedtuple("Coordinates", ["y", "x"])

class QueensAttack():

    def get_right(self, queen, length):
        x = [x for x in range(length)]
        return len(x[queen:])

    def get_left(self, queen, length):
        x = [x for x in range(length)]
        return len(x[:queen])

    def sum_moves(self, coord, length):
        return self.get_right(coord.x, length) + self.get_right(coord.y, length) +  self.get_left(coord.x - 1, length) +  self.get_left(coord.y - 1, length)


    def solve_east_west(self, queen, length):
        coord = Coordinates(y=queen[0], x=queen[1])
        return self.sum_moves(coord, length)

    def solve_diagonal(self, queen, length):
        coord = Coordinates(y=queen[0], x=queen[1])
        difference = abs(coord.x - coord.y)
        if difference > 0:
            return 2 * (self.get_right(coord.x, length - difference) + self.get_left(coord.x - 1, length - difference))
        return self.get_right(coord.x, length - difference) + self.get_left(coord.x - 1, length - difference)

    def solve_all(self, queen, length, blockers):
        coord = Coordinates(y=queen[0], x=queen[1])
        for blocker in blockers:
            if blocker[0] == coord.y:
                total = self.get_right(queen, length) + get_left(queen, length) -
        return 0
