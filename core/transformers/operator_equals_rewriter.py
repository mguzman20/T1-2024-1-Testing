from ast import *
from core.rewriter import RewriterCommand

# Clases que permiten transformar codigo que contiene x = x <operador_aritmetico_binario> z a x <operador_aritmetico_binario>= z.

class OperatorEqualsTransformer(NodeTransformer):

    def __init__(self):
        super().__init__()


class OperatorEqualsCommand(RewriterCommand):

    def apply(self, ast):
        pass