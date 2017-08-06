
class QueensAttack():

    def get_right(self, queen, length):
        x = [x for x in range(length)]
        return len(x[queen:])

    def get_left(self, queen, length):
        x = [x for x in range(length)]
        return len(x[:queen])

