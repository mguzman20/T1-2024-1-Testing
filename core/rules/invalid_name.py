from ..rule import *

# Clases que permiten detectar el uso de un nombre invalido en clases, metodos y funciones

class InvalidNameVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()


class InvalidNameRule(Rule):
    def analyze(self, ast):
        pass
    
    @classmethod
    def name(cls):
        return 'invalid-name'
