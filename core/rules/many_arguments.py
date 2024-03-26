from ..rule import *

# Clases que permiten detectar el uso de funciones que por definicion tengan más de 6 argumentos en la firma
# A veces se definen funciones con muchos argumentos, tener varios argumentos puede dañar la legibilidad del
# codigo y también indicar que el metodo puede ser más complejo de lo esperado.

class ManyArgumentsVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()
        self.currentClass = None
        self.threshold = 6

    def visit_ClassDef(self, node: ClassDef):
        self.currentClass = node.name
        NodeVisitor.generic_visit(self, node)
        self.currentClass = None

    def visit_FunctionDef(self, node: FunctionDef):
        # Si está definido dentro de una clase, asumir que uno de los argumentos será self
        if self.currentClass is not None:
            self.threshold = 7
        else:
            self.threshold = 6
            
        if len(node.args.args) > self.threshold:
            self.addWarning('ManyArgumentsWarning', node.lineno, 'function ' + node.name +
                            ' defined with many arguments!')


class ManyArgumentsRule(Rule):
    def analyze(self, ast):
        visitor = ManyArgumentsVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
    
    @classmethod
    def name(cls):
        return 'many-arguments'
