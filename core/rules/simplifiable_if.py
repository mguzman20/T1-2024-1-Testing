from _ast import AST, IfExp, If, Return, Assign, Name, Constant
from typing import Any
from ..rule import *

# Clases que permiten detectar el uso de if statements o if ternarios que 
# se pueden simplificar por la condición o la condición negada.

class SimplifiableIfVisitor(WarningNodeVisitor):

    # En especifico, se tomara en cuenta cuando un if ternario o if solo retorne True o False.
    # Tambien se agregara una alerta cuando un if statement tiene como “body” u “orelse” una asignacion
    # a la misma variable con los valores True o False.
    def visit_If(self, node: If): 
        if isinstance(node.body[0], Assign) and isinstance(node.orelse[0], Assign):
            if isinstance(node.body[0].value, Constant) and isinstance(node.orelse[0].value, Constant):
                if node.body[0].value.value == True and node.orelse[0].value.value == False:
                    self.addWarning('SimplifiableIf', node.lineno, 'if statement can be replaced with a bool(test)')
                elif node.body[0].value.value == False and node.orelse[0].value.value == True:
                    self.addWarning('SimplifiableIf', node.lineno, 'if statement can be replaced with a bool(test)')
        elif isinstance(node.body[0], Return) and isinstance(node.orelse[0], Return):
            if isinstance(node.body[0].value, Constant) and isinstance(node.orelse[0].value, Constant):
                if node.body[0].value.value == True and node.orelse[0].value.value == False:
                    self.addWarning('SimplifiableIf', node.lineno, 'if statement can be replaced with a bool(test)')
                elif node.body[0].value.value == False and node.orelse[0].value.value == True:
                    self.addWarning('SimplifiableIf', node.lineno, 'if statement can be replaced with a bool(test)')
            
        NodeVisitor.generic_visit(self, node)
    
    def visit_IfExp(self, node: IfExp):
        if isinstance(node.body, Constant) or isinstance(node.orelse, Constant):
            if node.body.value == True and node.orelse.value == False:
                self.addWarning('SimplifiableIf', node.lineno, 'if statement can be replaced with a bool(test)')
            elif node.body.value == False or node.orelse.value == True:
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
