from _ast import IfExp
from ast import *
from typing import Any
from core.rewriter import RewriterCommand


# Clases que permiten transformar if ternarios que puedan ser simplificados usando la condicion o su negacion.

class SimplifiedIfTransformer(NodeTransformer):

    def visit_IfExp(self, node: IfExp):

        if isinstance(node.test, Compare):
            if isinstance(node.body, Constant) and isinstance(node.orelse, Constant):
                if node.body.value == True and node.orelse.value == False:
                    return Compare(
                        left=node.test.left,
                        ops=node.test.ops,
                        comparators=node.test.comparators)
                elif node.body.value == False and node.orelse.value == True:
                    return UnaryOp(
                        op=Not(),
                        operand=Compare(
                            left=node.test.left,
                            ops=node.test.ops,
                            comparators=node.test.comparators))
        else:
            return node
        


class SimplifiedIfCommand(RewriterCommand):

    def apply(self, ast):
        new_tree = fix_missing_locations(SimplifiedIfTransformer().visit(ast))
        return new_tree

