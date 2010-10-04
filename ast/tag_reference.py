import ast_node


class TagReference(ast_node.AstNode):
    def __init__(self, ref_name):
        self.ref_name = ref_name

    def get_value(self):
        return '%placeholder_value%'

    def execute(self, tag_context):
        return tag_context.get_tag_value(self.ref_name)

    def set_value(self, tag_context, value):
        tag_context.set_tag_value(self.ref_name, value)
