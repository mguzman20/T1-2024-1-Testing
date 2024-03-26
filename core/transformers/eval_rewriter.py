from ast import *
from core.rewriter import RewriterCommand


# Clases que permiten transformar codigo que contiene la llamada a 'eval' por 'literal_eval'.
# Considere usar 'literal_eval' para evaluar de manera segura las cadenas que pueden tener expresiones poco confiables.

class LiteralEvalTransformer(NodeTransformer):
    def visit_Call(self, node):
        if node.func.id == 'eval':
            return Call(func=Name(id='literal_eval', ctx=Load()), 
                        args=node.args, 
                        keywords=node.keywords)
        else:
            return node


class LiteralEvalRewriterCommand(RewriterCommand):
    
    def apply(self, ast):
        # La funcion fix_missing_locations se utiliza para recorrer los nodos del AST y actualizar ciertos atributos
        # (e.g., número de línea) considerando ahora la modificacion
        new_tree = fix_missing_locations(LiteralEvalTransformer().visit(ast))
        return new_tree
