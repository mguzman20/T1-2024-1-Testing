import unittest
from core import *
from core.rewriter import rewrite
from .linter_test import *
from core.transformers import *


class TestIfTrueRewriter(LinterTest):

	def test_simplified_if_condition(self):
		result = rewrite(SimplifiedIfCommand, """
def example1(x, y):
	return True if x > y else False
    """)
		self.assertAST(result, """def example1(x, y):
        	return x > y""")

	def test_simplified_if_not_condition(self):
		result = rewrite(SimplifiedIfCommand, """
def example2(a):
	z = 100
	x = 10
	return False if z > a > x else True""")
		self.assertAST(result, """def example2(a):
	z = 100
	x = 10
	return not z > a > x""")

if __name__ == '__main__':
    unittest.main()

