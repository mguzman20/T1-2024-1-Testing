from ..rule import *

# Clases que permiten detectar si algun atributo no fue inicializado.
# A veces se usan algunos atributos que no estan inicializados y esto genera errores.

class UninitializedAttributeVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()


class UninitializedAttributeRule(Rule):

    def analyze(self, ast):
        pass

    @classmethod
    def name(cls):
        return 'uninit-attr'