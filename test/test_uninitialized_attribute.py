import unittest
from core import *
from .linter_test import *
from core.rules import UninitializedAttributeRule
from core.rule import *

class TestUninitializedAttributeRule(LinterTest):

    def test_uni_attr(self):
        result = analyze(UninitializedAttributeRule,
                         """class Demo:
                            def foo(self):
                                return self.x + self.y
                            """)
        expectedWarnings = [Warning('UninitializedAttribute', 3, 'x attribute was not initialized!'),
                            Warning('UninitializedAttribute', 3, 'y attribute was not initialized!')]
        self.asssertWarning(result, expectedWarnings)

    def test_uni_attr_one(self):
        result = analyze(UninitializedAttributeRule,
                         """class Demo:
                            def __init__(self):
                                self.x = 2

                            def foo(self):
                                return self.x + self.y
                            """)
        expectedWarnings = [Warning('UninitializedAttribute', 6, 'y attribute was not initialized!')]
        self.asssertWarning(result, expectedWarnings)

    def test_ini_attr(self):
        result = analyze(UninitializedAttributeRule,
                         """class Demo:
                            def __init__(self):
                                self.x = 2
                                self.y = 3

                            def foo(self):
                                return self.x + self.y
                            """)
        expectedWarnings = []
        self.asssertWarning(result, expectedWarnings)


if __name__ == '__main__':
    unittest.main()
