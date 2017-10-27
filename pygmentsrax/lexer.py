;'''UY|@Qqq1 # -*- coding: utf-8 -*-
# Copyright (c) 2017 Coders Co.
# Licensed under the MIT License (https://opensource.org/licenses/MIT)

from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

#__all__ = [ 'RaxLexer' ]

class RaxLexer(RegexLexer):
  name = 'Rax'
  aliases = ['rax']
  filenames = ['*.rax']
  tokens = {
    'root': [
      (r'//.*?\n', Comment)
    ]
  }
#
#  tokens = {
#    'punctKw': [(r'[()[\]{}]', Punctuation)],
#    'opsKw': [(r'(?:[|]?><[|]?|[=]?><[=]?|[:<=!>]=|\|>|\(\)|<[:-]|:[>/\\]|\.\.|&&|\|\||\^\^|\*\*|@[|&^\\?><]|@!\?|\\/|/\\|[;.:,!-+*?/<>\\~&%^#$@|])', Operator)],
#    'castKw': [(r'\([@~|%&^#$]\)', Operator.Word)],
#    'relationalKw': [(r'(?:project|partition|select|fold)', Operator.Word)],
#    'mathcKw': [(r'(?:M_E|M_LOG2E|M_LOG10E|M_LN2|M_LN10|M_PI|M_PI_2|M_PI_4|M_1_PI|M_2_PI|M_2_SQRTPI|M_SQRT2|M_SQRT1_2)', Keyword.Constant)],
#    'mathfKw': [(r'(?:acos|asin|atan|ceil|cos|cosh|exp|fabs|floor|frexp_man|frexp_exp|log|log10|modf_int|modf_frac|sin|sinh|sqrt|tan|tanh|erf|erfc|gamma|m_j0|m_j1|lgamma|m_y0|m_y1|isnan|acosh|asinh|atanh|cbrt|expm1|ilogb|log1p|logb|rint|atan2|fmod|ldexp|pow|hypot|jn|yn|nextafter|remainder|scalb|logistic)', Operator.Word)],
#    'randomKw': [(r'\?(?:\#|&|\$|@|\^|~|\||%)\?', Keyword.Constant)],
##--
#    'keyword': [
#      (r'\%warn', Generic.Emph),
#      (r'extern', Operator.Word),
#      (r'import', Operator.Word),
#      (r'true', Operator.Word),
#      (r'false', Operator.Word),
#      include('punctKw'),
#      include('opsKw'),
#      include('castKw'),
#      include('relationalKw'),
#      include('mathcKw'),
#      include('mathfKw'),
#      include('randomKw')
#    ],
#    'number': [
#      (r'[+-]*[0-9]*\.[0-9]+(?:[e|E][+-]*0*[1-9][0-9]*)?', Number.Float),
#      (r'[+-]*[1-9][0-9]*', Number.Integer),
#      (r'[+-]*[Xx][0-9A-Fa-f]+', Number.Hex),
#      (r'[+-]*0[1-9][0-9]*', Number.Oct),
#      (r'[+-]*0+', Number.Integer)
#    ],
##--
#    'comment':    [(r'//.*?\n', Comment)],
#    'outputproc': [(r'`[A-Za-z_][A-Za-z0-9_\']+', Name.Buildin)],
#    'identifier': [(r'[A-Za-z_][A-Za-z0-9_\']+', Name.Variable)],
#    'typeof':     [(r'\\', Keyword.Type)],
#    '__variable': [(r'__[A-Za-z][A-Za-z0-9_\']+__', Name.Buildin)],
##--
#    'metadef':    [(r'\%[A-Za-z_][A-Za-z0-9_]+', Name.Builtin, 'metabody')],
#    'funcdef':    [(r'(<-)( *)({)', bygroups(Operator, Whitespace, Operator), 'funcbody')],
#    'osetdef':    [(r'{', Operator, 'osetbody')],
#    'tupledef':   [(r'\[', Operator, 'tuplebody')],
#    'stringdef':  [(r'"', String, 'strbody')],
##--
#    'root': [
#      include('stringdef'),
#      include('number'),
#      include('outputproc'),
#      include('comment'),
#      include('__variable'),
#      include('identifier'),
#      include('keyword'),
#      include('typeof'),
##--
#      include('metadef'),
#      include('funcdef'),
#      include('osetdef'),
#      include('tupledef'),
#      (r'.', Text)
#    ],
##--
#    'metabody':   [include('stringdef'), (r';', Name.Buildin, '#pop'), (r'.', Name.Buildin)],
#    'strbody':    [(r'"', String, '#pop'), (r'.', String)],
##--
#    'funcbody':   [include('root'), (r'}', Operator, '#pop')],
#    'osetbody':   [include('root'), (r'}', Operator, '#pop')],
#    'tuplebody':  [include('root'), (r']', Operator, '#pop')]
#  }
