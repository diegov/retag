from pyparsing import alphas, alphanums, Word, Forward, nums, Optional, OneOrMore, Group, Regex, Combine, oneOf, Literal, QuotedString
from ast import ast_node, literal_value, tag_reference, assignment, arith

class DSLEngine(object):
    
    def __init__(self, context):
        self._context = context

    def to_assign(self, name, value):
        return assignment.Assignment(name, value)

    def to_literal(self, value):
        return literal_value.LiteralValue(value)

    def to_arith(self, left, oper, right):
        return arith.Arith(left, oper, right)

    def _build_grammar(self):
        expr = Forward()

        float_lit = Combine(Word(nums) + '.' + Word(nums))
        float_lit.setName('float')
        float_lit.setParseAction(lambda x: \
                                     self.to_literal(float(x[0])))

        int_lit = Word(nums)
        int_lit.setName('int')
        int_lit.setParseAction(lambda x: \
                                   self.to_literal(int(x[0])))

        num = (float_lit | int_lit)
        num.setParseAction(lambda x: x[0])

        tag_name = Word(alphas + "_", alphanums + "_")
        tag_name.setName('tag_name')
        tag_name.setParseAction(lambda t: tag_reference.TagReference(t[0]))

        quoted_string = QuotedString('"')
        quoted_string.setParseAction(lambda s: self.to_literal(s[0]))

        oper = oneOf('+ * / -')
        oper.setParseAction(lambda o: o[0])

        lpar  = Literal("(").suppress()
        rpar  = Literal(")").suppress()

        arith = Group(lpar + expr + oper + expr + rpar)
        arith.setParseAction(lambda t: \
                                 self.to_arith(t[0][0], t[0][1], t[0][2]))

        assign = tag_name + '=' + expr
        assign.setName('assign')
        assign.setParseAction(lambda x: self.to_assign(x[0],x[2]))

        expr <<(arith|assign|tag_name|num|quoted_string)
        expr.setParseAction(lambda x: x[0])
        return expr

    def get_result(self, script):
        grammar = self._build_grammar()
        res = grammar.parseString(script)
        return res

    def execute(self, script):
        res = self.get_result(script)
        res[0].execute(self._context)
        return res
