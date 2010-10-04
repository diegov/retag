import ast_node

class LiteralValue(ast_node.AstNode):
    def __init__(self, literal):
        self.literal = literal

    def get_value(self):
        return self.literal

    def execute(self, tag_context):
        return self.get_value()
