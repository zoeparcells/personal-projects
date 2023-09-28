import unittest


# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
def unique(string):
    # Brute force solution - does not account for stipulation
    # "What if you cannot use additional data structures?"
    charsUsed = []
    for char in string:
        if char in charsUsed:
            return False
        else:
            charsUsed.append(char)

    return True


# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
def permutation(firstString, secondString):
    if len(firstString) != len(secondString):
        return False
    for char in firstString:
        if char not in secondString:
            return False
    return True


# 1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient
# space at the end to hold the additional characters, and that you are given that 'true' length of the string.
def url(string):
    return "%20".join(string.split())


class Test(unittest.TestCase):

    trueUniqueCases = ['abcd', 'efgh', '']
    falseUniqueCases = ['abba', 'efgh = efgh']

    def test_unique(self):
        # true check
        for test_string in self.trueUniqueCases:
            case = unique(test_string)
            self.assertTrue(case)
        # false check
        for test_string in self.falseUniqueCases:
            case = unique(test_string)
            self.assertFalse(case)

    truePermutationCases = [('abcd', 'dcba'), ('efgh', 'hefg')]
    falsePermutationCases = [('abcd', 'efgh'), ('abc', 'abcd')]

    def test_permutation(self):
        # true check
        for test_strings in self.truePermutationCases:
            case = permutation(test_strings[0], test_strings[1])
            self.assertTrue(case)
        # false check
        for test_strings in self.falsePermutationCases:
            case = permutation(test_strings[0], test_strings[1])
            self.assertFalse(case)

    urlCases = [('abc d', 'abc%20d'), ('e fg h', 'e%20fg%20h')]

    def test_url(self):
        for test_strings in self.urlCases:
            case = url(test_strings[0])
            self.assertEqual(case, test_strings[1])

if __name__ == "__main__":
    unittest.main()
