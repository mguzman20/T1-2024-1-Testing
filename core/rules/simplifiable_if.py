from ..rule import *

# Clases que permiten detectar el uso de if statements o if ternarios que 
# se pueden simplificar por la condición o la condición negada.

class SimplifiableIfVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()


class SimplifiableIfRule(Rule):
    def analyze(self, ast):
        pass
    
    @classmethod
    def name(cls):
        return 'simpl-if'
