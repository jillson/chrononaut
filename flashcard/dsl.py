from StringIO import StringIO
from tokenize import generate_tokens
import operator, token
from funcparserlib.parser import (some, a, many, skip, finished, maybe, with_forward_decls)
import random
from collections import defaultdict


class Token(object):
    def __init__(self, code, value, start=(0, 0), stop=(0, 0), line=''):
        self.code = code
        self.value = value
        self.start = start
        self.stop = stop
        self.line = line

    @property
    def type(self):
        return token.tok_name[self.code]

    def __unicode__(self):
        pos = '-'.join('%d,%d' % x for x in [self.start, self.stop])
        return "%s %s '%s'" % (pos, self.type, self.value)

    def __repr__(self):
        return 'Token(%r, %r, %r, %r, %r)' % (
            self.code, self.value, self.start, self.stop, self.line)

    def __eq__(self, other):
        return (self.code, self.value) == (other.code, other.value)

def tokenize(s):
    'str -> [Token]'
    return list(Token(*t)
        for t in generate_tokens(StringIO(s).readline)
        if t[0] not in [token.NEWLINE])

def rolldice(n,d):
    return sum((random.randint(1,d) for _ in xrange(n)))


def parse(tokens,mydd):
    'Sequence(Token) -> int or float or rng or None'
    # Well known functions
    const = lambda x: lambda _: x
    unarg = lambda f: lambda x: f(*x)

    # Semantic actions and auxiliary functions
    tokval = lambda tok: tok.value
    makeop = lambda s, f: op(s) >> const(f)

    def lookup_variable(varname):
        return mydd[varname]
    
    def make_number(s):
        try:
            return int(s)
        except ValueError:
            return float(s)
    def eval_expr(z, list):
        'float, [((float, float -> float), float)] -> float'
        #Note: this is no longer legal in python 3
        return reduce(lambda s, (f, x): f(s, x), list, z)
        #return reduce(lambda s_f_x: s_f_x[1][0](s_f_x[0],s_f_x[1][1]), list, z)
        
    eval = unarg(eval_expr)

    # Primitives
    variable = (some(lambda tok: tok.code == 1)
                >> tokval
                >> lookup_variable)
    number = (
        some(lambda tok: tok.code == token.NUMBER)
        >> tokval
        >> make_number)
    
    op = lambda s: a(Token(token.OP, s)) >> tokval
    op_ = lambda s: skip(op(s))

    add = makeop('+', operator.add)
    sub = makeop('-', operator.sub)
    mul = makeop('*', operator.mul)
    div = makeop('/', operator.div)
    pow = makeop('**', operator.pow)
    mod = makeop('%', operator.mod)
    rdice = makeop('&', rolldice)

    mul_op = mul | div | mod | rdice
    add_op = add | sub

    # Means of composition
    @with_forward_decls
    def primary():
        return number | variable | (op_('(') + expr + op_(')'))
    factor = primary + many(pow + primary) >> eval
    term = factor + many(mul_op + factor) >> eval
    expr = term + many(add_op + term) >> eval

    # Toplevel parsers
    endmark = a(Token(token.ENDMARKER, ''))
    end = skip(endmark + finished)
    toplevel = maybe(expr) + end

    return toplevel.parse(tokens)





def build_vars(script):
    myddX = defaultdict(int)
    for line in script.split("\n"):
        v,myexpr = line.split("=")
        v = v.strip()
        myddX[v] = parse(tokenize(myexpr.strip()),myddX)
    return myddX


if __name__ == "__main__":
    script1 = """a = 3
    b = 4
    c = a + b"""

    script2 = """b = 4
    c = a + b"""

    print(build_vars(script1))
    print(build_vars(script2))
