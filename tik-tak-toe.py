import unittest


def tikTakToe(game):
    # horizontal wins
    winA = [(0, 0), (0, 1), (0, 2)]
    winB = [(1, 0), (1, 1), (1, 2)]
    winC = [(2, 0), (2, 1), (2, 2)]
    # vertical wins
    winD = [(0, 0), (1, 0), (2, 0)]
    winE = [(0, 1), (1, 1), (2, 1)]
    winF = [(0, 2), (1, 2), (2, 2)]
    # diagonal wins
    winG = [(0, 0), (1, 1), (2, 2)]
    winH = [(2, 2), (1, 1), (0, 0)]
    for win in (winA, winB, winC, winD, winE, winF, winG, winH):
        if game[win[0][0]][win[0][1]] == game[win[1][0]][win[1][1]] == game[win[2][0]][win[2][1]] == 'X':
            return 'X'
        elif game[win[0][0]][win[0][1]] == game[win[1][0]][win[1][1]] == game[win[2][0]][win[2][1]] == 'O':
            return 'O'
    return ''


class Test(unittest.TestCase):

    xCase = [['X', 'O', 'X'], ['', 'X', ''], ['O', '', 'X']]
    oCase = [['O', 'O', 'O'], ['O', 'X', 'X'], ['O', 'X', 'O']]
    drawCase = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'O']]

    def test_tikTakToe(self):
        case1 = tikTakToe(self.xCase)
        self.assertEqual(case1, 'X')
        case2 = tikTakToe(self.oCase)
        self.assertEqual(case2, 'O')
        case3 = tikTakToe(self.drawCase)
        self.assertEqual(case3, '')


if __name__ == '__main__':
    unittest.main()