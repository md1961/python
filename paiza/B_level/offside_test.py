import unittest

from offside import OffsideJudge

class OffsideJudgeTest(unittest.TestCase):

    def test_judge_1(self):
        oj = OffsideJudge('A', 3)
        oj.set_positions('A', (18, 44, 69, 31, 90, 72, 48, 29, 55, 37, 78))
        oj.set_positions('B', (103, 85, 39, 55, 51, 8, 80, 37, 21, 65, 54))
        self.assertEqual(oj.judge(), (5,))

    def test_judge_2(self):
        oj = OffsideJudge('A', 3)
        oj.set_positions('A', (18, 41, 63, 30, 84, 95, 67, 29, 71, 48, 91))
        oj.set_positions('B', (96, 77, 40, 67, 49, 75, 76, 31, 19, 60, 47))
        self.assertEqual(oj.judge(), (5, 6, 11))

    def test_judge_3(self):
        oj = OffsideJudge('B', 7)
        oj.set_positions('A', (86, 36, 55, 88, 10, 82, 53, 107, 83, 22, 15))
        oj.set_positions('B', (69, 38, 48, 73, 21, 50, 27, 1, 41, 24, 103))
        self.assertEqual(oj.judge(), (8,))

    def test_judge_4(self):
        oj = OffsideJudge('B', 10)
        oj.set_positions('A', (69, 41, 96, 89, 53, 42, 83, 95, 48, 4, 25))
        oj.set_positions('B', (100, 71, 90, 59, 86, 97, 84, 85, 79, 81, 98))
        self.assertEqual(oj.judge(), ())

    def test_judge_5(self):
        oj = OffsideJudge('A', 3)
        oj.set_positions('A', (18, 44, 69, 31, 70, 72, 48, 29, 55, 37, 78))
        oj.set_positions('B', (103, 85, 39, 55, 51, 8, 80, 37, 21, 65, 54))
        self.assertEqual(oj.judge(), ())
