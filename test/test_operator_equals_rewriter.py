import unittest
from core import *
from core.rewriter import rewrite
from .linter_test import *
from core.transformers import *


class TestOperatorEqualsRewriter(LinterTest):
    def test_plus_eq(self):
        result = rewrite(OperatorEqualsCommand, "a = a + 7")
        
        self.assertAST(result, "a += 7")

    def test_minus_eq(self):
        result = rewrite(OperatorEqualsCommand,
                    """b = b - c""")

        self.assertAST(result, 
                         """b -= c""")

    def test_pro_eq(self):
        result = rewrite(OperatorEqualsCommand, "d = d * a")
        
        self.assertAST(result, "d *= a")

    def test_div_eq(self):
        result = rewrite(OperatorEqualsCommand,
                    """e = e / 2""")

        self.assertAST(result, 
                         """e /= 2""")

    def test_mod_eq(self):
        result = rewrite(OperatorEqualsCommand, "f = f % 5")
        
        self.assertAST(result, "f %= 5")

    def test_pow_eq(self):
        result = rewrite(OperatorEqualsCommand,
                    """x = x ** y""")

        self.assertAST(result, 
                         """x **= y""")
    def test_divf_eq(self):
        result = rewrite(OperatorEqualsCommand,
                    """x = x // y""")

        self.assertAST(result, 
                         """x //= y""")
    

if __name__ == '__main__':
    unittest.main()
