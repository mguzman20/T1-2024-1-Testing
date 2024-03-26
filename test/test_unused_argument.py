import unittest
from core import *
from .linter_test import *
from core.rules import UnusedArgumentRule
from core.rule import *

class TestUnusedArgumentRule(LinterTest):

    def test_uni_attr(self):
        result = analyze(UnusedArgumentRule,
                         """def example1(x, y, z):
                                return x + y
                            """)
        expectedWarnings = [Warning('UnusedArgument', 1, 'z argument has not been used!')]
        self.asssertWarning(result, expectedWarnings)

    def test_uni_attr_one(self):
        result = analyze(UnusedArgumentRule,
                         """def example2(x, y, z):
                                a = y + z
                                c = z
                                return a + c
                            """)
        expectedWarnings = [Warning('UnusedArgument', 1, 'x argument has not been used!')]
        self.asssertWarning(result, expectedWarnings)

    def test_ini_attr(self):
        result = analyze(UnusedArgumentRule,
                         """class Fruit:

                                def __init__(self, name, vitamins):
                                    self.name = name
                                    self.vitamins = vitamins

                                def change_vitamins(self, vs):
                                    self.vitamins = []
                            """)
        expectedWarnings = [Warning('UnusedArgument', 7, 'vs argument has not been used!')]
        self.asssertWarning(result, expectedWarnings)


if __name__ == '__main__':
    unittest.main()
