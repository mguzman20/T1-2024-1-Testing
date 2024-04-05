from _ast import FunctionDef, ClassDef
from typing import Any
from ..rule import *

# Clases que permiten detectar el uso de un nombre invalido en clases, metodos y funciones

class InvalidNameVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()

    def visit_FunctionDef(self, node: FunctionDef):
        if not name_is_snake_case(node.name):
            if node.args.args[0].arg == 'self':
                self.addWarning('InvalidName', node.lineno, 'invalid method name ' + node.name)
            else:
                self.addWarning('InvalidName', node.lineno, 'invalid function name ' + node.name)
        NodeVisitor.generic_visit(self, node)

    def visit_ClassDef(self, node: ClassDef):
        if not name_is_camel_case(node.name):
            self.addWarning('InvalidName', node.lineno, 'invalid class name ' + node.name)
        NodeVisitor.generic_visit(self, node)


class InvalidNameRule(Rule):
    def analyze(self, ast):
        visitor = InvalidNameVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
    
    @classmethod
    def name(cls):
        return 'invalid-name'


def name_is_snake_case(name: str):
    if name[0].islower() and len(name) < 32 and len(name) > 2:
        for char in name:
            if not char.isdigit() and not char.isalpha() and char != '_':
                return False
        return True
    return False

def name_is_camel_case(name: str):
    if name[0].isupper() and len(name) > 0:
        for char in name:
            if not char.isdigit() and not char.isalpha() and char != '_':
                return False
        return True
    return False
