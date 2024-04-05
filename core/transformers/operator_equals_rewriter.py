from _ast import AST, Assign
from ast import *
from typing import Any
from core.rewriter import RewriterCommand

# Clases que permiten transformar codigo que contiene x = x <operador_aritmetico_binario> z a x <operador_aritmetico_binario>= z.

class OperatorEqualsTransformer(NodeTransformer):

    def __init__(self):
        super().__init__()

    def visit_Assign(self, node: Assign):
        if isinstance(node.value, BinOp):
            if isinstance(node.value.right, Name):
                if node.value.right.id == node.targets[0].id:
                    # AugAssign
                    return AugAssign(
                        target=node.targets[0],
                        op=node.value.op,
                        value=node.value.left
                    )
            if isinstance(node.value.left, Name):
                if node.value.left.id == node.targets[0].id:
                    return AugAssign(
                        target=node.targets[0],
                        op=node.value.op,
                        value=node.value.right
                    )


class OperatorEqualsCommand(RewriterCommand):

    def apply(self, ast):
        new_tree = fix_missing_locations(OperatorEqualsTransformer().visit(ast))
        return new_tree
