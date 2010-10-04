import tag_reference
import ast_node


class Assignment(ast_node.AstNode):
    def __init__(self, tag_ref, value):
        if not isinstance(tag_ref, tag_reference.TagReference):
            msg = 'assignment target must be a tag reference, not a %s' % (str(type(tag_ref)))
            raise Exception(msg)

        self.tag_ref = tag_ref
        self.value = value

    def __str__(self):
        return "{Name = %s, Val = %s}" % (self.tag_ref.ref_name, str(self.get_value()))

    def __repr__(self):
        return str(self)

    def get_value(self):
        return self.value.get_value()

    def execute(self, tag_context):
        this_val = self.value.execute(tag_context)
        self.tag_ref.set_value(tag_context, this_val)

        return this_val
