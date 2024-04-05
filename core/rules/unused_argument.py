from _ast import FunctionDef
from typing import Any
from ..rule import *

# Clases que permiten detectar si un argumento no fue usado

class UnusedArgumentVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()
        self.arguments = []
        self.used_arguments = []

    def visit_FunctionDef(self, node: FunctionDef):
        for arg in node.args.args:
            if arg.arg != 'self':
                self.arguments.append(arg)

        for atr in node.body:
            if isinstance(atr, Assign) or isinstance(atr, Return):
                if isinstance(atr.value, Name):
                    self.used_arguments.append(atr.value.id)
                elif isinstance(atr.value, List):
                    self.used_arguments.append(atr.value.elts)
                elif isinstance(atr.value, BinOp):
                    if isinstance(atr.value.left, Name):
                        self.used_arguments.append(atr.value.left.id)
                    if isinstance(atr.value.right, Name):
                        self.used_arguments.append(atr.value.right.id)

        for arg in self.arguments:
            if arg.arg not in self.used_arguments:
                self.addWarning('UnusedArgument', arg.lineno, arg.arg + ' argument has not been used!')

        NodeVisitor.generic_visit(self, node)


class UnusedArgumentRule(Rule):

    def analyze(self, ast):
        visitor = UnusedArgumentVisitor()
        visitor.visit(ast)
        return visitor.warningsList()

    @classmethod
    def name(cls):
        return 'unused-arg'