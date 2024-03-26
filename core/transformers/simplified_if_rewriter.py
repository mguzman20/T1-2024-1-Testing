from ast import *
from core.rewriter import RewriterCommand


# Clases que permiten transformar if ternarios que puedan ser simplificados usando la condicion o su negacion.

class SimplifiedIfTransformer(NodeTransformer):

    def __init__(self):
        super().__init__()


class SimplifiedIfCommand(RewriterCommand):

    def apply(self, ast):
        pass

