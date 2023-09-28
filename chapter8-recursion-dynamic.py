import unittest


# 8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps
# at a time. Implement a method to count how many possible ways the child can run up the stairs.
def tripleStep(n):
    hops = [1, 2, 3]
    while n > 0:
        if n in hops:
            return n
        else:
            return tripleStep(n - hops[0]) + tripleStep(n - hops[1]) + tripleStep(n - hops[2])
    else:
        return 0


class Test(unittest.TestCase):

    tripleStepCases = [(1, 1), (2, 2), (3, 3), (4, 6), (5, 11)]

    def test_tripleStep(self):
        for case in self.tripleStepCases:
            ways = tripleStep(case[0])
            self.assertEqual(ways, case[1])


if __name__ == '__main__':
    unittest.main()
