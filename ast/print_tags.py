from ast_node import AstNode

class PrintTags(AstNode):
    def __init__(self):
        pass

    def get_value(self):
        return None

    def execute(self, tag_context):
        tag_context.print_tags()
        return None
        

