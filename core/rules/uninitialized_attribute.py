from ..rule import *

# Clases que permiten detectar si algun atributo no fue inicializado.
# A veces se usan algunos atributos que no estan inicializados y esto genera errores.

class UninitializedAttributeVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()
        self.class_attributes = []
        self.init_attributes = []

    def visit_FunctionDef(self, node: FunctionDef):
        if node.name == '__init__':
            for atr in node.body:
                if isinstance(atr, Assign):
                    for target in atr.targets:
                        if isinstance(target, Attribute):
                            self.init_attributes.append(target.attr)
        else:
            for atr in node.body:
                if isinstance(atr.value.left, Attribute) and isinstance(atr.value.right, Attribute):
                    left_atr = atr.value.left.attr
                    right_atr = atr.value.right.attr
                    if left_atr not in self.init_attributes:
                        self.addWarning('UninitializedAttribute', atr.lineno, left_atr + ' attribute was not initialized!')
                    if right_atr not in self.init_attributes:
                        self.addWarning('UninitializedAttribute', atr.lineno, right_atr + ' attribute was not initialized!')

        NodeVisitor.generic_visit(self, node)


class UninitializedAttributeRule(Rule):

    def analyze(self, ast):
        visitor = UninitializedAttributeVisitor()
        visitor.visit(ast)
        return visitor.warningsList()

    @classmethod
    def name(cls):
        return 'uninit-attr'