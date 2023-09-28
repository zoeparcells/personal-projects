import unittest
from collections import deque
import numpy as np


# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOWUP How would you solve this problem if a temporary buffer is not allowed?
# def removeDups(list):

# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
def kToLast(list, k):
    pointer = list
    kElement = 0
    for i in np.arange(k):
        if i < k:
            pointer.popleft()
        else:
            kElement = pointer.popleft()
    return kElement


# 2.2 Delete Middle Node: Implement an algorithm to delete a node in the middle (ie. any node but the first and
# last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
def deleteMiddle(list, element):
    rightSide = list
    leftSide = deque()
    while len(rightSide) > 0:
        element_i = list.pop()
        if element_i == element:
             rightSide += leftSide
             break
        else:
            leftSide.appendleft(element_i)
            continue
    return rightSide

# 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be
# after the elements less than x (see below). the partition element x can appear anywhere in the "right partition",
# it does not need to appear between the left and right partitions.
# def partition(list, element):


class Test(unittest.TestCase):

    # removeDupsCases = [(deque("aabbccddee"), deque('abcde'))]
    #
    # def test_removeDups(self):
    #     case = removeDups(test_ll[0])
    #     self.assertEquals(case, test_ll[1])

    kToLastCase = [deque([1, 2, 3, 4, 5]), deque([5, 4, 3, 2, 1])]

    def test_kToLast(self):
        case1 = kToLast(self.kToLastCase[0], 1)
        case2 = kToLast(self.kToLastCase[1], 3)
        self.assertEqual(case1, case2)

    deleteMiddleCase = [deque([1, 2, 3, 4, 5]), deque([5, 4, 3, 2, 1])]

    def test_deleteMiddle(self):
        case1 = deleteMiddle(self.deleteMiddleCase[0], 1)
        self.assertEqual(case1, deque([2, 3, 4, 5]))
        case2 = deleteMiddle(self.deleteMiddleCase[1], 2)
        self.assertEqual(case2, deque([5, 4, 3, 1]))

    # partitionCase = [deque([3, 5, 8, 5, 10, 2, 1]), deque([3, 1, 2, 10, 5, 5, 8])]
    #
    # def test_partition(self):
    #     case = partition(self.partitionCase[0], 5)
    #     self.assertEqual(case, self.partitionCase[1])


if __name__ == '__main__':
    unittest.main()