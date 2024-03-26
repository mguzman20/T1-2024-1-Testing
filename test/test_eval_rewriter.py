import unittest
from core import *
from core.rewriter import rewrite
from .linter_test import *
from core.transformers import *


class TestEvalRewriter(LinterTest):
    def test_eval_used(self):
        result = rewrite(LiteralEvalRewriterCommand, "eval('2')")
        
        self.assertAST(result, "literal_eval('2')")

    def test_eval_usedInsideFunction(self):
        result = rewrite(LiteralEvalRewriterCommand,
                    """def function():
                        eval('3+5')""")

        self.assertAST(result, 
                         """def function():
                            literal_eval('3+5')""")
    

if __name__ == '__main__':
    unittest.main()
