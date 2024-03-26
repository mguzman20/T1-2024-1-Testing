import unittest
from core import *
from core.rewriter import rewrite
from .linter_test import *
from core.transformers import *


class TestIfTrueRewriter(LinterTest):
    def test_if_true_simple(self):
        result = rewrite(IfTrueRewriterCommand,
                         """
if True :
    return x
else :
    return y
    """)
        self.assertAST(result, "return x")

    def test_if_true_inside(self):
        result = rewrite(IfTrueRewriterCommand,
                         """
def greaterThan100(x):
    if (x > 100):
        if True:
            print(x + " is greater than 100")

    else:
        print(x + " is less than 100")
    """)
        self.assertAST(result, """def greaterThan100(x):
    if (x > 100):
        print(x + " is greater than 100")

    else:
        print(x + " is less than 100")""")


    def test_if_true_inside_2(self):
        result = rewrite(IfTrueRewriterCommand,
                         """
def greaterThan1000(x):
    if (x > 1000):
        print(x + " is greater than 1000")

    else:
        if True:
            print(x + " is less than 1000")
    """)
        self.assertAST(result, """def greaterThan1000(x):
    if (x > 1000):
        print(x + " is greater than 1000")

    else:
        print(x + " is less than 1000")""")



if __name__ == '__main__':
    unittest.main()
