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

    def test_x(self):
        self.assertEqual(3, self.sut.get_left(4 - 1, 4))
        self.assertEqual(0, self.sut.get_right(4, 4))
        self.assertEqual(2, self.sut.get_left(3 - 1, 5))
        self.assertEqual(2, self.sut.get_right(3, 5))
