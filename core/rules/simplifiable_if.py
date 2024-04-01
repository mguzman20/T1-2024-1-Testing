from ..rule import *

# Clases que permiten detectar el uso de if statements o if ternarios que 
# se pueden simplificar por la condición o la condición negada.

class SimplifiableIfVisitor(WarningNodeVisitor):

    # En especifico, se tomara en cuenta cuando un if ternario o if solo retorne True o False.
    # Tambien se agregara una alerta cuando un if statement tiene como “body” u “orelse” una asignacion
    # a la misma variable con los valores True o False.
    def visit_If(self, node: IfExp): 
        if isinstance(node.test, Constant):
            if node.test.value == True:
                self.addWarning('SimplifiableIf', node.lineno, 'if statement can be replaced with a bool(test)')
            elif node.test.value == False:
                self.addWarning('SimplifiableIf', node.lineno, 'if statement can be replaced with a bool(test)')
        elif isinstance(node.test, Assign):
            if isinstance(node.test.value in [True, False]):
                self.addWarning('SimplifiableIf', node.lineno, 'if statement can be replaced with a bool(test)')
        NodeVisitor.generic_visit(self, node)
        
        
        


class SimplifiableIfRule(Rule):
    def analyze(self, ast):
        visitor = SimplifiableIfVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
    
    @classmethod
    def name(cls):
        return 'simpl-if'
