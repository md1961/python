import unittest
from janken import Janken

class JankenTest(unittest.TestCase):

    def test_example_01(self):
        janken = Janken('CGPC')
        actual = janken.max_win_with(7)
        self.assertEqual(actual, 4)

    def test_example_02(self):
        janken = Janken('GPCPC')
        actual = janken.max_win_with(10)
        self.assertEqual(actual, 3)

    def test_play_100_times(self):
        hands = 'GCCGCPGPCPPGGGCCPPGGGCPPGCGPGGPGPPPGGPGPPCCCGPCCPPCGGGGCCCCGPCGCCCGPCPPPPPGCCPPGGPCGCPGCGCCPPCGCCCPG'
        janken = Janken(hands)
        actual = janken.max_win_with(250)
        self.assertEqual(actual, 95)

    def test_play_100_gu(self):
        janken = Janken('G' * 100)
        actual = janken.max_win_with(500)
        self.assertEqual(actual, 100)

    def test_play_100_choki(self):
        janken = Janken('C' * 100)
        actual = janken.max_win_with(0)
        self.assertEqual(actual, 100)

    def test_play_100_pa(self):
        janken = Janken('P' * 100)
        actual = janken.max_win_with(200)
        self.assertEqual(actual, 100)
