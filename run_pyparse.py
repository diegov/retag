from pyparsing import *
import sys
from dsl_engine import *
from ast import arith


def main():
    expr = Forward()
    float_lit = Combine(Word(nums) + '.' + Word(nums))

    int_lit = Word(nums)

    num = (float_lit | int_lit)

    tag_name = Word(alphas + "_", alphanums + "_")

    oper = oneOf('+ * / -')

    lpar  = Literal("(").suppress()
    rpar  = Literal(")").suppress()

    arith = Group(lpar + expr + oper + expr + rpar)

    def to_arith(left, oper, right):
        print left
        print oper
        print right
        return arith.Arith(left, oper, right)

    arith.setParseAction(lambda t: to_arith(t[0][0], t[0][1], t[0][2]))

    assign = tag_name + '=' + expr

    expr <<(arith|assign|tag_name|num)

    print expr.parseString(sys.argv[1])

if __name__ == "__main__":
    main()
