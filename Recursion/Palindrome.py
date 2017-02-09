"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""
import unittest


def remove_white(s):
    return s.replace(" ", "").replace("'", "")


def is_pal(s):
    if s == reverse(s):
        return True
    else:
        return False


def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]


class PalindromeTest(unittest.TestCase):
    def test_pal(self):
        self.assertEqual(is_pal(remove_white("x")), True)
        self.assertEqual(is_pal(remove_white("radar")), True)
        self.assertEqual(is_pal(remove_white("hello")), False)
        self.assertEqual(is_pal(remove_white("")), True)
        self.assertEqual(is_pal(remove_white("hannah")), True)
        self.assertEqual(is_pal(remove_white("madam i'm adam")), True)
