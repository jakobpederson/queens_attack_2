from queens_attack_2 import QueensAttack
import unittest


class QueensAttackTest(unittest.TestCase):

    def setUp(self):
        self.sut = QueensAttack()

    def test_get_right(self):
        self.assertEqual(0, self.sut.get_right(4, 4))
        self.assertEqual(3, self.sut.get_right(1, 4))
        self.assertEqual(2, self.sut.get_right(2, 4))

    def test_get_left(self):
        self.assertEqual(3, self.sut.get_left(3, 4))
        self.assertEqual(1, self.sut.get_left(1, 4))
        self.assertEqual(2, self.sut.get_left(2, 4))

    def test_right_left(self):
        self.assertEqual(3, self.sut.get_left(4 - 1, 4))
        self.assertEqual(0, self.sut.get_right(4, 4))
        self.assertEqual(2, self.sut.get_left(3 - 1, 5))
        self.assertEqual(2, self.sut.get_right(3, 5))

    def test_up_down(self):
        self.assertEqual(6, self.sut.solve_east_west((4, 4), 4))
        self.assertEqual(8, self.sut.solve_east_west((4, 3), 5))

    def test_solve_diagonal(self):
        self.assertEqual(3, self.sut.solve_diagonal((4, 4), 4))
        self.assertEqual(6, self.sut.solve_diagonal((4, 3), 5))

    def tests_blockers(self):
        self.assertEqual(0, self.sut.solve_all((4, 3), 5, ((5, 5), (4, 3), (2, 3))))
