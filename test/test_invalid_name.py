import unittest
from core import *
from .linter_test import *
from core.rules import InvalidNameRule
from core.rule import *

class TestInvalidNameRule(LinterTest):

    def test_invalid_class(self):
        result = analyze(InvalidNameRule, """class cat:
                                                def meow(self, number_of_meow):
                                                    print("Meow" * number_of_meow)
                                                    return number_of_meow""")
        expectedWarnings = [Warning('InvalidName', 1, 'invalid class name cat')]
        self.asssertWarning(result, expectedWarnings)

    def test_invalid_method(self):
        result = analyze(InvalidNameRule, """class Cat:
                                                def Meow(self, number_of_meow):
                                                    print("Meow" * number_of_meow)
                                                    return number_of_meow""")
        expectedWarnings = [Warning('InvalidName', 2, 'invalid method name Meow')]
        self.asssertWarning(result, expectedWarnings)

    def test_invalid_function(self):
        result = analyze(InvalidNameRule, """def Foo(number_of_meow):
                                                    print("Meow" * number_of_meow)""")
        expectedWarnings = [Warning('InvalidName', 1, 'invalid function name Foo')]
        self.asssertWarning(result, expectedWarnings)

    def test_invalid_cls_mtd(self):
        result = analyze(InvalidNameRule, """class cat:
                                                def Meow(self, number_of_meow):
                                                    print("Meow" * number_of_meow)
                                                    return number_of_meow""")
        expectedWarnings = [Warning('InvalidName', 1, 'invalid class name cat'),
                            Warning('InvalidName', 2, 'invalid method name Meow')]
        self.asssertWarning(result, expectedWarnings)


if __name__ == '__main__':
    unittest.main()
