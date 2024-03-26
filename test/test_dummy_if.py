import unittest
from core import *
from .linter_test import *
from core.rules import DummyIfRule
from core.rule import *

class TestDummyIfRule(LinterTest):

    def test_dummy_if(self):
        result = analyze(DummyIfRule, """def example1():
                                            if True:
                                                print("Example 1")""")
        expectedWarnings = [Warning('DummyIfWarning', 2, 'this if does not have any sense!')]
        self.asssertWarning(result, expectedWarnings)

    def test_dummy_if_insideIf(self):
        result = analyze(DummyIfRule, """def greaterThan100(x):
                                            if (x > 100):
                                                if True:
                                                    print(x + " is greater than 100")

                                            else:
                                                print(x + " is less than 100")""")
        expectedWarnings = [Warning('DummyIfWarning', 3, 'this if does not have any sense!')]
        self.asssertWarning(result, expectedWarnings)

    def test_dummy_if_insideIf2(self):
        result = analyze(DummyIfRule, """def greaterThan1000(x):
                                            if (x > 1000):
                                                print(x + " is greater than 1000")

                                            else:
                                                if True:
                                                    print(x + " is less than 1000")""")
        expectedWarnings = [Warning('DummyIfWarning', 6, 'this if does not have any sense!')]
        self.asssertWarning(result, expectedWarnings)


if __name__ == '__main__':
    unittest.main()
