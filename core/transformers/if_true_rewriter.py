from ast import *
from core.rewriter import RewriterCommand


# Clases que permiten transformar codigo que contiene if True y como resultado elimina el if innecesario.
# Considere solo usar el body del If si la condicion es la constante True.

class IfTrueTransformer(NodeTransformer):
    def visit_If(self, node):
        NodeTransformer.generic_visit(self, node)
        statements = node
        if isinstance(node.test, Constant):
            if node.test.value == True:
                # El body puede ser una lista de statement
                statements = node.body
        return statements


class IfTrueRewriterCommand(RewriterCommand):

    def apply(self, ast):
        # La funcion fix_missing_locations se utiliza para recorrer los nodos del AST y actualizar ciertos atributos
        # (e.g., número de línea) considerando ahora la modificacion
        new_tree = fix_missing_locations(IfTrueTransformer().visit(ast))
        return new_tree
