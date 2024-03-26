import unittest
from core import *
from .linter_test import *
from core.rules import ManyArgumentsRule
from core.rule import *


class TestManyArgumentsRule(LinterTest):

    def test_manyArgs(self):
        result = analyze(ManyArgumentsRule,
                         """def foo(a,b,c,d,e,f,g):
                            pass""")
        expectedWarnings = [Warning('ManyArgumentsWarning', 1, 'function foo defined with many arguments!')]
        self.asssertWarning(result, expectedWarnings)

    def test_noManyArgs_1(self):
        result = analyze(ManyArgumentsRule,
                         """def foo(a,b,c,d,e,f):
                            pass""")
        self.asssertWarning(result, [])

    def test_noManyArgs_2(self):
        result = analyze(ManyArgumentsRule,
                         """def foo(a):
                            pass""")
        self.asssertWarning(result, [])

    def test_noManyArgs_InsideAClass(self):
        result = analyze(ManyArgumentsRule,
                         """class Demo:
                            def foo(a):
                                pass""")
        self.asssertWarning(result, [])

    def test_noManyArgs_InsideAClass2(self):
        result = analyze(ManyArgumentsRule,
                         """class Demo:
                            def bar(a,b,c,d,e,f,g,h):
                                pass""")
        expectedWarnings = [Warning('ManyArgumentsWarning', 2, 'function bar defined with many arguments!')]

        self.asssertWarning(result, expectedWarnings)
    
if __name__ == '__main__':
    unittest.main()
