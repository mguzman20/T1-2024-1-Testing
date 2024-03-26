import unittest
from core import *
from .linter_test import *
from core.rules import SimplifiableIfRule
from core.rule import *

class TestSimplifiableIfRule(LinterTest):

    def test_simplify_ternary_if(self):
        result = analyze(SimplifiableIfRule, """return False if self.errors else True""")
        expectedWarnings = [Warning('SimplifiableIf', 1, 'if statement can be replaced with a bool(test)')]
        self.asssertWarning(result, expectedWarnings)

    def test_simplify_ternary_if_variable(self):
        result = analyze(SimplifiableIfRule, """res = False if self.errors else True""")
        expectedWarnings = [Warning('SimplifiableIf', 1, 'if statement can be replaced with a bool(test)')]
        self.asssertWarning(result, expectedWarnings)

    def test_simplify_if(self):
        result = analyze(SimplifiableIfRule, """def greaterThan1000(x):
                                            if (x <= 1000):
                                                a = False
                                            else:
                                                a = True""")
        expectedWarnings = [Warning('SimplifiableIf', 2, 'if statement can be replaced with a bool(test)')]
        self.asssertWarning(result, expectedWarnings)

    def test_simplify_if_return(self):
        result = analyze(SimplifiableIfRule, """def greaterThan1000(x):
                                            if (x <= 1000):
                                                return False
                                            else:
                                                return True""")
        expectedWarnings = [Warning('SimplifiableIf', 2, 'if statement can be replaced with a bool(test)')]
        self.asssertWarning(result, expectedWarnings)


if __name__ == '__main__':
    unittest.main()
