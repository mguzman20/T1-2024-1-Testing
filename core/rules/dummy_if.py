from ..rule import *

# Clases que permiten detectar el uso de un 'if' cuya expresion es la constante 'True'.
# A veces se usa 'if' para una constante que es verdadera y esta comparacion es innecesaria porque siempre se ejecuta.

class DummyIfVisitor(WarningNodeVisitor):

    def visit_If(self, node: If):
        if isinstance(node.test, Constant):
            if node.test.value == True:
                self.addWarning('DummyIfWarning', node.lineno, 'this if does not have any sense!')
        NodeVisitor.generic_visit(self, node)


class DummyIfRule(Rule):

    def analyze(self, ast):
        visitor = DummyIfVisitor()
        visitor.visit(ast)
        return visitor.warningsList()

    @classmethod
    def name(cls):
        return 'dummy'
