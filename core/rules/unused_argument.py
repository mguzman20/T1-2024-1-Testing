from ..rule import *

# Clases que permiten detectar si un argumento no fue usado

class UnusedArgumentVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()


class UnusedArgumentRule(Rule):

    def analyze(self, ast):
        pass

    @classmethod
    def name(cls):
        return 'unused-arg'