import ast_node

class Arith(ast_node.AstNode):
    def __init__(self, left, oper, right):
        self.left = left
        self.oper = oper
        self.right = right

    def get_value(self):
        #We can cheat with python
        return eval('selt.left.get_value() ' + self.oper + \
                 ' self.right.get_value()')

    def execute(self, tag_context):
        return eval('self.left.execute(tag_context) ' + self.oper + \
                        ' self.right.execute(tag_context)')

    def __repr__(self):
        try:
            left_str = str(self.left.get_value())
            right_str = str(self.right.get_value())
            return left_str + self.oper + right_str
        except:
            return 'failed to convert'
